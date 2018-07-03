from setuptools import setup, find_packages
import os

packages = find_packages(os.path.join('.', 'source'))
package_dir = {}
for package in packages:
    package_path = os.path.join(*package.split('.'))
    package_dir[package] = os.path.join('source', package_path)

setup(
    name='sphinx_theme',
    version='0.0.1',
    packages=packages,
    package_dir=package_dir,
    include_package_data=True,
    install_requires=[
        'sphinx',
        'jinja2',
    ]
)
