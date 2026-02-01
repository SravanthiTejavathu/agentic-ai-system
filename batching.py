from queue_manager import pop_task


def get_batch(size=2):
    tasks = []
    for _ in range(size):
        t = pop_task()
        if t:
            tasks.append(t)
    return tasks
