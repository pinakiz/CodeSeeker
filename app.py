from fastapi import FastAPI, Query
from pydantic import BaseModel
import faiss
import numpy as np
import json
from typing import List
from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download

# ---------- Hugging Face Repo ----------
REPO_ID = "pinakiz/codeSeeker"

# Files in repo
FILES = {
    "vectors": "data/functions.npy",
    "metadata": "data/metadata.json",
    "index": "data/code.index"
}

# Download from Hugging Face
VECTOR_FILE = hf_hub_download(repo_id=REPO_ID, filename=FILES["vectors"])
MAPPING_FILE = hf_hub_download(repo_id=REPO_ID, filename=FILES["metadata"])
INDEX_FILE = hf_hub_download(repo_id=REPO_ID, filename=FILES["index"])

# ---------- Load Models & Data ----------
# Load vectors
vectors = np.load(VECTOR_FILE).astype("float32")
dim = vectors.shape[1]

# Load FAISS index
index = faiss.read_index(INDEX_FILE)

# Load mapping (metadata for functions)
with open(MAPPING_FILE, "r") as f:
    functions = json.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

# ---------- Config ----------
DISTANCE_THRESHOLD = 25  # tune this value

# ---------- FastAPI Setup ----------
app = FastAPI(title="Semantic Code Search Engine")

class SearchResponse(BaseModel):
    id: int
    repo: str
    name: str
    code: str
    docstring: str
    distance: float
    warning: str

@app.get("/search", response_model=List[SearchResponse])
def search(
    q: str = Query(..., description="Your natural language query"),
    k: int = Query(5, description="Number of results to return")
):
    # Encode query into vector
    q_vec = model.encode(q).astype("float32").reshape(1, -1)

    # Search FAISS
    distances, indices = index.search(q_vec, k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        func = functions[idx]
        results.append(SearchResponse(
            id=func["id"],
            repo=func.get("repo", ""),
            name=func.get("name", ""),
            code=func.get("code", ""),
            docstring=func.get("docstring", ""),
            distance=float(dist),
            warning="⚠️ Low semantic similarity" if dist > DISTANCE_THRESHOLD else ""
        ))
    return results
