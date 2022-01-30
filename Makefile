build:
	docker build -t to_let_life_api .

clean:
	if [ $(shell lsof -t -i:80) ]; then kill -9 $(shell lsof -t -i:80); fi ;

logs:
	did=$(shell docker ps | grep '80' | awk '{ print $$1 }'); \
	if [ "$$did" ]; then docker logs $(shell docker ps | grep '80' | awk '{ print $$1 }') -f ; \
	else echo "no to_let_life_api container found"; fi;

dockerstop:
	did=$(shell docker ps | grep "80" | awk '{ print $$1 }'); \
	if [ "$$did" ]; \
	then docker stop $(shell docker ps | grep '80' | awk '{ print $$1 }'); \
	echo "go-docker-optimized stopped"; \
	docker logs $$did > ../logs/"$$did"_"$(shell date +"%Y_%m_%d_%I_%M_%p").log" ; \
	else echo "no to_let_life_api container found"; fi;

dev: dockerstop clean
	docker run --env-file ../.env.txt -d --restart unless-stopped -e STAGE=dev -p 80:4000 to_let_life_api

local: dockerstop clean
	docker run --env-file ../.env.txt -d --restart unless-stopped -e STAGE=local -p 80:4000 to_let_life_api
