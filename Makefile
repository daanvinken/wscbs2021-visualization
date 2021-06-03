requirements:
	pipenv lock -r > requirements.txt

build:
	brane unpublish -f visualization 1.0.0
	brane remove -f visualization
	brane build container.yml
	brane push visualization 1.0.0