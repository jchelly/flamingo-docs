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

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'piccolo_theme'
html_static_path = ['_static']
html_title = 'FLAMINGO Data Release'

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
