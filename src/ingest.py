import chromadb
from google import genai
from dotenv import load_dotenv
import os
from pypdf import PdfReader
from docx import Document
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client_genai = genai.Client(api_key=api_key)
def extract_pdf_pages(file_path):
    extracted_data = []

    file_name = os.path.basename(file_path)

    try:
        reader = PdfReader(file_path)

        for index, page in enumerate(reader.pages):

            text = page.extract_text()

            if text and text.strip():

                clean_text = " ".join(text.split())

                extracted_data.append({
                    "text": clean_text,
                    "metadata": {
                        "source": file_name,
                        "page": index + 1
                    }
                })

    except Exception as e:
        print(f"Error reading PDF {file_name}: {e}")

    return extracted_data

def extract_docx(file_path):

    document = Document(file_path)

    text = "\n".join(
        para.text
        for para in document.paragraphs
        if para.text.strip()
    )

    return [{
        "text": text,
        "metadata": {
            "source": os.path.basename(file_path),
            "page": 1
        }
    }]

def load_documents(data_folder):

    documents = []

    for file in os.listdir(data_folder):

        path = os.path.join(data_folder, file)

        if file.endswith(".pdf"):
            documents.extend(
                extract_pdf_pages(path)
            )

        elif file.endswith(".docx"):
            documents.extend(
                extract_docx(path)
            )

    return documents

def chunk_extracted_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=200
):
    chunks = []

    for page in pages:

        text = page["text"]
        metadata = page["metadata"]

        start = 0

        while start < len(text):

            end = min(
                start + chunk_size,
                len(text)
            )

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "metadata": {
                    "source": metadata["source"],
                    "page": metadata["page"],
                    "chunk_range": f"{start}-{end}"
                }
            })

            start += (
                chunk_size - chunk_overlap
            )

    return chunks

class GeminiEmbeddingFunction:
    def __call__(self, input):
        embeddings = []

        for text in input:
            response = client_genai.models.embed_content(
                model="gemini-embedding-001",
                contents=text
            )

            embeddings.append(response.embeddings[0].values)

        return embeddings
    def name(self):
        return "gemini"

def save_to_vector_db(
    chunks,
    db_path="./db"
):
    client = chromadb.PersistentClient(
        path=db_path
    )

    embedding_fn = GeminiEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="document_knowledge_base",
        metadata={"hnsw:space": "cosine"}
    )

    ids = [
        f"id_{i}"
        for i in range(len(chunks))
    ]

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        chunk["metadata"]
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )

    print(
        f"Successfully indexed {len(chunks)} chunks."
    )

if __name__ == "__main__":

    docs = load_documents("./data")

    chunks = chunk_extracted_pages(
        docs,
        chunk_size=1000,
        chunk_overlap=200
    )

    save_to_vector_db(chunks)

    print("Indexing Complete")