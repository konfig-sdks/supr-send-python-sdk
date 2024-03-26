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

from supr_send_python_sdk.pydantic.template_get_details_response_channels_item_versions_item_templates_item_content_example import TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample

class TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent(BaseModel):
    text: typing.Optional[str] = Field(None, alias='text')

    header: typing.Optional[str] = Field(None, alias='header')

    example: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample] = Field(None, alias='example')

    vendor_slug: typing.Optional[str] = Field(None, alias='vendor_slug')

    content_type: typing.Optional[str] = Field(None, alias='content_type')

    message_type: typing.Optional[str] = Field(None, alias='message_type')

    template_name: typing.Optional[str] = Field(None, alias='template_name')

    enterprise_name: typing.Optional[str] = Field(None, alias='enterprise_name')

    handlebars_text: typing.Optional[str] = Field(None, alias='handlebars_text')

    vendor_template_id: typing.Optional[str] = Field(None, alias='vendor_template_id')

    x-konfig-original-example_: typing.Optional[TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample] = Field(None, alias='x-konfig-original-example')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )