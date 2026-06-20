# Document Question Answering Bot using RAG

## Introduction

This project was developed as part of an AI Engineering Internship assignment to understand the practical implementation of Retrieval-Augmented Generation (RAG). The main objective of this project is to build a document-based question answering system that can answer user queries using information available inside uploaded documents.

Large Language Models are powerful, but they cannot access private files or recently created documents. This project solves that problem by retrieving relevant information from documents and then generating answers using Google Gemini.

## Problem Statement

Traditional language models sometimes generate incorrect answers when the required information is not present in their training data. They also cannot access private documents such as company reports, research papers, or business documents.

The aim of this project is to build a system that can:

* Read documents from local storage.
* Store document information in a vector database.
* Retrieve relevant information based on user questions.
* Generate answers only from the retrieved document content.

## Project Objective

The primary objective of this project is to develop a document question answering system that provides accurate answers from uploaded documents instead of relying completely on the language model's internal knowledge.

## Technologies Used

| Technology        | Purpose                          |
| ----------------- | -------------------------------- |
| Python            | Core programming language        |
| Google Gemini API | Embeddings and answer generation |
| ChromaDB          | Vector database                  |
| PyPDF             | PDF text extraction              |
| Python-Docx       | DOCX file processing             |
| Python-Dotenv     | Environment variable management  |
| Streamlit         | Optional user interface          |



## Project Workflow

The project follows the Retrieval-Augmented Generation approach.

1. Documents are collected from the data folder.
2. Text is extracted from PDF and DOCX files.
3. The extracted content is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. The embeddings are stored in ChromaDB.
6. User questions are converted into embeddings.
7. Similar document chunks are retrieved.
8. Retrieved context is provided to Gemini.
9. Gemini generates the final answer.

## Why RAG?

RAG helps overcome two important limitations of large language models:

* Lack of access to private documents.
* Generation of incorrect or hallucinated information.

By retrieving relevant information from the uploaded documents before generating answers, the system produces more reliable responses.

## Chunking Strategy

The extracted text is divided into chunks of 1000 characters with an overlap of 200 characters.

The overlap is maintained to ensure that important information present at chunk boundaries is not lost. This improves the quality of retrieval during similarity search.

## Embedding Model

Google Gemini embedding models are used to convert document text into vector representations. These vectors help identify semantically similar content during retrieval.

## Why ChromaDB?

ChromaDB was selected because:

* It is lightweight.
* It works locally without requiring a server.
* It supports persistent vector storage.
* It is easy to integrate with Python applications.

## Project Structure

document-qa-bot/

├── data/

├── src/

│   ├── config.py

│   ├── ingest.py

│   ├── query.py

│   └── main.py

├── README.md

├── requirements.txt

└── .gitignore

## Installation Steps

1. Clone the repository.

2. Create a virtual environment.

3. Activate the environment.

4. Install the required packages.

pip install -r requirements.txt

5. Create a .env file.

GEMINI_API_KEY=your_api_key

6. Run the document indexing script.

python src/ingest.py

7. Start the application.

python src/main.py

## Run Locally 

streamlit run app.py 

## Results

The system successfully:

* Extracts text from PDF and DOCX files.
* Stores document embeddings in ChromaDB.
* Retrieves relevant information based on user questions.
* Generates answers using Google Gemini.
* Produces context-based responses from the uploaded documents.

## Challenges Faced

During the development of this project, several challenges were encountered:

* Dependency compatibility issues between ChromaDB and Gemini libraries.
* Changes in Gemini API versions.
* Package installation errors.
* Managing vector database versions.
* Handling document chunk sizes effectively.

Solving these issues helped in understanding the practical challenges involved in AI application development.

## Future Improvements

Some possible future improvements are:

* Streamlit web interface.
* Support for additional file formats.
* OCR support for scanned documents.
* Chat history functionality.
* Improved source citations.
* Multi-document collections.

## Learning Outcomes

Through this project, I gained practical knowledge in:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Semantic search
* Document processing
* Google Gemini integration
* ChromaDB
* Python project development
* API integration

## Features 

- Ask questions from documents
- Powered by Gemini API
- Streamlit web interface 

## Live Demo

https://document-app-bot-a6vht9hdqhyjyymj6f4qbj.streamlit.app/

