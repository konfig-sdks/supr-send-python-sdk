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


class TemplateGetDetailsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.AnyTypeSchema
            id = schemas.IntSchema
            name = schemas.StrSchema
            slug = schemas.StrSchema
            is_active = schemas.BoolSchema
        
            @staticmethod
            def default_language() -> typing.Type['TemplateGetDetailsResponseDefaultLanguage']:
                return TemplateGetDetailsResponseDefaultLanguage
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
        
            @staticmethod
            def updated_by() -> typing.Type['TemplateGetDetailsResponseUpdatedBy']:
                return TemplateGetDetailsResponseUpdatedBy
            last_triggered_at = schemas.StrSchema
            is_auto_translate_enabled = schemas.BoolSchema
        
            @staticmethod
            def enabled_languages() -> typing.Type['TemplateGetDetailsResponseEnabledLanguages']:
                return TemplateGetDetailsResponseEnabledLanguages
        
            @staticmethod
            def channels() -> typing.Type['TemplateGetDetailsResponseChannels']:
                return TemplateGetDetailsResponseChannels
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "slug": slug,
                "is_active": is_active,
                "default_language": default_language,
                "created_at": created_at,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "last_triggered_at": last_triggered_at,
                "is_auto_translate_enabled": is_auto_translate_enabled,
                "enabled_languages": enabled_languages,
                "channels": channels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slug"]) -> MetaOapg.properties.slug: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_language"]) -> 'TemplateGetDetailsResponseDefaultLanguage': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_by"]) -> 'TemplateGetDetailsResponseUpdatedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_triggered_at"]) -> MetaOapg.properties.last_triggered_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_auto_translate_enabled"]) -> MetaOapg.properties.is_auto_translate_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled_languages"]) -> 'TemplateGetDetailsResponseEnabledLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channels"]) -> 'TemplateGetDetailsResponseChannels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "slug", "is_active", "default_language", "created_at", "updated_at", "updated_by", "last_triggered_at", "is_auto_translate_enabled", "enabled_languages", "channels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slug"]) -> typing.Union[MetaOapg.properties.slug, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_language"]) -> typing.Union['TemplateGetDetailsResponseDefaultLanguage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_by"]) -> typing.Union['TemplateGetDetailsResponseUpdatedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_triggered_at"]) -> typing.Union[MetaOapg.properties.last_triggered_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_auto_translate_enabled"]) -> typing.Union[MetaOapg.properties.is_auto_translate_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled_languages"]) -> typing.Union['TemplateGetDetailsResponseEnabledLanguages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channels"]) -> typing.Union['TemplateGetDetailsResponseChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "slug", "is_active", "default_language", "created_at", "updated_at", "updated_by", "last_triggered_at", "is_auto_translate_enabled", "enabled_languages", "channels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        slug: typing.Union[MetaOapg.properties.slug, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        default_language: typing.Union['TemplateGetDetailsResponseDefaultLanguage', schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        updated_by: typing.Union['TemplateGetDetailsResponseUpdatedBy', schemas.Unset] = schemas.unset,
        last_triggered_at: typing.Union[MetaOapg.properties.last_triggered_at, str, schemas.Unset] = schemas.unset,
        is_auto_translate_enabled: typing.Union[MetaOapg.properties.is_auto_translate_enabled, bool, schemas.Unset] = schemas.unset,
        enabled_languages: typing.Union['TemplateGetDetailsResponseEnabledLanguages', schemas.Unset] = schemas.unset,
        channels: typing.Union['TemplateGetDetailsResponseChannels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateGetDetailsResponse':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            name=name,
            slug=slug,
            is_active=is_active,
            default_language=default_language,
            created_at=created_at,
            updated_at=updated_at,
            updated_by=updated_by,
            last_triggered_at=last_triggered_at,
            is_auto_translate_enabled=is_auto_translate_enabled,
            enabled_languages=enabled_languages,
            channels=channels,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.template_get_details_response_channels import TemplateGetDetailsResponseChannels
from supr_send_python_sdk.model.template_get_details_response_default_language import TemplateGetDetailsResponseDefaultLanguage
from supr_send_python_sdk.model.template_get_details_response_enabled_languages import TemplateGetDetailsResponseEnabledLanguages
from supr_send_python_sdk.model.template_get_details_response_updated_by import TemplateGetDetailsResponseUpdatedBy
