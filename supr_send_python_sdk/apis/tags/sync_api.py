# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from supr_send_python_sdk.paths.v1_subscriber_list_list_id_start_sync.post import ListStartSync
from supr_send_python_sdk.apis.tags.sync_api_raw import SyncApiRaw


class SyncApi(
    ListStartSync,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SyncApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SyncApiRaw(api_client)
