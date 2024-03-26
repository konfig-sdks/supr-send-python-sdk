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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class PreferenceUpdateChannelPreferencesRequestChannelPreferencesItem(BaseModel):
    # Add channel as `email`, `inbox`, `sms`, `whatsapp`, `androidpush`, `slack`, `iospush`, `webpush`
    channel: typing.Optional[str] = Field(None, alias='channel')

    # set `is_restricted = true` if user wants to receive notification in mandatory categories on this channel. Mandatory categories are `can't unsubscribe` categories and the above channel is added as `mandatory channel` in that category
    is_restricted: typing.Optional[bool] = Field(None, alias='is_restricted')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )