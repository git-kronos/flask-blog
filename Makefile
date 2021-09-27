#flask run

run:
	 python run.py

init:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# db.create_all()
# db.drop_all()