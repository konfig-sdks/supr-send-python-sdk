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


class TemplateGetContentChannelResponseVersionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
        
            @staticmethod
            def templates() -> typing.Type['TemplateGetContentChannelResponseVersionsItemTemplates']:
                return TemplateGetContentChannelResponseVersionsItemTemplates
            status = schemas.StrSchema
            version_tag = schemas.StrSchema
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
        
            @staticmethod
            def updated_by() -> typing.Type['TemplateGetContentChannelResponseVersionsItemUpdatedBy']:
                return TemplateGetContentChannelResponseVersionsItemUpdatedBy
            version_tag_user = schemas.StrSchema
        
            @staticmethod
            def published_languages() -> typing.Type['TemplateGetContentChannelResponseVersionsItemPublishedLanguages']:
                return TemplateGetContentChannelResponseVersionsItemPublishedLanguages
        
            @staticmethod
            def apparent_published_languages() -> typing.Type['TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages']:
                return TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages
            __annotations__ = {
                "id": id,
                "templates": templates,
                "status": status,
                "version_tag": version_tag,
                "created_at": created_at,
                "updated_at": updated_at,
                "updated_by": updated_by,
                "version_tag_user": version_tag_user,
                "published_languages": published_languages,
                "apparent_published_languages": apparent_published_languages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templates"]) -> 'TemplateGetContentChannelResponseVersionsItemTemplates': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_tag"]) -> MetaOapg.properties.version_tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_by"]) -> 'TemplateGetContentChannelResponseVersionsItemUpdatedBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_tag_user"]) -> MetaOapg.properties.version_tag_user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_languages"]) -> 'TemplateGetContentChannelResponseVersionsItemPublishedLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apparent_published_languages"]) -> 'TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "templates", "status", "version_tag", "created_at", "updated_at", "updated_by", "version_tag_user", "published_languages", "apparent_published_languages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templates"]) -> typing.Union['TemplateGetContentChannelResponseVersionsItemTemplates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_tag"]) -> typing.Union[MetaOapg.properties.version_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_by"]) -> typing.Union['TemplateGetContentChannelResponseVersionsItemUpdatedBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_tag_user"]) -> typing.Union[MetaOapg.properties.version_tag_user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_languages"]) -> typing.Union['TemplateGetContentChannelResponseVersionsItemPublishedLanguages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apparent_published_languages"]) -> typing.Union['TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "templates", "status", "version_tag", "created_at", "updated_at", "updated_by", "version_tag_user", "published_languages", "apparent_published_languages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        templates: typing.Union['TemplateGetContentChannelResponseVersionsItemTemplates', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        version_tag: typing.Union[MetaOapg.properties.version_tag, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        updated_by: typing.Union['TemplateGetContentChannelResponseVersionsItemUpdatedBy', schemas.Unset] = schemas.unset,
        version_tag_user: typing.Union[MetaOapg.properties.version_tag_user, str, schemas.Unset] = schemas.unset,
        published_languages: typing.Union['TemplateGetContentChannelResponseVersionsItemPublishedLanguages', schemas.Unset] = schemas.unset,
        apparent_published_languages: typing.Union['TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateGetContentChannelResponseVersionsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            templates=templates,
            status=status,
            version_tag=version_tag,
            created_at=created_at,
            updated_at=updated_at,
            updated_by=updated_by,
            version_tag_user=version_tag_user,
            published_languages=published_languages,
            apparent_published_languages=apparent_published_languages,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.template_get_content_channel_response_versions_item_apparent_published_languages import TemplateGetContentChannelResponseVersionsItemApparentPublishedLanguages
from supr_send_python_sdk.model.template_get_content_channel_response_versions_item_published_languages import TemplateGetContentChannelResponseVersionsItemPublishedLanguages
from supr_send_python_sdk.model.template_get_content_channel_response_versions_item_templates import TemplateGetContentChannelResponseVersionsItemTemplates
from supr_send_python_sdk.model.template_get_content_channel_response_versions_item_updated_by import TemplateGetContentChannelResponseVersionsItemUpdatedBy
