from tqdm import tqdm

from settings import settings
from tasks import task_a, task_b, task_c
from utils import timing


@timing
def method_1():
    response = []
    for _ in tqdm(range(settings.TOTAL_EPOCHS), desc="Method 1 Progress"):
        result_a = task_a()
        result_b = task_b(result_a)
        result_c = task_c(result_b)
        response.append(result_c)


if __name__ == "__main__":
    method_1()
