import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/search"

st.title("Semantic Code Search Engine")

query = st.text_input("Enter your query:")

if st.button("Search") and query:
    with st.spinner("Searching..."):
        response = requests.get(API_URL, params={"q": query, "k": 5})
        results = response.json()
        
        for i, func in enumerate(results, 1):
            st.markdown(f"### {i}. {func['name']}  `({func['repo']})`")
            st.code(func["code"], language="python")
            if func["docstring"]:
                st.markdown(f"**Docstring:** {func['docstring']} {func['warning']}")
