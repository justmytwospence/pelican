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
#BOOTSTRAP_THEME = 'slate'
BOOTSTRAP_NAVBAR_INVERSE = True

# Sidebar
HIDE_SIDEBAR = False
#ABOUT_ME = ''
#AVATAR = 'images/avatar.png'
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
#GITHUB_USER = 'justmytwospence'
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 20

# Menus and navigation
USE_FOLDER_AS_CATEGORY = False
DISPLAY_ARTICLE_INFO = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Custom resources
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'pdfs', 'raw_html', 'extra/custom.css']
EXTRA_PATH_METADATA = {
	'extra/custom.css': {'path': 'static/custom.css'}
}
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.youtube']
EXTRA_HEADER = open('_nb_header_custom.html').read()
TYPOGRIFY = True

PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
