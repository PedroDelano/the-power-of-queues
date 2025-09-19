import random

import requests


def task_a(sess=requests.session()) -> int:
    r = sess.get("https://ifconfig.me", timeout=10)
    r.raise_for_status()
    return len(r.text)


def task_b(value: int) -> int:
    assert isinstance(value, int)
    for _ in range(int(1e7)):
        value += random.random()
    return int(value)


def task_c(value: int, sess=requests.session()) -> int:
    assert isinstance(value, int)
    r = sess.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    r.raise_for_status()
    return len(r.json()) * value
