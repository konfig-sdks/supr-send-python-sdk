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

from supr_send_python_sdk.type.template_get_details_response_channels_item_versions_item_templates_item_content_example import TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample

RequiredTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent = TypedDict("RequiredTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent", {
    })

OptionalTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent = TypedDict("OptionalTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent", {
    "text": str,

    "header": str,

    "example": TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample,

    "vendor_slug": str,

    "content_type": str,

    "message_type": str,

    "template_name": str,

    "enterprise_name": str,

    "handlebars_text": str,

    "vendor_template_id": str,

    "x-konfig-original-example": TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContentExample,
    }, total=False)

class TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent(RequiredTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent, OptionalTemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemContent):
    pass
