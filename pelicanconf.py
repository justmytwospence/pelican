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
BOOTSTRAP_THEME = 'solarizedlight'
#BOOTSTRAP_NAVBAR_INVERSE = True
PYGMENTS_STYLE = 'solarizeddark'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
FAVICON = '/favicon.ico'
TYPOGRIFY = True

# Display Switches
DISPLAY_ARCHIVES = False
DISPLAY_ARTICLE_INFO = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Variables
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 30
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))
#ABOUT_ME = ''
#AVATAR = 'images/avatar.png'

# Plugins
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook',
		   'pelican-dynamic',
		   'pelican_youtube',
		   'neighbors']

# Set paths to resources
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'Misc'
FILENAME_METADATA = '(?P<slug>.*)' # Filename = slug
USE_FOLDER_AS_CATEGORY = True

# URLs 
# These settings cause articles, pages, and 
# categorys to share a namespace; collions will
# generate an error! But I prefer the simpler URLs. 
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"

# Development settings
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None