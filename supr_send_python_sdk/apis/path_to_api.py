import typing_extensions

from supr_send_python_sdk.paths import PathValues
from supr_send_python_sdk.apis.paths.v1_template import V1Template
from supr_send_python_sdk.apis.paths.v1_template_template_slug import V1TemplateTemplateSlug
from supr_send_python_sdk.apis.paths.v1_template_template_slug_channel_channel_slug import V1TemplateTemplateSlugChannelChannelSlug
from supr_send_python_sdk.apis.paths.v1_brand_brand_id import V1BrandBrandId
from supr_send_python_sdk.apis.paths.v1_subscriber_distinct_id_category_category_slug import V1SubscriberDistinctIdCategoryCategorySlug
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_subscriber_add import V1SubscriberListListIdSubscriberAdd
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_subscriber_remove import V1SubscriberListListIdSubscriberRemove
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_delete import V1SubscriberListListIdDelete
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_version_version_id_delete import V1SubscriberListListIdVersionVersionIdDelete
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_start_sync import V1SubscriberListListIdStartSync
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_version_version_id_subscriber_add import V1SubscriberListListIdVersionVersionIdSubscriberAdd
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_version_version_id_subscriber_remove import V1SubscriberListListIdVersionVersionIdSubscriberRemove
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id_version_version_id_finish_sync import V1SubscriberListListIdVersionVersionIdFinishSync
from supr_send_python_sdk.apis.paths.workspace_key_broadcast import WorkspaceKeyBroadcast
from supr_send_python_sdk.apis.paths.event import Event
from supr_send_python_sdk.apis.paths.workspace_key_trigger import WorkspaceKeyTrigger
from supr_send_python_sdk.apis.paths.v1_brand import V1Brand
from supr_send_python_sdk.apis.paths.v1_subscriber_distinct_id_channel_preference import V1SubscriberDistinctIdChannelPreference
from supr_send_python_sdk.apis.paths.v1_subscriber_distinct_id_category import V1SubscriberDistinctIdCategory
from supr_send_python_sdk.apis.paths.v1_brand_brand_id_category_category_slug import V1BrandBrandIdCategoryCategorySlug
from supr_send_python_sdk.apis.paths.v1_brand_brand_id_category import V1BrandBrandIdCategory
from supr_send_python_sdk.apis.paths.v1_subscriber_list import V1SubscriberList
from supr_send_python_sdk.apis.paths.v1_subscriber_list_list_id import V1SubscriberListListId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_TEMPLATE: V1Template,
        PathValues.V1_TEMPLATE_TEMPLATE_SLUG: V1TemplateTemplateSlug,
        PathValues.V1_TEMPLATE_TEMPLATE_SLUG_CHANNEL_CHANNEL_SLUG: V1TemplateTemplateSlugChannelChannelSlug,
        PathValues.V1_BRAND_BRAND_ID: V1BrandBrandId,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CATEGORY_CATEGORY_SLUG: V1SubscriberDistinctIdCategoryCategorySlug,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_ADD: V1SubscriberListListIdSubscriberAdd,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_REMOVE: V1SubscriberListListIdSubscriberRemove,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_DELETE: V1SubscriberListListIdDelete,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_DELETE: V1SubscriberListListIdVersionVersionIdDelete,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_START_SYNC: V1SubscriberListListIdStartSync,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_ADD: V1SubscriberListListIdVersionVersionIdSubscriberAdd,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_REMOVE: V1SubscriberListListIdVersionVersionIdSubscriberRemove,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_FINISH_SYNC: V1SubscriberListListIdVersionVersionIdFinishSync,
        PathValues.WORKSPACE_KEY_BROADCAST: WorkspaceKeyBroadcast,
        PathValues.EVENT: Event,
        PathValues.WORKSPACE_KEY_TRIGGER: WorkspaceKeyTrigger,
        PathValues.V1_BRAND: V1Brand,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CHANNEL_PREFERENCE: V1SubscriberDistinctIdChannelPreference,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CATEGORY: V1SubscriberDistinctIdCategory,
        PathValues.V1_BRAND_BRAND_ID_CATEGORY_CATEGORY_SLUG: V1BrandBrandIdCategoryCategorySlug,
        PathValues.V1_BRAND_BRAND_ID_CATEGORY: V1BrandBrandIdCategory,
        PathValues.V1_SUBSCRIBER_LIST: V1SubscriberList,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID: V1SubscriberListListId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_TEMPLATE: V1Template,
        PathValues.V1_TEMPLATE_TEMPLATE_SLUG: V1TemplateTemplateSlug,
        PathValues.V1_TEMPLATE_TEMPLATE_SLUG_CHANNEL_CHANNEL_SLUG: V1TemplateTemplateSlugChannelChannelSlug,
        PathValues.V1_BRAND_BRAND_ID: V1BrandBrandId,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CATEGORY_CATEGORY_SLUG: V1SubscriberDistinctIdCategoryCategorySlug,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_ADD: V1SubscriberListListIdSubscriberAdd,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_SUBSCRIBER_REMOVE: V1SubscriberListListIdSubscriberRemove,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_DELETE: V1SubscriberListListIdDelete,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_DELETE: V1SubscriberListListIdVersionVersionIdDelete,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_START_SYNC: V1SubscriberListListIdStartSync,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_ADD: V1SubscriberListListIdVersionVersionIdSubscriberAdd,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_SUBSCRIBER_REMOVE: V1SubscriberListListIdVersionVersionIdSubscriberRemove,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID_VERSION_VERSION_ID_FINISH_SYNC: V1SubscriberListListIdVersionVersionIdFinishSync,
        PathValues.WORKSPACE_KEY_BROADCAST: WorkspaceKeyBroadcast,
        PathValues.EVENT: Event,
        PathValues.WORKSPACE_KEY_TRIGGER: WorkspaceKeyTrigger,
        PathValues.V1_BRAND: V1Brand,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CHANNEL_PREFERENCE: V1SubscriberDistinctIdChannelPreference,
        PathValues.V1_SUBSCRIBER_DISTINCT_ID_CATEGORY: V1SubscriberDistinctIdCategory,
        PathValues.V1_BRAND_BRAND_ID_CATEGORY_CATEGORY_SLUG: V1BrandBrandIdCategoryCategorySlug,
        PathValues.V1_BRAND_BRAND_ID_CATEGORY: V1BrandBrandIdCategory,
        PathValues.V1_SUBSCRIBER_LIST: V1SubscriberList,
        PathValues.V1_SUBSCRIBER_LIST_LIST_ID: V1SubscriberListListId,
    }
)
