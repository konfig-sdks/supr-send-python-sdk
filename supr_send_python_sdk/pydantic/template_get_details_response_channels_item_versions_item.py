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

from supr_send_python_sdk.pydantic.template_get_details_response_channels_item_versions_item_apparent_published_languages import TemplateGetDetailsResponseChannelsItemVersionsItemApparentPublishedLanguages
from supr_send_python_sdk.pydantic.template_get_details_response_channels_item_versions_item_published_languages import TemplateGetDetailsResponseChannelsItemVersionsItemPublishedLanguages
from supr_send_python_sdk.pydantic.template_get_details_response_channels_item_versions_item_templates import TemplateGetDetailsResponseChannelsItemVersionsItemTemplates
from supr_send_python_sdk.pydantic.template_get_details_response_channels_item_versions_item_updated_by import TemplateGetDetailsResponseChannelsItemVersionsItemUpdatedBy

class TemplateGetDetailsResponseChannelsItemVersionsItem(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    templates: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemTemplates] = Field(None, alias='templates')

    status: typing.Optional[str] = Field(None, alias='status')

    version_tag: typing.Optional[str] = Field(None, alias='version_tag')

    created_at: typing.Optional[str] = Field(None, alias='created_at')

    updated_at: typing.Optional[str] = Field(None, alias='updated_at')

    updated_by: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemUpdatedBy] = Field(None, alias='updated_by')

    version_tag_user: typing.Optional[str] = Field(None, alias='version_tag_user')

    published_languages: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemPublishedLanguages] = Field(None, alias='published_languages')

    apparent_published_languages: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemApparentPublishedLanguages] = Field(None, alias='apparent_published_languages')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
