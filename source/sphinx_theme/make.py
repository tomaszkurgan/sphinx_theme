import shutil
import tempfile

import jinja2
import os

from slex import inspect_ex
from . import paths
from . import utils


def find_docs_root_dir(start_path):
    path = start_path
    while os.path.basename(path) not in ('doc', 'docs'):
        temp_path = os.path.dirname(path)
        if temp_path == path:
            raise RuntimeError("Can't find docs root directory.")
        path = temp_path
    return path


class prepare_make_file(object):
    def __init__(self, project_name, source_dir, build_dir):
        make_file_template_basename = 'make.bat_t' if os.name == 'nt' else 'Makefile_t'

        make_file_template_path = os.path.join(paths.ROOT_DIR, make_file_template_basename)
        with open(make_file_template_path, 'r') as f:
            template = jinja2.Template(f.read())
        make_file_content = template.render(
            rsrcdir=source_dir,
            rbuilddir=build_dir,
            projname=project_name
        )

        make_file_basename = make_file_template_basename[:-2]  # remove the trailing _t
        make_file_path = os.path.join(tempfile.mkdtemp(), make_file_basename)
        with open(make_file_path, 'w') as f:
            f.write(make_file_content)

        self.make_file = make_file_path

    def __enter__(self):
        return self.make_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(os.path.dirname(self.make_file))
        return False


def main(project_name,
         docs_root_dir=None,
         code_source_dir_path=None,
         force_rebuild=True,
         autodoc_generate=True,
         autodoc_force_override=True):
    if not docs_root_dir:
        caller = inspect_ex.get_caller()
        docs_root_dir = find_docs_root_dir(caller.filename)

    if autodoc_generate:
        autodoc_output_dir_path = os.path.join(docs_root_dir, 'source', '_modules')
        code_source_dir_path = (
                code_source_dir_path or
                os.path.normpath(os.path.join(docs_root_dir, os.pardir, 'source', project_name))
        )

        # http://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html#envvar-SPHINX_APIDOC_OPTIONS
        os.environ['SPHINX_APIDOC_OPTIONS'] = 'no-members'
        if autodoc_force_override:
            utils.rmtree(autodoc_output_dir_path)

        # add -f flag to force overriding apidoc files
        utils.run_command('sphinx-apidoc --maxdepth 8 --separate -o {output} {source}'.format(
            output=autodoc_output_dir_path,
            source=code_source_dir_path,
        ))

    if force_rebuild:
        utils.rmtree(os.path.join(docs_root_dir, 'build'))

    with prepare_make_file(
            project_name,
            source_dir=os.path.join(docs_root_dir, 'source'),
            build_dir=os.path.join(docs_root_dir, 'build')
    ) as make_file_path:
        utils.run_command('{make_file} html'.format(make_file=make_file_path))
