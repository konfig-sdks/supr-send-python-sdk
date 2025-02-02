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

from supr_send_python_sdk.type.preference_update_channel_preferences_request_channel_preferences import PreferenceUpdateChannelPreferencesRequestChannelPreferences

class RequiredPreferenceUpdateChannelPreferencesRequest(TypedDict):
    pass

class OptionalPreferenceUpdateChannelPreferencesRequest(TypedDict, total=False):
    channel_preferences: PreferenceUpdateChannelPreferencesRequestChannelPreferences

class PreferenceUpdateChannelPreferencesRequest(RequiredPreferenceUpdateChannelPreferencesRequest, OptionalPreferenceUpdateChannelPreferencesRequest):
    pass
