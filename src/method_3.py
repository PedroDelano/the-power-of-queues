import time

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
    end = time.perf_counter()
    print(f"Finished {len(values)} chains in {end - start:.2f} seconds")
