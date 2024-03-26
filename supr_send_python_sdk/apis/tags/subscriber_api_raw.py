# coding: utf-8

"""
    SuprSend API

    SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.

    The version of the OpenAPI document: 1.2.1
    Generated by: https://konfigthis.com
"""

from supr_send_python_sdk.paths.v1_subscriber_list_list_id_version_version_id_subscriber_add.post import AddToDraftListRaw
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_subscriber_add.post import AddToListRaw
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_version_version_id_delete.patch import DeleteDraftListRaw
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_version_version_id_finish_sync.patch import FinishSyncDraftVersionRaw
from supr_send_python_sdk.paths.v1_subscriber_list_list_id_version_version_id_subscriber_remove.post import RemoveFromDraftListRaw
from supr_send_python_sdk.paths.v1_subscriber_distinct_id_category_category_slug.post import UpdateUserPreferencesCategoryRaw


class SubscriberApiRaw(
    AddToDraftListRaw,
    AddToListRaw,
    DeleteDraftListRaw,
    FinishSyncDraftVersionRaw,
    RemoveFromDraftListRaw,
    UpdateUserPreferencesCategoryRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
