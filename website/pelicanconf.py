#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kelsey Ferro'
SITENAME = 'green thumb project'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GTP Github', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (('Home', '/welcome-to-the-green-thumb-project.html'),
             ('Blog', '/blog.html'),
             ('Documentation', '/documentation.html'),
             ('About', '/about-me.html'),
             ('Get Involved!', '/contribute.html'),
             ('Contact Us', '/contact-info.html'),
             )




# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
