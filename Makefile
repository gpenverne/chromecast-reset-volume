install:
	pip install -r requirements.txt
	cp config.py.dist config.py

apply:
	python3 reset-volume.py
