DOCKER=docker
COVERAGE=coverage
run:
	$(DOCKER) build -t secfi:latest -f Dockerfile .
	$(DOCKER) run -p 8000:8000 secfi:latest 

test:
	$(COVERAGE) run manage.py test apps.stocks.tests --settings=config.settings
	$(COVERAGE) report
