# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

# -- Project information -----------------------------------------------------

import sys
sys.setrecursionlimit(15000)

project = 'discord.py-message-components'
copyright = '2022, Mathieu Corsham aka. mccoder.py'
author = 'Mathieu Corsham aka. mccoder.py'

version = ''
with open('../discord/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

# The full version, including alpha/beta/rc tags.
release = version

# This assumes a tag is available for final releases
branch = 'developer' if version.endswith('a') else 'v' + version



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

f = globals().get('napoleon_google_docstring', None)
del f

"""extensions = [
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'sphinxcontrib.contentui',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'builder',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'details',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',
] #'sphinx.ext.intersphinx', 'sphinxcontrib.napoleon', 'sphinx.ext.napoleon',"""

extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.contentui',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'details',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',
]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

autodoc_member_order = 'bysource'
autodoc_default_flags = ['members']
autodoc_typehints = 'none'

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aio': ('https://docs.aiohttp.org/en/stable/', None),
  'req': ('http://docs.python-requests.org/en/latest/', 'requests.inv')
}

html_context = {
  'discord_invite': 'https://discord.gg/sb69muSqsg',
  'discord_extensions': [
    ('discord.ext.commands', 'ext/commands'),
    ('discord.ext.tasks', 'ext/tasks'),
  ],
}

resource_links = {
  'discord': 'https://discord.gg/sb69muSqsg',
  'issues': 'https://github.com/mccoderpy/discord.py-message-components/issues',
  'discussions': 'https://github.com/mccoderpy/discord.py-message-components/discussions',
  'examples': 'https://github.com/mccoderpy/discord.py-message-components/tree/%s/examples' % branch,
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
# }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './images/discord_py_message_components_logo.ico'

extlinks = {
    'issue': ('https://github.com/mccoderpy/discord.py-message-components/issues/%s', 'GH-'),
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'basic'

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
html_search_scorer = '_static/scorer.js'

html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]

# The master toctree document.
master_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '_static/style.css']
