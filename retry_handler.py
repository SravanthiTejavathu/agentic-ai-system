import asyncio

async def retry(func, data, retries=3):
    for _ in range(retries):
        try:
            return await func(data)
        except Exception:
            await asyncio.sleep(1)
    return "Agent failed after retries"
