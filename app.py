import streamlit as st
from src.query import query_rag_pipeline

st.set_page_config(page_title="Document QA Bot")

st.title("📄 Document Question Answering Bot")

question = st.text_input(
    "Ask a question about your documents:"
)

if st.button("Get Answer"):
    answer, citations = query_rag_pipeline(question)

    st.subheader("Answer")
    st.write(answer)

    st.subheader("Sources")
    for citation in citations:
        st.write(citation)