# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import supr_send_python_sdk
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_version_version_id_subscriber_remove import post
from supr_send_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1SubscriberListListIdVersionVersionIdSubscriberRemove(ApiTestMixin, unittest.TestCase):
    """
    V1SubscriberListListIdVersionVersionIdSubscriberRemove unit test stubs
        Remove Subscribers from Draft List
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
