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


class EventTriggerEventRequestuserOperationsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            append = schemas.DictSchema
            remove = schemas.DictSchema
            set = schemas.DictSchema
        
            @staticmethod
            def unset() -> typing.Type['EventTriggerEventRequestuserOperationsItemunset']:
                return EventTriggerEventRequestuserOperationsItemunset
            __annotations__ = {
                "$append": append,
                "$remove": remove,
                "$set": set,
                "$unset": unset,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$append"]) -> MetaOapg.properties.append: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$remove"]) -> MetaOapg.properties.remove: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$set"]) -> MetaOapg.properties.set: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$unset"]) -> 'EventTriggerEventRequestuserOperationsItemunset': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["$append", "$remove", "$set", "$unset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$append"]) -> typing.Union[MetaOapg.properties.append, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$remove"]) -> typing.Union[MetaOapg.properties.remove, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$set"]) -> typing.Union[MetaOapg.properties.set, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$unset"]) -> typing.Union['EventTriggerEventRequestuserOperationsItemunset', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["$append", "$remove", "$set", "$unset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EventTriggerEventRequestuserOperationsItem':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.event_trigger_event_requestuser_operations_itemunset import EventTriggerEventRequestuserOperationsItemunset
