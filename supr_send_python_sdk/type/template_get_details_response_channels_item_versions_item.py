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

from supr_send_python_sdk.type.template_get_details_response_channels_item_versions_item_apparent_published_languages import TemplateGetDetailsResponseChannelsItemVersionsItemApparentPublishedLanguages
from supr_send_python_sdk.type.template_get_details_response_channels_item_versions_item_published_languages import TemplateGetDetailsResponseChannelsItemVersionsItemPublishedLanguages
from supr_send_python_sdk.type.template_get_details_response_channels_item_versions_item_templates import TemplateGetDetailsResponseChannelsItemVersionsItemTemplates
from supr_send_python_sdk.type.template_get_details_response_channels_item_versions_item_updated_by import TemplateGetDetailsResponseChannelsItemVersionsItemUpdatedBy

class RequiredTemplateGetDetailsResponseChannelsItemVersionsItem(TypedDict):
    pass

class OptionalTemplateGetDetailsResponseChannelsItemVersionsItem(TypedDict, total=False):
    id: int

    templates: TemplateGetDetailsResponseChannelsItemVersionsItemTemplates

    status: str

    version_tag: str

    created_at: str

    updated_at: str

    updated_by: TemplateGetDetailsResponseChannelsItemVersionsItemUpdatedBy

    version_tag_user: str

    published_languages: TemplateGetDetailsResponseChannelsItemVersionsItemPublishedLanguages

    apparent_published_languages: TemplateGetDetailsResponseChannelsItemVersionsItemApparentPublishedLanguages

class TemplateGetDetailsResponseChannelsItemVersionsItem(RequiredTemplateGetDetailsResponseChannelsItemVersionsItem, OptionalTemplateGetDetailsResponseChannelsItemVersionsItem):
    pass
