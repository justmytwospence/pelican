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

# Sidebar
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 50
#ABOUT_ME = ''
#AVATAR = 'images/avatar.png'

# Top Menu
DISPLAY_ARCHIVES = False
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))
DISPLAY_ARTICLE_INFO = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Set paths to resources
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'Misc'
FILENAME_METADATA = '(?P<slug>.*)' # Filename = slug
USE_FOLDER_AS_CATEGORY = True

# Plugins
STATIC_PATHS = ['images', 'pdfs']
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook',
		   'pelican-dynamic',
		   'pelican_youtube']

# Development settings
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None