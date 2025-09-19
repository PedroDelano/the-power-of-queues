build-infrastructure:
	docker run --rm -d -p 6379:6379 --name redis redis
	uv run celery -A src.celery_app:app worker -l INFO
	uv run celery -A src.celery_app:app worker -Q fast_io -c 8 -l INFO
	uv run celery -A src.celery_app:app worker -Q cpu_bottleneck -c 1 -l INFO

stop-infrastructure:
	pkill -f fast_io
	pkill -f cpu_bottleneck
	docker stop redis
	docker rm redis

run-experiments:
	docker pull redis
	make build-infrastructure &
	sleep 5
	uv run src/method_1.py
	uv run src/method_2.py
	PYTHONPATH=$(CURDIR) uv run src/method_3.py
	make stop-infrastructure
