import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client_genai = genai.Client(api_key=api_key)


class GeminiEmbeddingFunction:
    def __call__(self, input):
        embeddings = []

        for text in input:
            response = client_genai.models.embed_content(
                model="gemini-embedding-001",
                contents=text
            )

            embeddings.append(
                response.embeddings[0].values
            )

        return embeddings


def query_rag_pipeline(
    user_query,
    db_path="./db",
    k=3
):
    client = chromadb.PersistentClient(
        path=db_path
    )

    collection = client.get_collection(
        name="document_knowledge_base"
    )

    results = collection.query(
        query_texts=[user_query],
        n_results=k
    )

    context_blocks = []

    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

        context_blocks.append(
            f"[Source: {meta['source']}, "
            f"Page: {meta['page']}]\n{doc}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are a Document Question Answering Assistant.

Use ONLY the context below.

If answer is not available, say:
'I cannot find the answer in the provided documents.'

Context:
{context}

Question:
{user_query}
"""

    response = client_genai.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text