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


class WorkflowConfigureTriggerRequestDelivery(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    delivery instructions for the workflow. You can set [Smart Delivery](https://docs.suprsend.com/docs/smart-delivery) preference by setting "smart":true
    """


    class MetaOapg:
        
        class properties:
            smart = schemas.BoolSchema
            success = schemas.StrSchema
            time_to_live = schemas.StrSchema
        
            @staticmethod
            def mandatory_channels() -> typing.Type['WorkflowConfigureTriggerRequestDeliveryMandatoryChannels']:
                return WorkflowConfigureTriggerRequestDeliveryMandatoryChannels
            __annotations__ = {
                "smart": smart,
                "success": success,
                "time_to_live": time_to_live,
                "mandatory_channels": mandatory_channels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smart"]) -> MetaOapg.properties.smart: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time_to_live"]) -> MetaOapg.properties.time_to_live: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mandatory_channels"]) -> 'WorkflowConfigureTriggerRequestDeliveryMandatoryChannels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["smart", "success", "time_to_live", "mandatory_channels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smart"]) -> typing.Union[MetaOapg.properties.smart, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> typing.Union[MetaOapg.properties.success, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time_to_live"]) -> typing.Union[MetaOapg.properties.time_to_live, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mandatory_channels"]) -> typing.Union['WorkflowConfigureTriggerRequestDeliveryMandatoryChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["smart", "success", "time_to_live", "mandatory_channels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        smart: typing.Union[MetaOapg.properties.smart, bool, schemas.Unset] = schemas.unset,
        success: typing.Union[MetaOapg.properties.success, str, schemas.Unset] = schemas.unset,
        time_to_live: typing.Union[MetaOapg.properties.time_to_live, str, schemas.Unset] = schemas.unset,
        mandatory_channels: typing.Union['WorkflowConfigureTriggerRequestDeliveryMandatoryChannels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowConfigureTriggerRequestDelivery':
        return super().__new__(
            cls,
            *args,
            smart=smart,
            success=success,
            time_to_live=time_to_live,
            mandatory_channels=mandatory_channels,
            _configuration=_configuration,
            **kwargs,
        )

from supr_send_python_sdk.model.workflow_configure_trigger_request_delivery_mandatory_channels import WorkflowConfigureTriggerRequestDeliveryMandatoryChannels
