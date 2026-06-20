import streamlit as st
from src.query import query_rag_pipeline

st.set_page_config(page_title="Document QA Bot")

st.title("📄 Document Question Answering Bot")

question = st.text_input(
    "Ask a question about your documents:"
)

if st.button("Get Answer"):
    if question:
        answer = query_rag_pipeline(question)
        st.write("### Answer")
        st.write(answer)