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
THEME = '../pelican-bootstrap3'
BOOTSTRAP_THEME = 'solarizedlight'
PYGMENTS_STYLE = 'solarizeddark'
FAVICON = 'favicon.ico'

# Display Switches
HIDE_SIDEBAR = False
DISPLAY_ARCHIVES = False
DISPLAY_ARTICLE_INFO = True
DISPLAY_TAGS_INLINE = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Variables
DEFAULT_PAGINATION = 6
CLEAN_SUMMARY_MAXIMUM = 0
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 30
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),
          ('RSS', SITEURL + 'feeds/all.atom.xml'))

# Plugins
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['better_figures_and_images',
           'liquid_tags.notebook',
           'pelican-dynamic',
           'pelican_youtube',
           'render_math',
           'neighbors']

# URLs
# These settings cause articles, pages, and
# categorys to share a namespace; collions will
# generate an error! But I prefer the simpler URLs.

FILENAME_METADATA = '(?P<slug>.*)'  # Filename = slug

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

TAG_URL = "tags/{slug}/"
TAG_SAVE_AS = "tags/{slug}/index.html"
TAGS_URL = "tags/"
TAGS_SAVE_AS = "tags/index.html"

# Development settings
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
