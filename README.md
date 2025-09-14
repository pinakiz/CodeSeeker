# 🔍 CodeSeeker: Semantic Code Search Engine

CodeSeeker is a system that lets developers search **large Python codebases** using **natural language queries** — retrieving functions by meaning, not just keywords.

---

## 🚀 Features

* Search **400,000+ Python functions** by description or intent.
* Embeddings generated with **[sentence-transformers/multi-qa-mpnet-base-dot-v1](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1)**.
* **FAISS** for efficient similarity search across millions of vectors.
* Achieves high retrieval accuracy on validation and test sets.
* Prebuilt **indexes + metadata** available on Hugging Face.

---

## 📊 Results

**Test Set Performance (23107 queries)**

* **MRR**: `0.88`
* **Recall\@1**: `82.7%` → correct result is the top hit \~83% of the time.
* **Recall\@5**: `94.9%` → correct result appears within top 5 \~95% of the time.
* **Recall\@10**: `96.7%`

These results show CodeSeeker reliably surfaces the most relevant functions.

---

## 📂 Dataset

* **400,000+ Python functions** extracted from top GitHub repositories.
* Each function includes:

  * Name
  * Docstring
  * Implementation

---

## ⚙️ How It Works

1. **Data Preparation**

   * Functions collected, cleaned, and stored with metadata.

2. **Embeddings**

   * Text (function + docstring) → encoded into dense vectors using Sentence Transformers.

3. **Indexing**

   * Vectors stored in **FAISS** for fast nearest-neighbor search.

4. **Search**

   * Query → embedding → FAISS lookup → returns top-k relevant functions.

---

## 🛠️ Usage

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/codeseeker.git
cd codeseeker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run backend (FastAPI)

```bash
uvicorn app:app --reload
```

### 4. Run frontend (Streamlit)

```bash
streamlit run ui.py
```

Now open `http://localhost:8501` and try natural language queries like:

* *"Read a CSV file into a DataFrame"*
* *"Plot a histogram with matplotlib"*
* *"Save a dataframe to hdf5"*

---

## 🔗 Resources

* 📘 **Kaggle Notebook** (training & evaluation): [https://www.kaggle.com/code/pinakiz/codeseeker](https://www.kaggle.com/code/pinakiz/codeseeker)
* 🤗 **Hugging Face Repo** (embeddings + index): [https://huggingface.co/pinakiz/codeSeeker](https://huggingface.co/pinakiz/codeSeeker)

---

## 📌 Roadmap

* [ ]   Extend to multi-language code (Java, C++, JS).
* [ ]   IDE plugin for VSCode.
* [ ]   Add reranking with cross-encoder for higher precision.

---

## 🧑‍💻 Author

Developed by [@pinakiz](https://github.com/pinakiz)
