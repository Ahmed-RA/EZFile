# EZFile

Simple file management web app with google account login.
This project was created as part of the GSD course "Software Development Project"

Developed by: Ahmed Abdullah (email: ahmed.abdullah@informatik.hs-fulda.de)
Prerequisite: Python 3.9.2 or higher installed (tested only on 3.9.2 as of 28.07.2021)

# How to run:

1. Install django and django all-auth with the following two commands:
`pip install django` 
`pip install django all-auth`

2. Clone this repository, then modify the EZFile/settings.py file as follows:
- Change SECRET_KEY (How to generate one: (https://tech.serhatteker.com/post/2020-01/django-create-secret-key/))
- Modify DIRS in the TEMPLATES variable to an absolute path to the "templates" folder according to your file system.
- Modify the DATABASES dictionary to your implemented DB. Make sure to create a schema first.

3. Run in project root:
`python manage.py makemigrations` 
then:
`python manage.py migrate` 
These two commands should connect to the DB and create the respective tables automatically

4. Go to this guide (https://whizzoe.medium.com/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) and follow from step 7.
Make sure in the DB you have in your "django_site" an entry with domain "127.0.0.1:8000" and id "2", 
otherwise change the SITE_ID variable in settings.py so that it is the same as in the django
admin webiste.

5. If not already running, run in project root: 
`python manage.py runserver`

6. Server should be running and serving the web app at : 127.0.0.1:8000

Note: there is a bug where if you try to login with an admin account into the web app (not the /admin site) there will be an error screen.
Create a new user either by logging in with Google or by signing up.
