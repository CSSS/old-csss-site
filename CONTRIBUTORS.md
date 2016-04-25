How to Contribute
=================

Welcome! And thank you for wanting to make our site better. Open discussion
for site improvements can be found [here](CSSS/csss-site/issues/18).

Here is some information that can help you get started:

Dependencies
------------
- Python 3
- Django >= 1.8
- `django_markdown` package (`pip install django_markdown`)

Handy Django Commands
---------------------
* Create a new app: `python manage.py startapp <appname>`
* Tell Django about model changes: `python manage.py makemigrations <appname>`
* Check migration SQL: `python manage.py sqlmigrate <appname> <migration number>`
* Check for project errors: `python manage.py check`
* Apply migrations: `python manage.py migrate`
* Open django shell: `python manage.py shell`
* Run app tests: `python manage.py test <appname>`
* Populate database: `python manage.py populate`

