#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Spencer Boucher'
SITENAME = 'justmytwospence'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

# Theme
THEME = 'bootstrap3'
BOOTSTRAP_NAVBAR_INVERSE = True
#BOOTSTRAP_THEME = 'darkly'
TYPOGRIFY = True

# Sidebar
#HIDE_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 30
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))
#GITHUB_USER = 'justmytwospence'
#ABOUT_ME = ''
#AVATAR = 'images/avatar.png'

# Menus and navigation
DISPLAY_ARTICLE_INFO = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 5

# Set paths to resources
STATIC_PATHS = ['images', 'pdfs']
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook',
		   'pelican-dynamic']
EXTRA_HEADER = open('_nb_header_custom.html').read()
FILENAME_METADATA = '(?P<slug>.*)'
USE_FOLDER_AS_CATEGORY = True

# Development settings
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None