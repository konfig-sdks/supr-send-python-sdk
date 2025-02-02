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

from supr_send_python_sdk.type.template_get_details_response_channels import TemplateGetDetailsResponseChannels
from supr_send_python_sdk.type.template_get_details_response_default_language import TemplateGetDetailsResponseDefaultLanguage
from supr_send_python_sdk.type.template_get_details_response_enabled_languages import TemplateGetDetailsResponseEnabledLanguages
from supr_send_python_sdk.type.template_get_details_response_updated_by import TemplateGetDetailsResponseUpdatedBy

class RequiredTemplateGetDetailsResponse(TypedDict):
    pass

class OptionalTemplateGetDetailsResponse(TypedDict, total=False):
    description: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    id: int

    name: str

    slug: str

    is_active: bool

    default_language: TemplateGetDetailsResponseDefaultLanguage

    created_at: str

    updated_at: str

    updated_by: TemplateGetDetailsResponseUpdatedBy

    last_triggered_at: str

    is_auto_translate_enabled: bool

    enabled_languages: TemplateGetDetailsResponseEnabledLanguages

    channels: TemplateGetDetailsResponseChannels

class TemplateGetDetailsResponse(RequiredTemplateGetDetailsResponse, OptionalTemplateGetDetailsResponse):
    pass
