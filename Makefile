.phony: build push

all: build push 

build: 
	docker build -t vallard/twitter-scrape . 

push: 
	docker push vallard/twitter-scrape


