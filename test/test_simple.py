# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from supr_send_python_sdk import SuprSend

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        suprsend = SuprSend(
        
                        sec0 = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(suprsend)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()