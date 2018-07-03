import sys

import os
from sphinx import application

from slex import os_ex
from .. import paths


def setup(app):
    """
    Args:
        app (application.Sphinx):
    """
    sys.path.append(paths.THEME_PYTHON_DIR)

    # noinspection PyUnresolvedReferences
    import instance_attributes

    os_ex.copy_tree(paths.THEME_STATIC_DIR, os.path.join(app.outdir, '_static', ))
    app.add_stylesheet(os.path.join('css', 'custom.css'))

    # this is a walk around, to be able to add links to general index and module index
    # inside the sidebar, with absolute link paths
    # TODO: there must be a better way to put index and module index links into sidebar
    app.config.template_bridge = 'template_loader.TemplateLoader'

