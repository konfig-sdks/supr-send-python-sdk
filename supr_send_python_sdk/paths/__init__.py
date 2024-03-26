# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from supr_send_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_TEMPLATE = "/v1/template"
    V1_TEMPLATE_TEMPLATE_SLUG = "/v1/template/{template_slug}"
    V1_TEMPLATE_TEMPLATE_SLUG_CHANNEL_CHANNEL_SLUG = "/v1/template/{template_slug}/channel/{channel_slug}"
    V1_BRAND_BRAND_ID = "/v1/brand/{brand_id}"
    V1_SUBSCRIBER_DISTINCT_ID_CATEGORY_CATEGORY_SLUG = "/v1/subscriber/{distinct_id}/category/{category_slug}"
    V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_ADD = "/v1/subscriber_list/{list_id}/subscriber/add"
    V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_REMOVE = "/v1/subscriber_list/{list_id}/subscriber/remove"
    V1_SUBSCRIBER_LIST_LIST_ID_DELETE = "/v1/subscriber_list/{list_id}/delete"
    V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_DELETE = "/v1/subscriber_list/{list_id}/version/{version_id}/delete"
    V1_SUBSCRIBER_LIST_LIST_ID_START_SYNC = "/v1/subscriber_list/{list_id}/start_sync"
    V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_ADD = "/v1/subscriber_list/{list_id}/version/{version_id}/subscriber/add"
    V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_REMOVE = "/v1/subscriber_list/{list_id}/version/{version_id}/subscriber/remove"
    V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_FINISH_SYNC = "/v1/subscriber_list/{list_id}/version/{version_id}/finish_sync"
    WORKSPACE_KEY_BROADCAST = "/{workspace_key}/broadcast"
    EVENT = "/event"
    WORKSPACE_KEY_TRIGGER = "/{workspace_key}/trigger"
    V1_BRAND = "/v1/brand"
    V1_SUBSCRIBER_DISTINCT_ID_CHANNEL_PREFERENCE = "/v1/subscriber/{distinct_id}/channel_preference"
    V1_SUBSCRIBER_DISTINCT_ID_CATEGORY = "/v1/subscriber/{distinct_id}/category"
    V1_BRAND_BRAND_ID_CATEGORY_CATEGORY_SLUG = "/v1/brand/{brand_id}/category/{category_slug}"
    V1_BRAND_BRAND_ID_CATEGORY = "/v1/brand/{brand_id}/category"
    V1_SUBSCRIBER_LIST = "/v1/subscriber_list"
    V1_SUBSCRIBER_LIST_LIST_ID = "/v1/subscriber_list/{list_id}"
