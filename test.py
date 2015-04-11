#!/usr/bin/env python

"""Tests for the Flask Heroku template."""

import unittest
from app import app


class TestApp(unittest.TestCase):
    """ Test the index """


    def setUp(self):
        self.app = app.test_client()


    def test_home_page_works(self):
        """ Test the index """
        request = self.app.get('/')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()


    def test_404_page(self):
        """ Test 404 """
        request = self.app.get('/i-am-not-found/')
        self.assertEqual(request.status_code, 404)
        request.close()


    def test_static_text_file_request(self):
        """ Test robots.txt """
        request = self.app.get('/robots.txt')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()


    def test_image_request(self):
        """ Test images """
        request = self.app.get('/images/dod.png')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()


    def test_font_request(self):
        """ Test fonts """
        request = self.app.get('/fonts/fontawesome-webfont.svg')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()

if __name__ == '__main__':
    unittest.main()
