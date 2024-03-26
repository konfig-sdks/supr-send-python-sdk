# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from supr_send_python_sdk.type.subscriber_add_to_draft_list_request_distinct_ids import SubscriberAddToDraftListRequestDistinctIds

class RequiredSubscriberAddToDraftListRequest(TypedDict):
    pass

class OptionalSubscriberAddToDraftListRequest(TypedDict, total=False):
    distinct_ids: SubscriberAddToDraftListRequestDistinctIds

class SubscriberAddToDraftListRequest(RequiredSubscriberAddToDraftListRequest, OptionalSubscriberAddToDraftListRequest):
    pass
