from tqdm import tqdm

from settings import settings
from tasks import task_a, task_b, task_c
import time
import json


def method_1():
    response = []
    for _ in tqdm(range(settings.TOTAL_EPOCHS), desc="Method 1 Progress"):
        result_a = task_a()
        result_b = task_b(result_a)
        result_c = task_c(result_b)
        response.append(result_c)


if __name__ == "__main__":
    start = time.perf_counter()
    result = method_1() 
    elapsed = time.perf_counter() - start

    with open("method_1_time.json", "w") as f:
        json.dump({"elapsed_seconds": elapsed}, f, indent=2)

    print(f"Tempo total de execução salvo em method_1_time.json: {elapsed:.2f} s")
