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


class TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemApprovalCycle(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            status = schemas.StrSchema
            comment = schemas.AnyTypeSchema
            request_received_at = schemas.StrSchema
            sent_for_approval_at = schemas.AnyTypeSchema
            approval_status_received_at = schemas.StrSchema
            __annotations__ = {
                "status": status,
                "comment": comment,
                "request_received_at": request_received_at,
                "sent_for_approval_at": sent_for_approval_at,
                "approval_status_received_at": approval_status_received_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_received_at"]) -> MetaOapg.properties.request_received_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sent_for_approval_at"]) -> MetaOapg.properties.sent_for_approval_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval_status_received_at"]) -> MetaOapg.properties.approval_status_received_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "comment", "request_received_at", "sent_for_approval_at", "approval_status_received_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_received_at"]) -> typing.Union[MetaOapg.properties.request_received_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sent_for_approval_at"]) -> typing.Union[MetaOapg.properties.sent_for_approval_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval_status_received_at"]) -> typing.Union[MetaOapg.properties.approval_status_received_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "comment", "request_received_at", "sent_for_approval_at", "approval_status_received_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        request_received_at: typing.Union[MetaOapg.properties.request_received_at, str, schemas.Unset] = schemas.unset,
        sent_for_approval_at: typing.Union[MetaOapg.properties.sent_for_approval_at, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        approval_status_received_at: typing.Union[MetaOapg.properties.approval_status_received_at, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateGetDetailsResponseChannelsItemVersionsItemTemplatesItemApprovalCycle':
        return super().__new__(
            cls,
            *args,
            status=status,
            comment=comment,
            request_received_at=request_received_at,
            sent_for_approval_at=sent_for_approval_at,
            approval_status_received_at=approval_status_received_at,
            _configuration=_configuration,
            **kwargs,
        )
