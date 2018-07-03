import os

SELF_DIR = os.path.dirname(__file__)
ROOT_DIR = SELF_DIR
assert os.path.basename(ROOT_DIR) == 'sphinx_theme'

THEME_DIR = os.path.join(ROOT_DIR, 'theme')
THEME_STATIC_DIR = os.path.join(THEME_DIR, 'static')
THEME_TEMPLATES_DIR = os.path.join(THEME_DIR, 'templates')
THEME_PYTHON_DIR = os.path.join(THEME_DIR, 'python')
