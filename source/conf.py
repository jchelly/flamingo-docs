# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FLAMINGO Data Release'
copyright = '2025, John Helly'
author = 'John Helly'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_title = 'FLAMINGO Data Release'

# The piccolo theme doesn't have an option to have a logo AND text in the nav bar, hence this hack
html_short_title = '<image src="/flamingo/_static/FLAMINGO_navbar_brand_stroke.png" class="flamingo_logo"> FLAMINGO Data Release'

#
# Theme selection
#
# Read the Docs
#html_theme = 'sphinx_rtd_theme'

# Piccolo
html_theme = 'piccolo_theme'
# Don't collapse toc when using Piccolo theme
#html_theme_options = {
#    "globaltoc_collapse": False
#}

# Immaterial
#extensions = ["sphinx_immaterial"]
#html_theme = 'sphinx_immaterial'

#
# Additional files needed for the file browser: msgpack library for decoding
# responses, highlight.js syntax highlighter, dompurify and some CSS
# customization.
#
html_css_files = [
    'custom.css',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/styles/default.min.css',
]
html_js_files = [
    'https://unpkg.com/@msgpack/msgpack@2.8.0',
    'https://unpkg.com/dompurify@3.2.3/dist/purify.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/highlight.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/languages/python.min.js',
    'https://unpkg.com/@highlightjs/cdn-assets@11.11.1/languages/yaml.min.js',
]
