# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'Omada SDN'
# copyright = u'2021, Gheldmandare'
# author = 'Vincent Tu'

# The full version, including alpha/beta/rc tags
release = '0.2'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_copybutton'
]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'default'
html_logo = 'logo.png'
html_favicon = 'tplink.ico'

# -- Shared files ------------------------------------------------------------
templates_path = ['_templates']
html_static_path = ['_static']