# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup

version = 0.9

LONG_DESCRIPTION = """
Markdown extensions for basic syntax flavoring: automatically
convert line breaks to <br>, convert urls to links. Works with
Markdown>=2.0 http://www.freewisdom.org/projects/python-markdown
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(name='mdxflavours',
      version=version,
      author='Alexey Kinyov',
      author_email='rudy@05bit.com',
      description='Markdown extensions for basic syntax flavoring.',
      license='BSD',
      keywords='markdown, extensions',
      url='https://github.com/05bit/python-mdxflavours',
      packages=['mdxflavours',],
      long_description=long_description(),
      install_requires=['Markdown>=2.0',],
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: OS Independent',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Text Processing :: Filters',
                   'Topic :: Text Processing :: Markup :: HTML'])
