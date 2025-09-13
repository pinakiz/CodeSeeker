import streamlit as st
import os
import requests
backend = st.secrets["BACK_URL"]  
API_URL = f"{backend}/search"

st.set_page_config(page_title="CodeSeeker", layout="wide")
st.title(" Semantic Code Search Engine")

query = st.text_input("Enter your query:")

if st.button("Search") and query:
    with st.spinner("Searching..."):
        try:
            response = requests.get(API_URL, params={"q": query, "k": 5}, timeout=30)
            response.raise_for_status()
            results = response.json()

            for i, func in enumerate(results, 1):
                st.markdown(f"### {i}. {func['name']}  `({func['repo']})`")
                st.code(func["code"], language="python")
                if func.get("docstring"):
                    st.markdown(f"**Docstring:** {func['docstring']}")
                if func.get("warning"):
                    st.warning(func["warning"] + f" (distance={func['distance']:.2f})")
        except Exception as e:
            st.error(f"❌ Error: {e}")
