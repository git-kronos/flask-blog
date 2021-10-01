#python run.py

run: format
	flask run

init:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

format:
	black .
# db.create_all()
# db.drop_all()