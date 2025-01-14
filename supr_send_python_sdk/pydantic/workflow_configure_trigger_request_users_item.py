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

from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itemandroidpush import WorkflowConfigureTriggerRequestUsersItemandroidpush
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itemchannels import WorkflowConfigureTriggerRequestUsersItemchannels
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itememail import WorkflowConfigureTriggerRequestUsersItememail
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itemiospush import WorkflowConfigureTriggerRequestUsersItemiospush
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itemsms import WorkflowConfigureTriggerRequestUsersItemsms
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users_itemwhatsapp import WorkflowConfigureTriggerRequestUsersItemwhatsapp

class WorkflowConfigureTriggerRequestUsersItem(BaseModel):
    # unique identifier of the user
    distinct_id: str = Field(alias='distinct_id')

    $channels_: typing.Optional[WorkflowConfigureTriggerRequestUsersItemchannels] = Field(None, alias='$channels')

    $email_: typing.Optional[WorkflowConfigureTriggerRequestUsersItememail] = Field(None, alias='$email')

    $sms_: typing.Optional[WorkflowConfigureTriggerRequestUsersItemsms] = Field(None, alias='$sms')

    $whatsapp_: typing.Optional[WorkflowConfigureTriggerRequestUsersItemwhatsapp] = Field(None, alias='$whatsapp')

    $androidpush_: typing.Optional[WorkflowConfigureTriggerRequestUsersItemandroidpush] = Field(None, alias='$androidpush')

    $iospush_: typing.Optional[WorkflowConfigureTriggerRequestUsersItemiospush] = Field(None, alias='$iospush')

    # Send Slack on a particular channel in user's profile. Use one of the methods to add slack token - 1. slack using email: {\"email\": \"user@example.com\", \"access_token\": \"xoxb-XXXXXXXX\"} ------ 2. slack using member_id: {\"user_id\": \"U/WXXXXXXXX\", \"access_token\": \"xoxb-XXXXXXXX\"} ------- 3. slack channel: {\"channel\": \"CXXXXXXXX\", \"access_token\": \"xoxb-XXXXXXXX\"} -------- 4. slack incoming webhook: {\"incoming_webhook\": { \"url\": \"https://hooks.slack.com/services/TXXXXXXXXX/BXXXXXXXX/XXXXXXXXXXXXXXXXXXX\"}}
    $slack_: typing.Optional[str] = Field(None, alias='$slack')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
