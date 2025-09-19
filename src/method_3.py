import time
import json

from celery import chain

from settings import settings
from tasks_celery import task_a, task_b, task_c


def submit_n_jobs():
    results = []
    for _ in range(settings.TOTAL_EPOCHS):
        ch = chain(
            task_a.s().set(queue="fast_io"),
            task_b.s().set(queue="cpu_bottleneck"),
            task_c.s().set(queue="fast_io"),
        )
        results.append(ch.apply_async())
    return results


if __name__ == "__main__":
    start = time.perf_counter()
    async_results = submit_n_jobs()
    values = [r.get() for r in async_results]
    elapsed = time.perf_counter() - start
    with open("method_3_time.json", "w") as f:
        json.dump({"elapsed_seconds": elapsed}, f, indent=2)
    print(f"Tempo total de execução salvo em method_3_time.json: {elapsed:.2f} s")
