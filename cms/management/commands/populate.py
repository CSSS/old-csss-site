#!/usr/bin/env python
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from cms.models import Category, Post, Announcement
from datetime import datetime

class Command(BaseCommand):
    help = "Populates database"

    def handle(self, *args, **options):
        lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

        categories = [
                        {'name':'About', 'slug':'about'},
                        {'name':'Events', 'slug':'events'},
                        {'name':'Projects', 'slug':'projects'},
                        {'name':'Comp Sci Guide', 'slug':'comp-sci-guide'},
                     ]
        posts = {
                    'About':[
                        {'title':'General', 'slug':'general', 'content':lorem},
                        {'title':'Exec', 'slug':'exec', 'content':lorem},
                        {'title':'Photos', 'slug':'photos', 'content':lorem},
                        {'title':'Docs', 'slug':'docs', 'content':lorem},
                        {'title':'Contact', 'slug':'contact', 'content':lorem},
                        ],
                    'Events':[
                        {'title':'Upcoming', 'slug':'upcoming', 'content':lorem},
                        {'title':'Frosh Week', 'slug':'frosh-week', 'content':lorem},
                        {'title':'Workshops', 'slug':'workshops', 'content':lorem},
                        ],
                    'Projects':[
                        {'title':'Hack Time', 'slug':'hack-time', 'content':lorem},
                        {'title':'Dev Tools', 'slug':'dev-tools', 'content':lorem},
                        {'title':'Team Names', 'slug':'team-names', 'content':lorem},
                        {'title':'CSSS Github', 'slug':'csss-github', 'content':lorem},
                        ],
                    'Comp Sci Guide':[
                        {'title':'Course Map', 'slug':'course-map', 'content':lorem},
                        {'title':'Software', 'slug':'software', 'content':lorem},
                        {'title':'Co-op', 'slug':'co-op', 'content':lorem},
                        ],
                }
        announcements = [
                            {'title':'First Thing', 'author':'Corbettron9000','slug':'first-thing','content':lorem,'created':datetime.now()},
                            {'title':'Second Thing', 'author':'Colintron9000','slug':'second-thing','content':lorem,'created':datetime.now()},
                            {'title':'Third Thing', 'author':'Sidtron9000','slug':'third-thing','content':lorem,'created':datetime.now()},
                            {'title':'Fourth Thing', 'author':'Kennethtron9000','slug':'fourth-thing','content':lorem,'created':datetime.now()},
                            {'title':'Fifth Thing', 'author':'Jordantron9000','slug':'fifth-thing','content':lorem,'created':datetime.now()},
                        ]
        # Create the Categories
        for category in categories:
            try:
                c = Category(**category)
                c.save()
                self.stdout.write(category['name'] + ' category created')
                
                # Create the Posts
                for post in posts[category['name']]:
                    try:
                        p = Post(**post)
                        p.category = c
                        p.save()
                        self.stdout.write(post['title'] + ' post created')
                    except IntegrityError:
                        self.stdout.write(post['title'] + ' post skipped')

            except IntegrityError:
                self.stdout.write(category['name'] + ' category skipped')
                self.stdout.write('Skipping all Posts in ' + category['name'])

        # Create the Announcements
        for announcement in announcements:
            try:
                a = Announcement(**announcement)
                a.save()
                self.stdout.write(announcement['title'] + ' announcement created')
            except IntegrityError:
                self.stdout.write(announcement['title'] + ' announcement skipped')