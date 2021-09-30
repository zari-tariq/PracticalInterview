# Introduction
This is a small django project which have only crud operations. For fron-end I use Html, css, Bootstrap and Jquery.For backend python. It consist only two pages
one is for login and signup and second for crud operations.

# Requirements:
Install IDE(pycharm or vscode).
Install python 3.9.
Download project from github repository.
Extract project in pycharm project folder.
On terminal run the command pip install django.
Install postgresql.
Create an empty database.

# Run commands and Instructions
In settings.py replace the name and password of database you created.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'practicequiz',
         'USER': 'postgres',
         'PASSWORD': 'aaa',
         'HOST':'localhost' }}
In terminal run command pip install psycopg2 for postgresql.
then run these commands python manage.py makemigrations and python manage.py migrate these commands will migrate all models to the database.
Run command python manage.py runserver. It will show a link in cmd click on this link you will see the interface. you can simply click the login button and it will take you to the
next page on which we can store the data. 


