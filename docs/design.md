# Agentic AI System Design

User task → Planner → Agents → Output streaming.

Agents:
- Retriever
- Analyzer
- Writer

Redis queue stores tasks.
Async execution used.
Retry handling implemented.
Manual batching supported.
