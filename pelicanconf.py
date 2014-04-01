#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Spencer Boucher'
SITENAME = 'justmytwospence'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
SITEURL = ''

# Theme
THEME = 'bootstrap3'
BOOTSTRAP_NAVBAR_INVERSE = True
#BOOTSTRAP_THEME = 'darkly'
TYPOGRIFY = True
PYGMENTS_STYLE = 'github'
FAVICON = '/favicon.ico'

# Display Switches
DISPLAY_ARCHIVES = False
DISPLAY_ARTICLE_INFO = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Variables
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 50
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))
#ABOUT_ME = ''
#AVATAR = 'images/avatar.png'

# Set paths to resources
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'Misc'
FILENAME_METADATA = '(?P<slug>.*)' # Filename = slug
USE_FOLDER_AS_CATEGORY = True

# Plugins
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook',
		   'pelican-dynamic',
		   'pelican_youtube']

# Development settings
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None