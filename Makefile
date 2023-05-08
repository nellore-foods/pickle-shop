default:
	. ./venv/bin/activate && cd src && python manage.py runserver

env:
	@-virtualenv venv
	. ./venv/bin/activate && pip install -r requirements.txt

freeze:
	@. ./venv/bin/activate && pip freeze > requirements.txt
