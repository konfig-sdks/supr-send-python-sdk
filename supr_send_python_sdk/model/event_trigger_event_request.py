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


class EventTriggerEventRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "distinct_id",
            "event",
        }
        
        class properties:
            distinct_id = schemas.StrSchema
            event = schemas.StrSchema
        
            @staticmethod
            def user_operations() -> typing.Type['EventTriggerEventRequestuserOperations']:
                return EventTriggerEventRequestuserOperations
            properties = schemas.StrSchema
            brand_id = schemas.StrSchema
            idempotency_key = schemas.StrSchema
            __annotations__ = {
                "distinct_id": distinct_id,
                "event": event,
                "$user_operations": user_operations,
                "properties": properties,
                "brand_id": brand_id,
                "$idempotency_key": idempotency_key,
            }
    
    distinct_id: MetaOapg.properties.distinct_id
    event: MetaOapg.properties.event
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distinct_id"]) -> MetaOapg.properties.distinct_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$user_operations"]) -> 'EventTriggerEventRequestuserOperations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["properties"]) -> MetaOapg.properties.properties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand_id"]) -> MetaOapg.properties.brand_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$idempotency_key"]) -> MetaOapg.properties.idempotency_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["distinct_id", "event", "$user_operations", "properties", "brand_id", "$idempotency_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distinct_id"]) -> MetaOapg.properties.distinct_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> MetaOapg.properties.event: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$user_operations"]) -> typing.Union['EventTriggerEventRequestuserOperations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["properties"]) -> typing.Union[MetaOapg.properties.properties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand_id"]) -> typing.Union[MetaOapg.properties.brand_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$idempotency_key"]) -> typing.Union[MetaOapg.properties.idempotency_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["distinct_id", "event", "$user_operations", "properties", "brand_id", "$idempotency_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        distinct_id: typing.Union[MetaOapg.properties.distinct_id, str, ],
        event: typing.Union[MetaOapg.properties.event, str, ],
        properties: typing.Union[MetaOapg.properties.properties, str, schemas.Unset] = schemas.unset,
        brand_id: typing.Union[MetaOapg.properties.brand_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventTriggerEventRequest':
        return super().__new__(
            cls,
            *args,
            distinct_id=distinct_id,
            event=event,
            properties=properties,
            brand_id=brand_id,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.event_trigger_event_requestuser_operations import EventTriggerEventRequestuserOperations