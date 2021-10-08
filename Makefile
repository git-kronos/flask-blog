#python run.py

run: format
	# flask run
	python run.py

init:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

format:
	black .

db-recreate:
	python data.py
