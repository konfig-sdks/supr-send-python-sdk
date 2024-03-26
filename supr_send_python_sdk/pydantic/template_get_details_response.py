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

from supr_send_python_sdk.pydantic.template_get_details_response_channels import TemplateGetDetailsResponseChannels
from supr_send_python_sdk.pydantic.template_get_details_response_default_language import TemplateGetDetailsResponseDefaultLanguage
from supr_send_python_sdk.pydantic.template_get_details_response_enabled_languages import TemplateGetDetailsResponseEnabledLanguages
from supr_send_python_sdk.pydantic.template_get_details_response_updated_by import TemplateGetDetailsResponseUpdatedBy

class TemplateGetDetailsResponse(BaseModel):
    description: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='description')

    id: typing.Optional[int] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    slug: typing.Optional[str] = Field(None, alias='slug')

    is_active: typing.Optional[bool] = Field(None, alias='is_active')

    default_language: typing.Optional[TemplateGetDetailsResponseDefaultLanguage] = Field(None, alias='default_language')

    created_at: typing.Optional[str] = Field(None, alias='created_at')

    updated_at: typing.Optional[str] = Field(None, alias='updated_at')

    updated_by: typing.Optional[TemplateGetDetailsResponseUpdatedBy] = Field(None, alias='updated_by')

    last_triggered_at: typing.Optional[str] = Field(None, alias='last_triggered_at')

    is_auto_translate_enabled: typing.Optional[bool] = Field(None, alias='is_auto_translate_enabled')

    enabled_languages: typing.Optional[TemplateGetDetailsResponseEnabledLanguages] = Field(None, alias='enabled_languages')

    channels: typing.Optional[TemplateGetDetailsResponseChannels] = Field(None, alias='channels')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )