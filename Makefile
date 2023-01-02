DOCKER=docker
run:
	$(DOCKER) build -t secfi:latest -f Dockerfile .
	$(DOCKER) run -p 8000:8000 secfi:latest 
