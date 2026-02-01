def break_task(task: str):
    return [
        {"agent": "retriever", "data": task},
        {"agent": "analyzer", "data": task},
        {"agent": "writer", "data": task},
    ]
