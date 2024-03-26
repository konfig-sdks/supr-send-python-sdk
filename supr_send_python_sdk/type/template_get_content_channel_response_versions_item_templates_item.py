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

from supr_send_python_sdk.type.template_get_content_channel_response_versions_item_templates_item_content import TemplateGetContentChannelResponseVersionsItemTemplatesItemContent
from supr_send_python_sdk.type.template_get_content_channel_response_versions_item_templates_item_language import TemplateGetContentChannelResponseVersionsItemTemplatesItemLanguage
from supr_send_python_sdk.type.template_get_content_channel_response_versions_item_templates_item_updated_by import TemplateGetContentChannelResponseVersionsItemTemplatesItemUpdatedBy

class RequiredTemplateGetContentChannelResponseVersionsItemTemplatesItem(TypedDict):
    pass

class OptionalTemplateGetContentChannelResponseVersionsItemTemplatesItem(TypedDict, total=False):
    id: int

    language: TemplateGetContentChannelResponseVersionsItemTemplatesItemLanguage

    is_enabled: bool

    approval_status: str

    content: TemplateGetContentChannelResponseVersionsItemTemplatesItemContent

    created_at: str

    updated_at: str

    updated_by: TemplateGetContentChannelResponseVersionsItemTemplatesItemUpdatedBy

    approval_cycle: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    is_approval_needed: bool

    is_cloned_from_last_version: bool

class TemplateGetContentChannelResponseVersionsItemTemplatesItem(RequiredTemplateGetContentChannelResponseVersionsItemTemplatesItem, OptionalTemplateGetContentChannelResponseVersionsItemTemplatesItem):
    pass
