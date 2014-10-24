# coding: utf-8

from xml.dom import minidom


class WechatParser(object):
    """ Message Parser

        Using:
            >>> string = '<xml><name>John</name></xml>'
            >>> parsed_string = WechatParser(string)
            >>> name = parsed_string.name
            John

    """
    def __init__(self, string):
        """ Initialization parse string.
        """

        self._content = minidom.parseString(string)

    def __getattr__(self, tag):

        return self._get_tag_content(tag)

    def _get_tag_content(self, tag):

        try:
            content = self._content.getElementsByTagName(tag)[0].firstChild.wholeText
        except IndexError:
            content = None

        return content
