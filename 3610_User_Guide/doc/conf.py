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
import sys

from sphinx.builders.html import StandaloneHTMLBuilder

# -- Project information -----------------------------------------------------

# TODO
# WHAT TO DO ABOUT COPYRIGHTS - this is for all the docs! not the cof.py file itself!
#
copyright = '2019-2021, XMOS Ltd'
author = 'XMOS Ltd'

# ----------------------------------------------
# get environment variables (set as part of make .ps1 (powershell script) file)
# to set project name and version which show up below the XMOS logo
env_doc_title = os.getenv("DOC_TITLE")
env_doc_version = os.getenv("DOC_VERSION")

if env_doc_title != None:
    project = env_doc_title
else:
    project = 'Documentation'

if env_doc_version != None:
    release = "(V{})".format(env_doc_version)
else:
    release = ''

html_title = "{} {}".format(project, release) #overrides the default format that adds the word "documentation" to the project and release



# ----------------------------------------------
StandaloneHTMLBuilder.supported_image_types = [
    "image/svg+xml",
    "image/gif",
    "image/png",
    "image/jpeg",
]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "breathe",
    'sphinx.ext.autosectionlabel',
]


# Breathe Configuration
breathe_projects = {"TMP": "./_build/_doxygen/xml/"}
breathe_default_project = "TMP"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/README.rst', '**/CHANGELOG.rst', '**/LICENSE.rst', '**/CONTRIBUTIONS.rst', 'COPYRIGHTS.rst']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

html_logo = "./rst/images/xmos_logo.png"
html_theme_options = {
    "sidebar_hide_name" : False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# -- Options for sphinx_copybutton -------------------------------------------

copybutton_prompt_text = r"\$ |\(gdb\) "
copybutton_prompt_is_regexp = True

#My setup for figures
numfig = True
numfig_secnum_depth = 1


autosectionlabel_prefix_document = True

html_sidebars = {'**':[
    "sidebar/brand.html",
    "sidebar/search.html",
    "sidebar/navigation.html",
    "sidebar/ethical-ads.html",
    'versioning.html',
]}

