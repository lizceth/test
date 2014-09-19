import sys, os

extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'


# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'{{ project_name }}'
copyright = u'2014, ChangeMyName'

# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'


exclude_patterns = ['_build']


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

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
html_static_path = ['_static']

htmlhelp_basename = '{{ project_name }}doc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', '{{ project_name }}.tex', u'{{ project_name }} Documentation',
   u'ChangeToMyName', 'manual'),
]

man_pages = [
    ('index', '{{ project_name }}', u'{{ project_name }} Documentation',
     [u'ChangeToMyName'], 1)
]



texinfo_documents = [
  ('index', '{{ project_name }}', u'{{ project_name }} Documentation',
   u'ChangeToMyName', '{{ project_name }}', 'One line description of project.',
   'Miscellaneous'),
]

