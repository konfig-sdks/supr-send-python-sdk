# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from supr_send_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from supr_send_python_sdk.api_response import AsyncGeneratorResponse
from supr_send_python_sdk import api_client, exceptions
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

from supr_send_python_sdk.model.workflow_configure_trigger_request import WorkflowConfigureTriggerRequest as WorkflowConfigureTriggerRequestSchema
from supr_send_python_sdk.model.workflow_configure_trigger_request_delivery import WorkflowConfigureTriggerRequestDelivery as WorkflowConfigureTriggerRequestDeliverySchema
from supr_send_python_sdk.model.workflow_configure_trigger_request_users import WorkflowConfigureTriggerRequestUsers as WorkflowConfigureTriggerRequestUsersSchema

from supr_send_python_sdk.type.workflow_configure_trigger_request_delivery import WorkflowConfigureTriggerRequestDelivery
from supr_send_python_sdk.type.workflow_configure_trigger_request import WorkflowConfigureTriggerRequest
from supr_send_python_sdk.type.workflow_configure_trigger_request_users import WorkflowConfigureTriggerRequestUsers

from ...api_client import Dictionary
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_users import WorkflowConfigureTriggerRequestUsers as WorkflowConfigureTriggerRequestUsersPydantic
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request import WorkflowConfigureTriggerRequest as WorkflowConfigureTriggerRequestPydantic
from supr_send_python_sdk.pydantic.workflow_configure_trigger_request_delivery import WorkflowConfigureTriggerRequestDelivery as WorkflowConfigureTriggerRequestDeliveryPydantic

from . import path

# Path params
WorkspaceKeySchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'workspace_key': typing.Union[WorkspaceKeySchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_workspace_key = api_client.PathParameter(
    name="workspace_key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkspaceKeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = WorkflowConfigureTriggerRequestSchema


request_body_workflow_configure_trigger_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'sec0',
]
SchemaFor202ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = schemas.StrSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: str


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '202': _response_for_202,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _configure_trigger_mapped_args(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if template is not None:
            _body["template"] = template
        if notification_category is not None:
            _body["notification_category"] = notification_category
        if users is not None:
            _body["users"] = users
        if data is not None:
            _body["data"] = data
        if delivery is not None:
            _body["delivery"] = delivery
        if delay is not None:
            _body["delay"] = delay
        if trigger_at is not None:
            _body["trigger_at"] = trigger_at
        if brand_id is not None:
            _body["brand_id"] = brand_id
        if idempotency_key is not None:
            _body["$idempotency_key"] = idempotency_key
        args.body = _body
        if workspace_key is not None:
            _path_params["workspace_key"] = workspace_key
        args.path = _path_params
        return args

    async def _aconfigure_trigger_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Trigger Workflow
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_workspace_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{workspace_key}/trigger',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_workflow_configure_trigger_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _configure_trigger_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Trigger Workflow
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_workspace_key,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/{workspace_key}/trigger',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_workflow_configure_trigger_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ConfigureTriggerRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aconfigure_trigger(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._configure_trigger_mapped_args(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
        )
        return await self._aconfigure_trigger_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def configure_trigger(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._configure_trigger_mapped_args(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
        )
        return self._configure_trigger_oapg(
            body=args.body,
            path_params=args.path,
        )

class ConfigureTrigger(BaseApi):

    async def aconfigure_trigger(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.aconfigure_trigger(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def configure_trigger(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.configure_trigger(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._configure_trigger_mapped_args(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
        )
        return await self._aconfigure_trigger_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        template: str,
        notification_category: str,
        users: WorkflowConfigureTriggerRequestUsers,
        workspace_key: str,
        data: typing.Optional[str] = None,
        delivery: typing.Optional[WorkflowConfigureTriggerRequestDelivery] = None,
        delay: typing.Optional[str] = None,
        trigger_at: typing.Optional[date] = None,
        brand_id: typing.Optional[str] = None,
        idempotency_key: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._configure_trigger_mapped_args(
            name=name,
            template=template,
            notification_category=notification_category,
            users=users,
            workspace_key=workspace_key,
            data=data,
            delivery=delivery,
            delay=delay,
            trigger_at=trigger_at,
            brand_id=brand_id,
            idempotency_key=idempotency_key,
        )
        return self._configure_trigger_oapg(
            body=args.body,
            path_params=args.path,
        )

