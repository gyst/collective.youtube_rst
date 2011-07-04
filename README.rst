Introduction
============

This is a tiny addon for Plone that enables embedding of Youtube videos
in ReStructuredText.


Installation
------------

Include the egg in your buildout::

| [buildout]
|    eggs += collective.youtube_rst


Manual setup
------------

You will need to allow IFRAME tags in your site.

* In your browser, goto /@@filter-controlpanel
* Under **Custom tags** hit the button 'Add Custom tags'
* in the new input field, enter: iframe
* Hit 'Save' or your changes will not take effect


Usage
-----

You can now embed a youtube video in rst using the 'youtube' directive::

    .. youtube:: foobar

Optionally you can override the default with (560px) and height (349px) settings::

    .. youtube:: foobar
        width=640
        height=390


Gotchas
-------

ReStructuredText to HTML conversion is (apparently) done save-time, not render-time.
If you're fiddling with the rst config, you may need to re-save any rst documents
for changes to show up.

Credits
-------

Based on http://countergram.com/youtube-in-rst
