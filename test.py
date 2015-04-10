#!/usr/bin/env python

"""Tests for the Flask Heroku template."""

import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page_works(self):
        request = self.app.get('/')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)

    def test_404_page(self):
        request = self.app.get('/i-am-not-found/')
        self.assertEqual(request.status_code, 404)

    def test_static_text_file_request(self):
        request = self.app.get('/robots.txt')
        self.assertTrue(request.data)
        self.assertEqual(request.status_code, 200)
        request.close()


if __name__ == '__main__':
    unittest.main()
