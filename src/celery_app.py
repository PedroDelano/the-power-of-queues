# src/celery_app.py
from celery import Celery
from kombu import Exchange, Queue

app = Celery("method_3")
app.conf.imports = ("src.tasks_celery",)

app.conf.broker_url = "redis://localhost:6379/0"
app.conf.result_backend = "redis://localhost:6379/1"

app.conf.task_queues = (
    Queue("fast_io", Exchange("fast_io"), routing_key="fast_io"),
    Queue("cpu_bottleneck", Exchange("cpu_bottleneck"), routing_key="cpu_bottleneck"),
)

app.conf.task_routes = {
    "task_a": {"queue": "fast_io", "routing_key": "fast_io"},
    "task_c": {"queue": "fast_io", "routing_key": "fast_io"},
    "task_b": {"queue": "cpu_bottleneck", "routing_key": "cpu_bottleneck"},
}
