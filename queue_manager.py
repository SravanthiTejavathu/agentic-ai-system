import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

QUEUE_NAME = "tasks"

def push_task(task):
    r.rpush(QUEUE_NAME, json.dumps(task))

def pop_task():
    data = r.lpop(QUEUE_NAME)
    if data:
        return json.loads(data)
    return None
