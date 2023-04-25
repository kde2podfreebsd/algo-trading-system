up:
	docker compose -f docker-compose-local.yaml up -d

down:
	docker compose -f docker-compose-local.yaml down && docker network prune --force

# Clean cache
clean:
	find . -name __pycache__ -type d -print0|xargs -0 rm -r --
	rm -rf .idea/

test:
	pytest app/TaLib/Test/MomentumIndicatorsTest.py

alembic_init:
	alembic init migrations

alembic_rev:
	alembic revision --autogenerate -m 'init'

alembic_upgrade:
	alembic upgrade heads

server_up:
	uvicorn app.main:app

pre_commit:
	pre-commit run flake8 --all-files

pylint:
	pylint $(git ls-files '*.py')
