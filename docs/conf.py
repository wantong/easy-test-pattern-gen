# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'easy test pattern gen'
copyright = '2026, winterlii'
author = 'winterlii'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# 核心：ReadTheDocs主题
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'navigation_depth': 3,    # 目录最多展开3级，和verilator一致
    'collapse_navigation': False, # 默认不全部折叠（打开页面直接看到完整树）
    'sticky_navigation': True,
    'logo_only': True,        # 只显示logo，不显示项目文字标题
}

# 自定义css，用来替换logo、微调颜色（复刻verilator蓝色logo栏）
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
