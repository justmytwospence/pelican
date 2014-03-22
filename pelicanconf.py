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
#BOOTSTRAP_THEME = 'slate'
BOOTSTRAP_NAVBAR_INVERSE = True

HIDE_SIDEBAR = True
#SHOW_ABOUTME = True
#ABOUT_ME = "I'm spencer!"
AVATAR = 'images/avatar.png'
DISPLAY_TAGS_INLINE = True
#GITHUB_USER = 'justmytwospence'
TWITTER_USERNAME = 'justmytwospence'
TWITTER_WIDGET_ID = '413946059455361024'

DISPLAY_ARTICLE_INFO = True
	
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'pdfs', 'raw_html', 'extra/custom.css']
EXTRA_PATH_METADATA = {
	'extra/custom.css': {'path': 'static/custom.css'}
}

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['liquid_tags.notebook']
EXTRA_HEADER = open('_nb_header_custom.html').read()

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('GitHub', 'http://github.com/justmytwospence'),
          ('LinkedIn', 'http://linkedin.com/in/spencerboucher'),)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
