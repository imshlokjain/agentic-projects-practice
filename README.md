# LangChain & LangGraph Projects

A collection of end-to-end projects built to learn and explore **LangChain** and **LangGraph** through practical implementation.

The repository progresses from fundamental LLM applications to RAG systems, tool-calling agents, stateful LangGraph workflows, multi-agent systems, and finally a complete automation platform.

Rather than learning LangChain and LangGraph only through isolated examples, each project focuses on building a complete application while introducing new concepts incrementally.

---

## Projects

### 1. AI Research Assistant

An AI-powered research assistant capable of processing research queries and generating structured responses.

**Concepts covered:**

- Chat models
- System, human, and AI messages
- Prompt templates
- LCEL chains
- Conversation history
- Output parsers
- Tool calling
- Web search
- Research pipelines

---

### 2. PDF Question Answering — RAG

A Retrieval-Augmented Generation system that allows users to ask questions about PDF documents.

**Concepts covered:**

- Document loaders
- Text splitting
- Embeddings
- Vector databases
- Semantic search
- Retrievers
- Retrieval-Augmented Generation (RAG)
- Context injection
- RAG chains

Basic architecture:

```text
PDF
 │
 ▼
Document Loader
 │
 ▼
Text Splitter
 │
 ▼
Embeddings
 │
 ▼
Vector Store
 │
 ▼
Retriever
 │
 ▼
LLM
 │
 ▼
Answer
```

---

### 3. SQL Database Agent

An AI agent capable of understanding natural-language questions, querying a SQL database, and returning understandable answers.

**Concepts covered:**

- SQL tools
- Tool calling
- Database interaction
- Natural language to SQL
- Agent reasoning
- Structured outputs
- Query execution
- Error handling

Example:

```text
User
 │
 │ "Which products generated the most revenue?"
 ▼
Agent
 │
 ▼
Generate SQL
 │
 ▼
Database
 │
 ▼
Query Result
 │
 ▼
LLM
 │
 ▼
Natural-language answer
```

---

### 4. Multi-Tool AI Assistant

An AI assistant capable of selecting and using different tools depending on the user's request.

Possible tools include:

- Web search
- Calculator
- Database queries
- Document retrieval
- Custom Python functions
- APIs

**Concepts covered:**

- LangChain tools
- Tool schemas
- Tool calling
- Agent loops
- Tool selection
- Routing
- Structured outputs
- Error handling

Architecture:

```text
                 ┌── Web Search
                 │
User ──► Agent ──┼── Calculator
                 │
                 ├── Database
                 │
                 └── Document Search
```

---

### 5. LangGraph Workflow Engine

A stateful AI workflow built using LangGraph.

Unlike a simple linear chain, the application represents execution as a graph containing nodes, edges, conditions, and shared state.

**Concepts covered:**

- StateGraph
- Nodes
- Edges
- Graph state
- Conditional edges
- Routing
- Cycles
- Checkpointing
- Persistence
- Human-in-the-loop workflows

Example:

```text
START
  │
  ▼
Analyze Request
  │
  ▼
Select Action
  │
  ├──── Search ────┐
  │                │
  ├──── Tool ──────┤
  │                │
  └──── Respond ───┤
                   │
                   ▼
                  END
```

---

### 6. Multi-Agent Research System

A research system where multiple specialized agents collaborate to complete a larger research task.

Possible agents:

```text
Research Coordinator
        │
        ├── Search Agent
        │
        ├── Research Agent
        │
        ├── Fact-Checking Agent
        │
        └── Report Writer
```

**Concepts covered:**

- Multi-agent architectures
- Agent specialization
- Agent communication
- Shared state
- Task delegation
- Supervisor patterns
- LangGraph orchestration
- Parallel workflows
- Result aggregation

---

### 7. Automation Platform

The final project combines the concepts explored throughout the repository into an AI-driven automation system.

The platform will execute multi-step workflows where LLMs, tools, APIs, and deterministic application logic can work together.

**Concepts covered:**

- Workflow orchestration
- Stateful execution
- Conditional routing
- Tool execution
- API integrations
- Persistent state
- Retry and failure handling
- Human approval steps
- Long-running workflows
- LangGraph orchestration

Conceptual architecture:

```text
                 User / Trigger
                       │
                       ▼
                Workflow Engine
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         LLM Node            Logic Node
             │                   │
             ▼                   ▼
        Tool Selection      Condition
             │                   │
      ┌──────┼──────┐            │
      ▼      ▼      ▼            │
    API     RAG     DB            │
      │      │      │             │
      └──────┴──────┴─────────────┘
                    │
                    ▼
               Update State
                    │
                    ▼
              Next Workflow
                    │
                    ▼
                  Result
```

---

## Learning Progression

The projects are intentionally ordered so that each project introduces a new layer of LLM application development.

```text
LLM Fundamentals
       │
       ▼
Prompts & Messages
       │
       ▼
Chains
       │
       ▼
RAG
       │
       ▼
Tools
       │
       ▼
Agents
       │
       ▼
LangGraph
       │
       ▼
Stateful Workflows
       │
       ▼
Multi-Agent Systems
       │
       ▼
Automation Platform
```

---

## Core Technologies

The repository primarily explores:

- Python
- LangChain
- LangGraph
- Groq
- Open-source LLMs
- Vector databases
- SQL databases
- Retrieval-Augmented Generation
- Tool calling
- AI agents
- Multi-agent systems

Different projects may introduce additional technologies where required.

---

## Repository Structure

```text
langchain-langgraph-projects/
│
├── 01-ai-research-assistant/
│   └── README.md
│
├── 02-pdf-rag/
│   └── README.md
│
├── 03-sql-database-agent/
│   └── README.md
│
├── 04-multi-tool-assistant/
│   └── README.md
│
├── 05-langgraph-workflow-engine/
│   └── README.md
│
├── 06-multi-agent-research-system/
│   └── README.md
│
├── 07-automation-platform/
│   └── README.md
│
└── README.md
```

Each project contains its own documentation covering its architecture, setup, implementation, and concepts learned.

---

## Objective

The objective of this repository is to develop a practical understanding of building LLM-powered applications from the ground up.

The progression focuses on understanding not only how to use LangChain and LangGraph APIs, but also the underlying application architecture:

```text
Prompt
  ↓
Model
  ↓
Chain
  ↓
Retriever
  ↓
Tool
  ↓
Agent
  ↓
State
  ↓
Graph
  ↓
Multi-Agent Workflow
  ↓
Automation System
```

By the final project, the repository progresses from basic LLM invocation to designing complete stateful and agentic automation workflows.
