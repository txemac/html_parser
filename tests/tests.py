import unittest
import os

from html_parser import html_parser


__author__ = 'josebermudez'


class ParserTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(ParserTest, self).__init__(*args, **kwargs)
        self.fixture_path = os.path.join(os.path.dirname(__file__), "../", "fixtures")

    def test_html_string_none(self):
        self.assertRaises(ValueError, html_parser, html_string=None)

    def test_fixture_1(self):
        fixture1 = open(os.path.join(self.fixture_path, 'fixture1.html')).read()
        address, suite, postcode, description, images = html_parser(html_string=fixture1)

        expected_address = "Crown House, Toutley Road, Wokingham, Berkshire"
        expected_images = [
            'http://media.clarkscomputers.co.uk/images/PHBRA/208042_1_003.jpg',
            'http://media.clarkscomputers.co.uk/images/PHBRA/208042_1_004.jpg'
        ]
        self.assertEquals(address, expected_address)
        self.assertEquals(postcode, "RG41 1QW")
        self.assertEquals(suite, "Suite 2")
        self.assertEqual(description, "This is some test description 1")
        self.assertEqual(images, expected_images)

    def test_fixture_2(self):
        fixture2 = open(os.path.join(self.fixture_path, 'fixture2.html')).read()
        address, suite, postcode, description, images = html_parser(html_string=fixture2)

        expected_address = "329 bracknell, Doncastle Road, Bracknell, Berkshire"
        expected_images = [
            'http://media.clarkscomputers.co.uk/images/PHBRA/217018_1_001.jpg',
            'http://media.clarkscomputers.co.uk/images/PHBRA/217018_1_000.jpg',
            'http://media.clarkscomputers.co.uk/images/PHBRA/217018_1_002.jpg',
            'http://media.clarkscomputers.co.uk/images/PHBRA/217018_1_003.jpg'
        ]
        self.assertEquals(address, expected_address)
        self.assertEquals(postcode, None)
        self.assertEquals(suite, None)
        self.assertEqual(description, "Description part 1. Desc part 2.")
        self.assertEqual(images, expected_images)
