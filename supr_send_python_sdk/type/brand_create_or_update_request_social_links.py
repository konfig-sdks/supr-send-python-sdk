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


class RequiredBrandCreateOrUpdateRequestSocialLinks(TypedDict):
    pass

class OptionalBrandCreateOrUpdateRequestSocialLinks(TypedDict, total=False):
    # link of brand website. While updating a social link, if you want to remove the link, you must the value=\"\" (instead of null)
    website: str

    # brand facebook page link
    facebook: str

    # brand linkedin page link
    linkedin: str

    # brand twitter page link
    twitter: str

    # brand instagram page link
    instagram: str

    # brand medium page link
    medium: str

    # brand discord page link
    discord: str

    # brand telegram page link
    telegram: str

    # brand youtube page link
    youtube: str

class BrandCreateOrUpdateRequestSocialLinks(RequiredBrandCreateOrUpdateRequestSocialLinks, OptionalBrandCreateOrUpdateRequestSocialLinks):
    pass
