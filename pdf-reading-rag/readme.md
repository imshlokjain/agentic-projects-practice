# PDF RAG Assistant

A conversational **Retrieval-Augmented Generation (RAG)** application that allows users to ask questions about the contents of a PDF. The system retrieves relevant sections from the PDF using vector search and uses **GPT-OSS 20B through Groq** to generate grounded answers.

The project also supports conversational follow-up questions through question rewriting and chat history.

---

## Architecture

```text
                         PDF
                          │
                          ▼
                    PDF Loader
                          │
                          ▼
                       Chunks
                          │
                          ▼
                 Cohere Embeddings
                          │
                          ▼
                    Chroma DB
                          │
                          │
                          ▼
                    User Question
                          │
                          ▼
                Conversation History
                          │
                          ▼
                 Question Rewriter
                          │
                          ▼
               Standalone Query
                          │
                          ▼
                     Retriever
                          │
                          ▼
                  Relevant Chunks
                          │
                          ▼
                       Prompt
                          │
                          ├── Question
                          ├── PDF Context
                          └── Chat History
                          │
                          ▼
                   GPT-OSS 20B
                    via Groq
                          │
                          ▼
                       Answer
                          │
                          ▼
                      Sources
```

---

## Features

* Load and process PDF documents
* Split documents into smaller chunks
* Generate vector embeddings using Cohere
* Store embeddings in Chroma
* Perform semantic similarity search
* Generate answers using GPT-OSS 20B through Groq
* Ground answers using retrieved PDF context
* Maintain conversational history
* Rewrite follow-up questions into standalone retrieval queries
* Display PDF source/page information
* Refuse to fabricate information when the PDF does not contain enough information

---

## Tech Stack

| Technology    | Purpose                          |
| ------------- | -------------------------------- |
| Python        | Application language             |
| LangChain     | RAG pipeline and LLM integration |
| Cohere        | Text embeddings                  |
| Chroma        | Vector database                  |
| Groq          | LLM inference                    |
| GPT-OSS 20B   | Answer generation                |
| PyPDF         | PDF loading                      |
| python-dotenv | Environment variables            |

---

## Project Structure

```text
pdf-reading-rag/
│
├── app.py
├── ingest.py
│
├── embeddings.py
├── vector_store.py
├── retriever.py
├── llm.py
├── prompt.py
├── question_rewriter.py
├── sources.py
│
├── sample.pdf
├── chroma_db/
│
├── .env
├── .gitignore
└── README.md
```

### File responsibilities

#### `ingest.py`

Processes the PDF and creates the vector database.

```text
PDF
 ↓
Load
 ↓
Split
 ↓
Embed
 ↓
Chroma
```

Run this whenever the source PDF changes.

---

#### `embeddings.py`

Creates the Cohere embedding model used to convert text into numerical vectors.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

---

#### `vector_store.py`

Creates and loads the Chroma vector database.

---

#### `retriever.py`

Creates the retriever used to perform semantic search against the Chroma database.

---

#### `llm.py`

Initializes GPT-OSS 20B through Groq.

```python
ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    timeout=30,
    max_retries=2,
)
```

---

#### `prompt.py`

Defines the prompt used by the LLM to answer questions using the retrieved PDF context.

It instructs the model to:

* use the provided document context
* avoid outside information
* avoid hallucinating
* use conversation history
* admit when the document doesn't contain enough information

---

#### `question_rewriter.py`

Converts conversational questions into standalone questions suitable for vector retrieval.

For example:

```text
User:
What topics are covered under Stability?

User:
Explain the first one.
```

is transformed approximately into:

```text
Explain the definition of stability.
```

This makes the question understandable to the vector retriever.

---

#### `sources.py`

Extracts source and page information from retrieved documents so the application can display where the answer came from.

---

#### `app.py`

The main application.

It connects:

```text
Question
 ↓
Question Rewriter
 ↓
Retriever
 ↓
PDF Context
 ↓
LLM
 ↓
Answer
```

and maintains conversation history between questions.

---

# Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd pdf-reading-rag
```

---

## 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

Install the required packages:

```bash
pip install langchain
pip install langchain-community
pip install langchain-chroma
pip install langchain-cohere
pip install langchain-groq
pip install chromadb
pip install pypdf
pip install python-dotenv
```

---

# Environment Variables

Create a `.env` file:

```env
COHERE_API_KEY=your_cohere_api_key
GROQ_API_KEY=your_groq_api_key
```

Do **not** commit `.env` to Git.

The `.gitignore` should contain:

```gitignore
__pycache__/
*.py[cod]
.venv/
.env
chroma_db/
.DS_Store
```

---

# Running the Project

## Step 1 — Add your PDF

Place your PDF in the project directory.

For example:

```text
pdf-reading-rag/
└── sample.pdf
```

---

## Step 2 — Ingest the PDF

Run:

```bash
python ingest.py
```

The ingestion process:

```text
Loading PDF...
      ↓
Splitting PDF...
      ↓
Creating embeddings...
      ↓
Creating vector store...
      ↓
Vector store created successfully.
```

This creates:

```text
chroma_db/
```

The vector database contains the embeddings and document information required for retrieval.

---

## Step 3 — Run the application

```bash
python app.py
```

You should see:

```text
==================================================
PDF RAG Assistant
Type 'exit' to quit.
==================================================
```

You can now ask questions about the PDF.

---

# Example

### Question

```text
You: What topics are covered under Stability?
```

The system:

```text
Question
 ↓
Embedding
 ↓
Chroma search
 ↓
Relevant PDF chunks
 ↓
GPT-OSS 20B
```

might respond:

```text
Assistant:

Under Stability the following topics are covered:

- Definition
- Routh-Hurwitz criterion
- Root locus techniques
- Nyquist criterion
- Bode plots
- Relative stability
- Gain and phase margins
```

The application also displays the source:

```text
Sources:
- sample.pdf, page 3
```

---

# Conversational Questions

The system supports follow-up questions.

For example:

```text
You:
What topics are covered under Stability?
```

Then:

```text
You:
Explain the first topic.
```

The question rewriter converts the second question into a standalone retrieval query.

Conceptually:

```text
"Explain the first topic."
              ↓
      Question Rewriter
              ↓
"Explain the definition of stability."
              ↓
          Retriever
              ↓
        PDF Context
              ↓
             LLM
```

This allows the application to understand references such as:

* "the first one"
* "the second one"
* "explain it"
* "what about that?"
* "the previous topic"

---

# How RAG Works in This Project

RAG stands for **Retrieval-Augmented Generation**.

Instead of asking the LLM to answer entirely from its pretrained knowledge, the application first retrieves relevant information from the PDF.

```text
User Question
      │
      ▼
Vector Search
      │
      ▼
Relevant PDF Chunks
      │
      ▼
LLM + Retrieved Context
      │
      ▼
Grounded Answer
```

### Embeddings

Text is converted into numerical vectors:

```text
"Routh-Hurwitz criterion"
            ↓
Embedding Model
            ↓
[0.12, -0.43, 0.78, ...]
```

The question is also converted into a vector.

Chroma then compares the vectors to find semantically similar chunks.

---

# Why Chroma?

A normal database might search for exact keywords.

A vector database allows **semantic search**.

For example:

```text
Question:
How can stability be analyzed?
```

can retrieve a chunk containing:

```text
Routh-Hurwitz criterion, Root locus techniques,
Nyquist criterion, Bode plots...
```

even though the wording isn't identical.

---

# Grounding

The LLM receives:

```text
PDF Context
+
User Question
+
Conversation History
```

and is instructed to answer using the provided document.

If the PDF doesn't contain enough information, the application should respond that the information isn't available rather than inventing an answer.

For example, if the PDF only lists:

```text
Stability
Definition
```

but doesn't actually provide the definition, the model should not fabricate one.

---

# Ingestion vs Application

There are two distinct stages.

### Ingestion

```text
ingest.py

PDF
 ↓
Chunks
 ↓
Embeddings
 ↓
Chroma
```

This is performed when the PDF changes.

### Querying

```text
app.py

Question
 ↓
Retriever
 ↓
Chroma
 ↓
Relevant chunks
 ↓
LLM
 ↓
Answer
```

The vector database is **loaded**, not recreated, when running `app.py`.

---

# Updating the PDF

If you replace `sample.pdf` with a different document:

1. Delete the old vector database:

```bash
rm -rf chroma_db
```

2. Run ingestion again:

```bash
python ingest.py
```

3. Start the application:

```bash
python app.py
```

This ensures the vectors correspond to the new PDF.

---

# Limitations

This project is intentionally a learning-oriented RAG implementation.

Current limitations include:

* Basic semantic retrieval
* Fixed number of retrieved chunks
* No reranking
* No hybrid keyword + vector search
* No sophisticated retrieval evaluation
* Conversation history is maintained in memory
* The application processes one PDF knowledge base at a time
* No persistent conversation memory

These are potential improvements for future projects.

---

# Key Concepts Learned

This project demonstrates:

```text
PDF Processing
      ↓
Document Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Semantic Retrieval
      ↓
RAG
      ↓
Prompt Engineering
      ↓
LLM Integration
      ↓
Conversation History
      ↓
Conversational RAG
```

The main distinction is:

> **The retriever finds information; the LLM uses that information to generate the answer.**

---

# Project 2 Outcome

By completing this project, you have progressed from a standalone conversational LLM application to a system that can combine:

```text
LLM
+
External Knowledge
+
Vector Search
+
Conversation History
```

This forms the foundation for more advanced AI applications such as document assistants, knowledge-base agents, research systems, and agentic workflows.
