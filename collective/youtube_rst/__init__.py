from youtube import youtube
from docutils.parsers.rst import directives


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    directives.register_directive('youtube', youtube)
