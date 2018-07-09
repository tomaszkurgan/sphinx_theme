from setuptools import setup, find_packages
import os

source_dir = 'source'

packages = find_packages(os.path.join('.', source_dir))
package_dir = {
    '': source_dir,
}

install_requires = [
    'sphinx',
    'jinja2',
]
dependency_links = []

READTHEDOCS_PROJECT = os.environ.get('READTHEDOCS_PROJECT')
if not READTHEDOCS_PROJECT or READTHEDOCS_PROJECT != 'slex':
    install_requires.append('slex<=999')
    dependency_links.append('https://github.com/tomaszkurgan/slex/archive/master.zip#egg=slex-999')

setup(
    name='sphinx_theme',
    version='0.0.1',
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
)
