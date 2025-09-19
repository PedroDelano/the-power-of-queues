build-infrastructure:
	docker run --rm -d -p 6379:6379 --name redis redis
	uv run celery -A src.celery_app:app worker -l INFO
	uv run celery -A src.celery_app:app worker -Q fast_io -c 8 -l INFO
	uv run celery -A src.celery_app:app worker -Q cpu_bottleneck -c 1 -l INFO

stop-infrastructure:
	docker stop redis
	docker rm redis
	docker ps -a | grep "celery" | awk '{print $1}' | xargs docker stop
	docker ps -a | grep "celery" | awk '{print $1}' | xargs docker rm