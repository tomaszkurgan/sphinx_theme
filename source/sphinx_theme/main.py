import os

from slex import inspect_ex
from sphinx_theme import paths


def init():
    caller = inspect_ex.get_caller()
    template_rel_path = os.path.relpath(
        os.path.join(paths.THEME_DIR, 'templates'),
        os.path.dirname(caller.filename)
    )

    # add templates
    caller.frame.f_globals['templates_path'].append(template_rel_path)

    # add plugins
    caller.frame.f_globals['extensions'].append('sphinx_theme.ext.sphinx_paramlinks')
    caller.frame.f_globals['extensions'].insert(0, 'sphinx_theme.ext.sphinx_theme')
