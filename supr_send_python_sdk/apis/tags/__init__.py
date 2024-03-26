# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from supr_send_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    SUBSCRIBER = "Subscriber"
    BRAND = "Brand"
    SUBSCRIBER_LIST = "SubscriberList"
    TEMPLATE = "Template"
    PREFERENCE = "Preference"
    EVENT = "Event"
    PREF_CATEGORY = "PrefCategory"
    BROADCAST = "Broadcast"
    WORKFLOW = "Workflow"
    SYNC = "Sync"
