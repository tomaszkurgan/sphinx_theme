"""Monkeypatch for Sphinx to get rid of annoying '= None' next to the instance
attribute documentation.
"""

from sphinx.ext.autodoc import ClassLevelDocumenter, InstanceAttributeDocumenter


def add_directive_header(self, sig):
    ClassLevelDocumenter.add_directive_header(self, sig)


InstanceAttributeDocumenter.add_directive_header = add_directive_header
