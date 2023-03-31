up:
	docker compose -f docker-compose-local.yaml up -d

down:
	docker compose -f docker-compose-local.yaml down && docker network prune --force
  
# Clean cache
clean:
	find . -name __pycache__ -type d -print0|xargs -0 rm -r --
