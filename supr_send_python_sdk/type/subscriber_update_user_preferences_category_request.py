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

from supr_send_python_sdk.type.subscriber_update_user_preferences_category_request_opt_out_channels import SubscriberUpdateUserPreferencesCategoryRequestOptOutChannels

class RequiredSubscriberUpdateUserPreferencesCategoryRequest(TypedDict):
    pass

class OptionalSubscriberUpdateUserPreferencesCategoryRequest(TypedDict, total=False):
    # choose one of the options: `opt_in` if the user has allowed notification in this category and `opt_out` if user wants to discontinue notification in this category
    preference: str

    opt_out_channels: SubscriberUpdateUserPreferencesCategoryRequestOptOutChannels

class SubscriberUpdateUserPreferencesCategoryRequest(RequiredSubscriberUpdateUserPreferencesCategoryRequest, OptionalSubscriberUpdateUserPreferencesCategoryRequest):
    pass
