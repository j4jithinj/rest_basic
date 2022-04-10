# rest_basic

virtualenv venv --python=python3.10 && cd venv && cd scripts && activate && cd .. && cd .. && pip install -r requirements.txt && python manage.py runserver

virtualenv venv --python=python3.10 && cd venv && cd scripts && activate && cd .. && cd .. && pip install django==3.2.8 djangorestframework django-cors-headers drf_spectacular Pillow && pip freeze > requirements.txt && django-admin startproject mysite . && python manage.py startapp myapp

python manage.py makemigrations && python manage.py migrate && python manage.py runserver

djangotest74
dt156email
pzpcykfzegqjbvwm