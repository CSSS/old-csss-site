CSSS Website
============

What it needs
-------------
- New exec list, with photos
- Pages: About (General/Exec/Photos/Docs/Contact),
Events (Upcoming/Froshweek/Workshops),
Projects (Hack Time/Dev Tools/Team Names/CSSS Github),
Comp Sci Guide (Course Map/Software/Co-op)
- New URL!
- Contact info repeated on the bottom of both pages

What we can use
---------------
- Python + Django
- Bootstrap
- MySQL (SQLite?)

Handy Django Commands
---------------------
* Create a new app: `python manage.py startapp <appname>`
* Tell Django about model changes: `python manage.py makemigrations <appname>`
* Check migration SQL: `python manage.py sqlmigrate <appname> <migration number>`
* Check for project errors: `python manage.py check`
* Apply migrations: `python manage.py migrate`
* Open django shell: `python manage.py shell`
* Run app tests: `python manage.py test <appname>`

Design
------
- Logo top-left
- Navbar of categories to the right of that
- Home page contains announcements and carousel with images
- Topbar follows user down the page (but shrinks)
- Footer contains: copyright, icons, csss@sfu.ca email
- Coloured side bars?
- Announcement format: Title, "By <person> on <date>", content
- Use Frosh theme colours every year (for side bars?)
- Side bars: shadows on the edges for depth
