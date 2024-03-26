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

from supr_send_python_sdk.type.workflow_configure_trigger_request_delivery_mandatory_channels import WorkflowConfigureTriggerRequestDeliveryMandatoryChannels

class RequiredWorkflowConfigureTriggerRequestDelivery(TypedDict):
    pass

class OptionalWorkflowConfigureTriggerRequestDelivery(TypedDict, total=False):
    # You can enable smart delivery by setting \"smart\":True
    smart: bool

    # Measure that defines the success of this notification. You can set notification status like delivery, interaction or custom success event
    success: str

    # Time window for triggering notifications in case of smart delivery. notification on each channel will be sent with time-interval of [time_to_live / (number_of_channels - 1)] apart. Format - XXdXXhXXmXXs or if its number (n) then delay is in seconds (n)
    time_to_live: str

    mandatory_channels: WorkflowConfigureTriggerRequestDeliveryMandatoryChannels

class WorkflowConfigureTriggerRequestDelivery(RequiredWorkflowConfigureTriggerRequestDelivery, OptionalWorkflowConfigureTriggerRequestDelivery):
    pass