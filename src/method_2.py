from tasks import task_a, task_b, task_c
from utils import timing
from tqdm import tqdm
import concurrent.futures
from settings import settings


def task_a_wrapper(_):
    return task_a()


@timing
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
    method_2()
