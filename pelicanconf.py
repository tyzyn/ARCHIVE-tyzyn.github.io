#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Chris Tyson'
SITENAME = 'Chris Tyson'
DESCRIPTION = "Blog description."
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "monospace"

DIRECT_TEMPLATES = ['blog']
PAGINATED_DIRECT_TEMPLATES = ['blog']

STATIC_PATHS = ['documents']
#MD_EXTENSIONS = ['codehilite(noclasses=True, pygments_style=native)', 'extra']
