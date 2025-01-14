# coding: utf-8

# flake8: noqa

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

__version__ = "1.2.1"

# import ApiClient
from supr_send_python_sdk.api_client import ApiClient

# import Configuration
from supr_send_python_sdk.configuration import Configuration

# import exceptions
from supr_send_python_sdk.exceptions import OpenApiException
from supr_send_python_sdk.exceptions import ApiAttributeError
from supr_send_python_sdk.exceptions import ApiTypeError
from supr_send_python_sdk.exceptions import ApiValueError
from supr_send_python_sdk.exceptions import ApiKeyError
from supr_send_python_sdk.exceptions import ApiException

from supr_send_python_sdk.client import SuprSend
