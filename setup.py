# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in it_management/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('it_management/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.read().strip().split('\n') if line.strip() and not line.startswith('#')]

setup(
    name='it_management',
    version=version,
    description='Management von IT-Bausteinen. Hierzu gehören IT-Geräte und IT-Lösungen wie Server, Rechner, Netzwerke und E-Mailserver sowie auch Backups, Dienstleistungsverträge, Accounts und Internetleistungen.',
    author='TUEIT',
    author_email='info@tueit.de',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)