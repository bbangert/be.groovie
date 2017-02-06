.PHONY: install build

install:
	pip install -r requirements.txt

build:
	tinker -b

publish:
	aws s3 cp --recursive --acl public-read blog/html s3://be-groovie-site/
