from pkg_resources import parse_version
from configparser import ConfigParser
import setuptools,re,sys
assert parse_version(setuptools.__version__)>=parse_version('36.2')

statuses = [ '1 - Planning', '2 - Pre-Alpha', '3 - Alpha',
    '4 - Beta', '5 - Production/Stable', '6 - Mature', '7 - Inactive' ]
py_versions = '2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7 3.8 3.9 3.10 3.11 3.12 3.13'.split()
min_python = '3.8'
lic = ('Apache Software License 2.0','OSI Approved :: Apache Software License')

requirements = ['pip', 'packaging']

long_description = open('README.md', encoding="utf8").read()

setuptools.setup(
    name = 'nbclassic-collapsible-headings',
    version = '0.0.5',
    description = 'Allows notebook to have collapsible sections, separated by headings',
    keywords = 'notebook',
    author = 'Nbextensions team',
    author_email = 'info@fast.ai',
    license = lic[0],
    classifiers = [
        'Development Status :: ' + statuses[3],
        'Intended Audience :: ' + 'Developers',
        'License :: ' + lic[1],
        'Natural Language :: ' + 'English',
    ] + ['Programming Language :: Python :: '+o for o in py_versions[py_versions.index(min_python):]],
    url = 'https://github.com/AnswerDotAI/nbclassic-collapsible-headings',
    include_package_data = True,
    data_files=[
        ("share/jupyter/nbextensions", [ "static/collapsible_headings.js", ]),
        ("share/jupyter/nbextensions", [ "static/collapsible_headings.css", ]),
        ("etc/jupyter/nbconfig/notebook.d", [ "jupyter-config/collapsible_headings.json" ])
    ],
    install_requires = requirements,
    python_requires  = '>=3.8',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    zip_safe = False)

