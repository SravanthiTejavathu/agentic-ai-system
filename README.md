# Agentic AI System for Multi-Step Tasks

## Overview
This project implements an Agentic AI system capable of handling complex multi-step tasks by coordinating multiple specialized agents using an asynchronous execution pipeline and message queue.

The system breaks down user tasks, assigns them to agents, processes them asynchronously, and streams responses back to the user.

---

## Features
- Multi-agent architecture
- Task decomposition and orchestration
- Asynchronous execution pipeline
- Streaming responses
- Redis-based message queue
- Retry and failure handling
- Manual batching logic
- Parallel agent execution
- Execution logging for monitoring

---

## Agent Roles
1. **Retriever Agent**
   - Fetches or gathers task data.

2. **Analyzer Agent**
   - Processes and analyzes retrieved information.

3. **Writer Agent**
   - Generates final output for user.

---

## System Workflow
User Task → Planner → Orchestrator → Agents → Streaming Output

Steps:
1. User submits task.
2. Task broken into steps.
3. Steps assigned to agents.
4. Agents execute asynchronously.
5. Partial results streamed back.

---

## Technology Stack
- Python
- FastAPI
- Redis
- AsyncIO
- Uvicorn

---

## Project Structure
agentic-ai-system/
│
├── agents/
│ ├── retriever.py
│ ├── analyzer.py
│ └── writer.py
│
├── docs/
│ └── design.md
│
├── main.py
├── planner.py
├── queue_manager.py
├── batching.py
├── orchestrator.py
├── retry_handler.py
├── streaming.py
├── requirements.txt
└── README.md

---

## How to Run

### 1. Install Dependencies
pip install -r requirements.txt


### 2. Start Redis Server
cd C:\Redis
.\redis-server.exe


### 3. Run Application
uvicorn main:app --reload


### 4. Open API
http://127.0.0.1:8000/docs


---

## Failure Handling
Agents simulate failures and retry automatically, ensuring resilience and system robustness.

---

## Scalability Considerations
- Agents can run in parallel.
- Queue supports distributed task handling.
- Agents can be deployed independently.

---

## Future Improvements
- Deploy agents as microservices
- Add monitoring dashboard
- Add distributed scaling

---

## Author
Sravanthi – B.Tech IT Student