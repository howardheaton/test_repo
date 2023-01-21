# Configuration file for the Sphinx documentation builder.

# -- Path Setup

import os
import sys
sys.path.insert(0, os.path.abspath('./../..'))

import sphinx.apidoc
def setup(app):
    sphinx.apidoc.main(['-f', #Overwrite existing files
                        '-T', #Create table of contents
                        #'-e', #Give modules their own pages
                        '-E', #user docstring headers
                        #'-M', #Modules first
                        '-o', #Output the files to:
                        './source/_autogen/', #Output Directory
                        './../arteryfe', #Main Module directory
                        ]
    )

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
