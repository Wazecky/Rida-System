# Steps to setup
* pip install sklearn
* pip install -r requirements.txt
* Create Rida_Osmaniya Database in PostgreSQL.
* Configure Database section in settings.py.
* python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver
* Login to Django Administration page (http://127.0.0.1:8000/admin) and add details of superuser in EC_Admins.
* Navigate to http://127.0.0.1:8000 and Login as admin