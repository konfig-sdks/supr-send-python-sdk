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

from supr_send_python_sdk.pydantic.brand_create_or_update_request_social_links import BrandCreateOrUpdateRequestSocialLinks

class BrandCreateOrUpdateRequest(BaseModel):
    # Name of the brand. You can add company / organization name here
    brand_name: str = Field(alias='brand_name')

    # URL of the brand logo
    logo: typing.Optional[str] = Field(None, alias='logo')

    # Primary color of the brand - used for designing brand template. If you don't provide any of the colors for the brand, SuprSend will assume you want to use the default values, so color settings will automatically be set to the color settings of default brand.
    primary_color: typing.Optional[str] = Field(None, alias='primary_color')

    # Secondary color of the brand - not used for designing the default templates. You can however add this property and use it in your templates
    secondary_color: typing.Optional[str] = Field(None, alias='secondary_color')

    # Tertiary color of the brand - not used for designing the default templates. You can however add this property and use it in your templates
    tertiary_color: typing.Optional[str] = Field(None, alias='tertiary_color')

    # Link of the hosted preference page inside the brand product
    preference_page_url: typing.Optional[str] = Field(None, alias='preference_page_url')

    social_links: typing.Optional[BrandCreateOrUpdateRequestSocialLinks] = Field(None, alias='social_links')

    # Custom properties associated with the brand. Example value - `{\"k1\": \"v1\", \"k2\": 1.0}` <br> Update operation on properties works like upsert on 1st-level keys (i.e. if top-level key doesn't already exist, then it will be added, otherwise its value will be replaced by the new value. All other key-value pairs will remain unchanged).
    properties: typing.Optional[str] = Field(None, alias='properties')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
