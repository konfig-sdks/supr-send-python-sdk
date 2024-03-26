import typing_extensions

from supr_send_python_sdk.apis.tags import TagValues
from supr_send_python_sdk.apis.tags.subscriber_api import SubscriberApi
from supr_send_python_sdk.apis.tags.brand_api import BrandApi
from supr_send_python_sdk.apis.tags.subscriber_list_api import SubscriberListApi
from supr_send_python_sdk.apis.tags.template_api import TemplateApi
from supr_send_python_sdk.apis.tags.preference_api import PreferenceApi
from supr_send_python_sdk.apis.tags.event_api import EventApi
from supr_send_python_sdk.apis.tags.pref_category_api import PrefCategoryApi
from supr_send_python_sdk.apis.tags.broadcast_api import BroadcastApi
from supr_send_python_sdk.apis.tags.workflow_api import WorkflowApi
from supr_send_python_sdk.apis.tags.sync_api import SyncApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SUBSCRIBER: SubscriberApi,
        TagValues.BRAND: BrandApi,
        TagValues.SUBSCRIBER_LIST: SubscriberListApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.PREFERENCE: PreferenceApi,
        TagValues.EVENT: EventApi,
        TagValues.PREF_CATEGORY: PrefCategoryApi,
        TagValues.BROADCAST: BroadcastApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.SYNC: SyncApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SUBSCRIBER: SubscriberApi,
        TagValues.BRAND: BrandApi,
        TagValues.SUBSCRIBER_LIST: SubscriberListApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.PREFERENCE: PreferenceApi,
        TagValues.EVENT: EventApi,
        TagValues.PREF_CATEGORY: PrefCategoryApi,
        TagValues.BROADCAST: BroadcastApi,
        TagValues.WORKFLOW: WorkflowApi,
        TagValues.SYNC: SyncApi,
    }
)
