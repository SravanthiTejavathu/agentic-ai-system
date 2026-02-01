from agents import retriever, analyzer, writer
from retry_handler import retry
import asyncio
import datetime

agent_map = {
    "retriever": retriever.run,
    "analyzer": analyzer.run,
    "writer": writer.run,
}

async def run_single_step(step):
    agent = step["agent"]
    data = step["data"]

    print(f"[{datetime.datetime.now()}] Running agent: {agent}")

    func = agent_map[agent]
    result = await retry(func, data)

    print(f"[{datetime.datetime.now()}] Completed agent: {agent}\n")

    return f"{agent} -> {result}"

async def execute_steps(steps):
    print("\n===== Agent Pipeline Started =====")

    # Run steps concurrently
    tasks = [run_single_step(step) for step in steps]
    outputs = await asyncio.gather(*tasks)

    print("===== Agent Pipeline Completed =====\n")

    return outputs
