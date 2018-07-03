"""Add custom filters to Jinja processor.

The original purpose of this module was to be able to put links to general index and
module index into sidebar, using manual URL composition with custom Jinja filters.
"""
import os
import posixpath

from sphinx.jinja2glue import BuiltinTemplateLoader

_template_filters = []


def template_filter(func):
    _template_filters.append(func)
    return func


@template_filter
def dirname(path):
    return os.path.dirname(path)


@template_filter
def join_with(path, path2):
    return posixpath.join(path, path2)


class TemplateLoader(BuiltinTemplateLoader):
    def init(self, builder, theme=None, dirs=None):
        super(TemplateLoader, self).init(builder, theme, dirs)
        for template_filter in _template_filters:
            self.environment.filters[template_filter.__name__] = template_filter
