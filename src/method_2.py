import concurrent.futures

from tqdm import tqdm

from settings import settings
from tasks import task_a, task_b, task_c
import time, json


def task_a_wrapper(_):
    return task_a()


def method_2():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        jobs = list(
            tqdm(
                executor.map(task_a_wrapper, range(settings.TOTAL_EPOCHS)),
                desc="Method 2 (Task A)",
                total=settings.TOTAL_EPOCHS,
            )
        )

    result_b = [
        task_b(result_a)
        for result_a in tqdm(
            jobs, desc="Method 2 (Task B)", total=settings.TOTAL_EPOCHS
        )
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        jobs = list(
            tqdm(
                executor.map(task_c, result_b),
                desc="Method 2 (Task C)",
                total=settings.TOTAL_EPOCHS,
            )
        )


if __name__ == "__main__":
    start = time.perf_counter()
    result = method_2()
    elapsed = time.perf_counter() - start

    with open("method_2_time.json", "w") as f:
        json.dump({"elapsed_seconds": elapsed}, f, indent=2)

    print(f"Tempo total de execução salvo em method_2_time.json: {elapsed:.2f} s")
