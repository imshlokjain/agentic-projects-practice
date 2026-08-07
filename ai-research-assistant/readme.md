# 🤖 AI Research Assistant

An AI-powered Research Assistant built using **LangGraph**, **LangChain**, and **Groq LLMs**. This project demonstrates how to create a stateful conversational AI capable of deciding when to use external tools (DuckDuckGo Search) to answer user queries.

---

## 🚀 Features

- Conversational AI powered by Groq LLM
- LangGraph workflow orchestration
- Stateful conversations
- Conditional tool execution
- DuckDuckGo web search integration
- Modular architecture
- System prompt for agent behavior
- Interactive command-line interface

---

## 🏗️ Project Structure

```text
ai-research-assistant/
│
├── graph/
│   ├── __init__.py
│   ├── state.py          # Graph state definition
│   ├── nodes.py          # Assistant & Tool nodes
│   ├── edges.py          # Conditional routing logic
│   └── builder.py        # Graph construction
│
├── tools/
│   ├── __init__.py
│   └── search.py         # DuckDuckGo Search Tool
│
├── lessons/              # LangChain practice files
│
├── app.py                # Main application
├── config.py             # LLM configuration
├── requirements.txt
├── .env
└── README.md
```

---

# 🧠 Architecture

```text
                 User Query
                     │
                     ▼
            HumanMessage Added
                     │
                     ▼
             LangGraph START
                     │
                     ▼
             Assistant Node
                     │
             ┌───────┴────────┐
             │                │
       Needs Tool?        No Tool?
             │                │
             ▼                ▼
         Tool Node         Final Answer
             │
             ▼
     Search Results Added
             │
             ▼
      Assistant Node Again
             │
             ▼
              END
```

---

# ⚙️ Technologies Used

- Python 3
- LangChain
- LangGraph
- LangChain Community
- Groq API
- DuckDuckGo Search
- Pydantic

---

# 📦 Installation

Clone the repository.

```bash
git clone <repository-url>
cd ai-research-assistant
```

Create a virtual environment.

```bash
python3 -m venv .venv
```

Activate it.

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Running the Project

```bash
python3 app.py
```

Example:

```text
==================================================
AI Research Assistant
Type 'exit' to quit.
==================================================

You: What is LangGraph?

Assistant:
LangGraph is a framework built on top of LangChain...
```

---

# 🧩 Core Components

## 1. State

The graph state stores the conversation history.

```python
ResearchState
```

It automatically carries information between nodes.

---

## 2. Assistant Node

Responsibilities:

- Reads the current conversation
- Adds the system prompt
- Calls the LLM
- Produces the next AI message

---

## 3. Tool Node

Responsibilities:

- Executes tools requested by the model
- Returns tool outputs
- Adds them back into the conversation

Current tool:

- DuckDuckGo Search

---

## 4. Conditional Edges

LangGraph decides what happens after the assistant node.

If the model requests a tool:

```text
Assistant
      │
      ▼
Tool Node
      │
      ▼
Assistant
```

Otherwise:

```text
Assistant
      │
      ▼
END
```

---

# 🔍 Search Tool

The project integrates DuckDuckGo Search using LangChain.

```python
@tool
def search_web(query: str):
    ...
```

The assistant automatically decides whether to call this tool.

---

# 💡 System Prompt

The assistant is instructed to:

- Answer clearly
- Search only when necessary
- Avoid unnecessary tool calls
- Summarize search results
- Use Markdown formatting

---

# 📚 Concepts Learned

This project covers:

- LangGraph
- Graph workflows
- Nodes
- Edges
- State management
- Tool calling
- LangChain Tools
- System prompts
- Conversation memory
- LLM orchestration

---

# 🛠 Future Improvements

- Wikipedia Tool
- ArXiv Research Tool
- PDF Reader
- Memory Persistence
- Streaming Responses
- Multi-Agent Research Workflow
- Report Generation
- Vector Database Integration
- RAG Pipeline

---

# 📸 Example Workflow

```text
User
 │
 ▼
Assistant Node
 │
 ▼
Need Search?
 │
 ├── No
 │      │
 │      ▼
 │   Final Answer
 │
 └── Yes
        │
        ▼
  DuckDuckGo Search
        │
        ▼
 Assistant Node
        │
        ▼
   Final Answer
```

---

# 🎯 Learning Outcomes

By completing this project, you have learned how to:

- Build a stateful AI application with LangGraph
- Create reusable LangChain tools
- Implement graph-based workflows
- Integrate external APIs
- Design modular AI applications
- Use system prompts effectively
- Build conversational AI agents

---

# 📄 License

This project is intended for educational purposes and personal learning.