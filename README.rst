============
Installation
============

Get source from GitHub_::

	$ git clone git://github.com/05bit/python-mdxflavours.git

and add mdxflavours to PYTHONPATH::

    $ export PYTHONPATH=$PYTHONPATH:$(pwd)/mdxflavours/

or::

    $ cd mdxflavours
    $ python setup.py install

Note: importing package ``mdxflavours`` automatically adds required
path to system paths.

=====
Usage
=====

Example for auto line breaks::

	>>> import markdown
	>>> markdown.markdown(u'And may the force  \nbe with you!') # no extension
	>>> u'<p>And may the force<br />\nbe with you!</p>'
	>>> markdown.markdown(u'And may the force\nbe with you!', extensions=['autobr'])
	>>> u'<p>And may the force<br />\nbe with you!</p>'

====================
Available extensions
====================

At the moment 2 extensions available:

	1. autobr
	2. autolink