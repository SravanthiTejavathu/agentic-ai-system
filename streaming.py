import asyncio

async def stream_generator(messages):
    for msg in messages:
        yield msg + "\n"
        await asyncio.sleep(0.5)
