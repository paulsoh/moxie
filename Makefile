migrate:
	python moxie/manage.py makemigrations user ideas
	python moxie/manage.py migrate
