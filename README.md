# EZFile

Simple file management web app.


Prerequisite: 
- Python 3.9.2 or higher installed (tested only on 3.9.2 as of 28.07.2021)
- Mysql server up and running.

# How to run:

1. Install django, django all-auth, and mysqlclient for python with the following commands:
`pip install django` 
`pip install django all-auth`
`pip install mysqlclient`


2. Clone this branch, then modify the EZFile/settings.py file as follows:

- (Optional) Modify DIRS in the TEMPLATES variable to an absolute path to the "templates" folder according to your file system.
- Modify the DATABASES dictionary to your implemented DB. Make sure to create a schema first.

3. Run in project root:
`python manage.py makemigrations` 
then:
`python manage.py migrate` 
These two commands should connect to the DB and create the respective tables automatically

4. If not already running, run in project root: 
`python manage.py runserver`

5. Server should be running and serving the web app at : 127.0.0.1:8000

Notes for settings.py (incase of production environment):
- Change SECRET_KEY (How to generate one: (https://tech.serhatteker.com/post/2020-01/django-create-secret-key/))
- Change ALLOWED HOSTS accordingly
- Change DEBUG to False


