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


class WorkflowConfigureTriggerRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "template",
            "notification_category",
            "name",
            "users",
        }
        
        class properties:
            name = schemas.StrSchema
            template = schemas.StrSchema
            notification_category = schemas.StrSchema
        
            @staticmethod
            def users() -> typing.Type['WorkflowConfigureTriggerRequestUsers']:
                return WorkflowConfigureTriggerRequestUsers
            data = schemas.StrSchema
        
            @staticmethod
            def delivery() -> typing.Type['WorkflowConfigureTriggerRequestDelivery']:
                return WorkflowConfigureTriggerRequestDelivery
            delay = schemas.StrSchema
            trigger_at = schemas.DateSchema
            brand_id = schemas.StrSchema
            idempotency_key = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "template": template,
                "notification_category": notification_category,
                "users": users,
                "data": data,
                "delivery": delivery,
                "delay": delay,
                "trigger_at": trigger_at,
                "brand_id": brand_id,
                "$idempotency_key": idempotency_key,
            }
    
    template: MetaOapg.properties.template
    notification_category: MetaOapg.properties.notification_category
    name: MetaOapg.properties.name
    users: 'WorkflowConfigureTriggerRequestUsers'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notification_category"]) -> MetaOapg.properties.notification_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["users"]) -> 'WorkflowConfigureTriggerRequestUsers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery"]) -> 'WorkflowConfigureTriggerRequestDelivery': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delay"]) -> MetaOapg.properties.delay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trigger_at"]) -> MetaOapg.properties.trigger_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["brand_id"]) -> MetaOapg.properties.brand_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$idempotency_key"]) -> MetaOapg.properties.idempotency_key: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "template", "notification_category", "users", "data", "delivery", "delay", "trigger_at", "brand_id", "$idempotency_key", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notification_category"]) -> MetaOapg.properties.notification_category: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["users"]) -> 'WorkflowConfigureTriggerRequestUsers': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery"]) -> typing.Union['WorkflowConfigureTriggerRequestDelivery', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delay"]) -> typing.Union[MetaOapg.properties.delay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trigger_at"]) -> typing.Union[MetaOapg.properties.trigger_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["brand_id"]) -> typing.Union[MetaOapg.properties.brand_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["$idempotency_key"]) -> typing.Union[MetaOapg.properties.idempotency_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "template", "notification_category", "users", "data", "delivery", "delay", "trigger_at", "brand_id", "$idempotency_key", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        template: typing.Union[MetaOapg.properties.template, str, ],
        notification_category: typing.Union[MetaOapg.properties.notification_category, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        users: 'WorkflowConfigureTriggerRequestUsers',
        data: typing.Union[MetaOapg.properties.data, str, schemas.Unset] = schemas.unset,
        delivery: typing.Union['WorkflowConfigureTriggerRequestDelivery', schemas.Unset] = schemas.unset,
        delay: typing.Union[MetaOapg.properties.delay, str, schemas.Unset] = schemas.unset,
        trigger_at: typing.Union[MetaOapg.properties.trigger_at, str, date, schemas.Unset] = schemas.unset,
        brand_id: typing.Union[MetaOapg.properties.brand_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowConfigureTriggerRequest':
        return super().__new__(
            cls,
            *args,
            template=template,
            notification_category=notification_category,
            name=name,
            users=users,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.workflow_configure_trigger_request_delivery import WorkflowConfigureTriggerRequestDelivery
from supr_send_python_sdk.model.workflow_configure_trigger_request_users import WorkflowConfigureTriggerRequestUsers
