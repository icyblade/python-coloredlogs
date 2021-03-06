"""Documentation build configuration file for the `coloredlogs` package."""

import os
import sys

# Add the 'coloredlogs' source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'coloredlogs'
copyright = u'2015, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from coloredlogs import __version__ as coloredlogs_version  # noqa

# The short X.Y version.
version = '.'.join(coloredlogs_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = coloredlogs_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python=('https://docs.python.org/2', None),
    humanfriendly=('https://humanfriendly.readthedocs.io/en/latest', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'classic'

# Output file base name for HTML help builder.
htmlhelp_basename = 'coloredlogsdoc'


def setup(app):
    """
    Configure the autodoc extension not to skip ``__init__()`` members.

    Based on http://stackoverflow.com/a/5599712/788200.
    """
    app.connect('autodoc-skip-member', (lambda app, what, name, obj, skip, options:
                                        False if name == '__init__' and obj.__doc__ else skip))
