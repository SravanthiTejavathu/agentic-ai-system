import asyncio

counter = 0

async def run(data):
    global counter
    await asyncio.sleep(1)

    # Fail first time only
    if counter == 0:
        counter += 1
        print("Analyzer agent failed! Retrying...")
        raise Exception("Temporary failure")

    return f"Analyzed content of '{data}'"
