import asyncio

async def run(data):
    await asyncio.sleep(1)
    return f"Written final response for '{data}'"
