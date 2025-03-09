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
import subprocess
import sphinx_rtd_theme
import json
import jsonschema_restructuredtext

def get_context():
    """Return the current RTD version or git branch name"""
    try:
        git_context = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        ).strip().decode("utf-8")

        # Check for RTD version, default to git_version if not on RTD
        context = os.getenv("READTHEDOCS_VERSION", git_context)

        return context
    except Exception:
        return ""

# -- Project information -----------------------------------------------------

project = 'DAS Metadata'
copyright = '2024, International FDSN'
author = 'FDSN'

version = '2.0'
release = '2.0.0'

# -- General configuration ---------------------------------------------------

# Default in Sphinx 2, but not in older versions
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx_rtd_theme',
  'sphinx_design'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['schema/*.rst', 'venv/*', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Allow :strike:`TEXT` to be used in RST for strikethrough styling
rst_prolog = """
.. role:: strike
    :class: strike
"""

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'sticky_navigation': False,
    "navigation_depth": 3,  # Sidebar opens level limit
}

html_logo='_static/FDSN-logo.png'
html_favicon = '_static/favicon.ico'
html_title = 'DAS Metadata'
html_show_sphinx = False
html_search_language = 'en'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
  'css/fdsn_rtd_theme.css',
  'css/custom.css',
]

html_js_files = [
  'js/sidebar_context.js',
]

# -- Generate JSON schema documentation -------------------------------
import jsonschema_restructuredtext

with open('schema/DAS-Metadata.v2.0.schema.json') as f:
    schema_json = json.load(f)

schema_rst = jsonschema_restructuredtext.generate(schema_json,
                                                  section_punctuation=["-", "^", "~", '+', '*', '+', '.'],)

with open('schema/schema_tables.rst', 'w') as f:
    f.write(schema_rst)

# Enable sphinxmark for draft documentation
if get_context() == "draft":
    extensions.append("sphinxmark")
    sphinxmark_enable = True
    sphinxmark_div = "document"
