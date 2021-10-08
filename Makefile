#python run.py

run: format
	python run.py

init:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

format:
	black .

db-restore:
	python core/data.py

clean-pycache:
	find . -type d -name __pycache__ -exec rm -r {} \+