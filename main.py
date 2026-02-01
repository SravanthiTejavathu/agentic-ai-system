from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from planner import break_task
from orchestrator import execute_steps
from queue_manager import push_task

from streaming import stream_generator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic AI running"}

@app.post("/task")
async def submit_task(task: str):
    push_task(task)
    return {"message": "Task added to queue"}

@app.get("/run")
async def run_task(task: str):
    steps = break_task(task)
    results = await execute_steps(steps)

    return StreamingResponse(
        stream_generator(results),
        media_type="text/plain"
    )
