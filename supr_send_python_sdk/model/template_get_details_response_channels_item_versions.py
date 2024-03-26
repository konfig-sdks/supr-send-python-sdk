# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from supr_send_python_sdk import schemas  # noqa: F401


class TemplateGetDetailsResponseChannelsItemVersions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TemplateGetDetailsResponseChannelsItemVersionsItem']:
            return TemplateGetDetailsResponseChannelsItemVersionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TemplateGetDetailsResponseChannelsItemVersionsItem'], typing.List['TemplateGetDetailsResponseChannelsItemVersionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TemplateGetDetailsResponseChannelsItemVersions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TemplateGetDetailsResponseChannelsItemVersionsItem':
        return super().__getitem__(i)

from supr_send_python_sdk.model.template_get_details_response_channels_item_versions_item import TemplateGetDetailsResponseChannelsItemVersionsItem
