#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Spencer Boucher'
SITENAME = 'justmytwospence'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

THEME = 'bootstrap3'
#BOOTSTRAP_THEME = 'lumen'
BOOTSTRAP_NAVBAR_INVERSE = True
HIDE_SIDEBAR = True

STATIC_PATHS = ['images', 'pdfs']
MARKUP = ('md', 'ipynb')
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['ipythonnb', 'liquid_tags.notebook']
EXTRA_HEADER = open('_nb_header_custom.html').read()

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
