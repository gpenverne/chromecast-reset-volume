install:
	pip3 install -r requirements.txt
	cp config.py.dist config.py

apply:
	python3 cli.py

server:
	python3 server.py
