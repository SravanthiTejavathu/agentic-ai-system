# Post-Mortem Document – Agentic AI System

## 1. Scaling Issue Encountered
During development, sequential agent execution caused increased response latency as each agent waited for the previous one to complete. This created a bottleneck when handling multiple requests.

To address this, asynchronous parallel execution was introduced.

---

## 2. Design Decision to Change
Initially, all agents were executed sequentially within a single orchestrator process. In future iterations, agents would be deployed as independent microservices communicating through queues for better scalability and fault isolation.

---

## 3. Development Trade-offs
To keep implementation simple and submission-ready, a lightweight architecture was chosen instead of full distributed deployment. This reduces complexity but limits scalability compared to production systems.
