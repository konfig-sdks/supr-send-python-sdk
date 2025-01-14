# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from supr_send_python_sdk.paths.v1_subscriber_list.post import CreateList
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_delete.patch import DeleteList
from supr_send_python_sdk.paths.v1_subscriber_list.get import GetAllLists
from supr_send_python_sdk.paths.v1_subscriber_list_list_id.get import GetListData
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_subscriber_remove.post import RemoveSubscribersFromList
from supr_send_python_sdk.apis.tags.subscriber_list_api_raw import SubscriberListApiRaw


class SubscriberListApi(
    CreateList,
    DeleteList,
    GetAllLists,
    GetListData,
    RemoveSubscribersFromList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SubscriberListApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SubscriberListApiRaw(api_client)
