#!/usr/bin/env python
# coding: utf-8


import unittest
from wemsg.parser import WechatParser

class TestWeMsgParse(unittest.TestCase):

    def setUp(self):
        string = '<xml><name>John</name></xml>'
        self.parsed_string = WechatParser(string)

    def test_success_parse(self):

        self.assertEqual(self.parsed_string.name, 'John')

    def test_fail_parse(self):
        self.assertEqual(self.parsed_string.age, None)


if __name__ == '__main__':
    unittest.main()
