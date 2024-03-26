<div align="left">

[![Visit Suprsend](./header.png)](https://suprsend.com)

# Suprsend<a id="suprsend"></a>

SuprSend is a central communication stack for easily creating, managing and delivering notifications to your end users on multiple channels. Our single notification API has all the features set, which enables you to send notifications in a reliable and scalable manner and take care of end user experience, thereby eliminating the need to develop any notification service in-house for transactional/engagement notifications.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`suprsend.brand.brand_data_get`](#suprsendbrandbrand_data_get)
  * [`suprsend.brand.create_or_update`](#suprsendbrandcreate_or_update)
  * [`suprsend.brand.get_categories`](#suprsendbrandget_categories)
  * [`suprsend.brand.list_get`](#suprsendbrandlist_get)
  * [`suprsend.brand.update_default_preference`](#suprsendbrandupdate_default_preference)
  * [`suprsend.broadcast.trigger_message_list`](#suprsendbroadcasttrigger_message_list)
  * [`suprsend.event.trigger_event`](#suprsendeventtrigger_event)
  * [`suprsend.pref_category.get_user_preferences_all_categories`](#suprsendpref_categoryget_user_preferences_all_categories)
  * [`suprsend.preference.get_user_channel_preferences`](#suprsendpreferenceget_user_channel_preferences)
  * [`suprsend.preference.update_channel_preferences`](#suprsendpreferenceupdate_channel_preferences)
  * [`suprsend.subscriber.add_to_draft_list`](#suprsendsubscriberadd_to_draft_list)
  * [`suprsend.subscriber.add_to_list`](#suprsendsubscriberadd_to_list)
  * [`suprsend.subscriber.delete_draft_list`](#suprsendsubscriberdelete_draft_list)
  * [`suprsend.subscriber.finish_sync_draft_version`](#suprsendsubscriberfinish_sync_draft_version)
  * [`suprsend.subscriber.remove_from_draft_list`](#suprsendsubscriberremove_from_draft_list)
  * [`suprsend.subscriber.update_user_preferences_category`](#suprsendsubscriberupdate_user_preferences_category)
  * [`suprsend.subscriber_list.create_list`](#suprsendsubscriber_listcreate_list)
  * [`suprsend.subscriber_list.delete_list`](#suprsendsubscriber_listdelete_list)
  * [`suprsend.subscriber_list.get_all_lists`](#suprsendsubscriber_listget_all_lists)
  * [`suprsend.subscriber_list.get_list_data`](#suprsendsubscriber_listget_list_data)
  * [`suprsend.subscriber_list.remove_subscribers_from_list`](#suprsendsubscriber_listremove_subscribers_from_list)
  * [`suprsend.sync.list_start_sync`](#suprsendsynclist_start_sync)
  * [`suprsend.template.get_content_channel`](#suprsendtemplateget_content_channel)
  * [`suprsend.template.get_details`](#suprsendtemplateget_details)
  * [`suprsend.template.get_list`](#suprsendtemplateget_list)
  * [`suprsend.workflow.configure_trigger`](#suprsendworkflowconfigure_trigger)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=SuprSend&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from supr_send_python_sdk import SuprSend, ApiException

suprsend = SuprSend(
    sec0="YOUR_API_KEY",
)

try:
    # Get Brand data
    brand_data_get_response = suprsend.brand.brand_data_get(
        brand_id="brand_id_example",
    )
except ApiException as e:
    print("Exception when calling BrandApi.brand_data_get: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from supr_send_python_sdk import SuprSend, ApiException

suprsend = SuprSend(
    sec0="YOUR_API_KEY",
)


async def main():
    try:
        # Get Brand data
        brand_data_get_response = await suprsend.brand.abrand_data_get(
            brand_id="brand_id_example",
        )
    except ApiException as e:
        print("Exception when calling BrandApi.brand_data_get: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from supr_send_python_sdk import SuprSend, ApiException

suprsend = SuprSend(
    sec0="YOUR_API_KEY",
)

try:
    # Get Brand data
    brand_data_get_response = suprsend.brand.raw.brand_data_get(
        brand_id="brand_id_example",
    )
    pprint(brand_data_get_response.headers)
    pprint(brand_data_get_response.status)
    pprint(brand_data_get_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BrandApi.brand_data_get: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `suprsend.brand.brand_data_get`<a id="suprsendbrandbrand_data_get"></a>

API to get brand settings corresponding to a brand id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
brand_data_get_response = suprsend.brand.brand_data_get(
    brand_id="brand_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

unique identifier of the brand you want to get the details for

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/brand/{brand_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.brand.create_or_update`<a id="suprsendbrandcreate_or_update"></a>

API to create a new Brand OR update an existing Brand

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_response = suprsend.brand.create_or_update(
    brand_name="Awesome Brand",
    brand_id="brand_id_example",
    logo="https://ik.imagekit.io/l0quatz6utm/suprsend/staging/media/suprsend-only-logo_c8aa27faef118418e8c5bd7b31a1cafc74e09200.png",
    primary_color="#ff0000",
    secondary_color="#00ff00",
    tertiary_color="#0000ff",
    preference_page_url="string_example",
    social_links={
        "website": "https://suprsend.com",
    },
    properties="string_example",
    content___type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_name: `str`<a id="brand_name-str"></a>

Name of the brand. You can add company / organization name here

##### brand_id: `str`<a id="brand_id-str"></a>

unique identifier of the brand that you want to create / update

##### logo: `str`<a id="logo-str"></a>

URL of the brand logo

##### primary_color: `str`<a id="primary_color-str"></a>

Primary color of the brand - used for designing brand template. If you don't provide any of the colors for the brand, SuprSend will assume you want to use the default values, so color settings will automatically be set to the color settings of default brand.

##### secondary_color: `str`<a id="secondary_color-str"></a>

Secondary color of the brand - not used for designing the default templates. You can however add this property and use it in your templates

##### tertiary_color: `str`<a id="tertiary_color-str"></a>

Tertiary color of the brand - not used for designing the default templates. You can however add this property and use it in your templates

##### preference_page_url: `str`<a id="preference_page_url-str"></a>

Link of the hosted preference page inside the brand product

##### social_links: [`BrandCreateOrUpdateRequestSocialLinks`](./supr_send_python_sdk/type/brand_create_or_update_request_social_links.py)<a id="social_links-brandcreateorupdaterequestsociallinkssupr_send_python_sdktypebrand_create_or_update_request_social_linkspy"></a>


##### properties: `str`<a id="properties-str"></a>

Custom properties associated with the brand. Example value - `{\\\"k1\\\": \\\"v1\\\", \\\"k2\\\": 1.0}` <br> Update operation on properties works like upsert on 1st-level keys (i.e. if top-level key doesn't already exist, then it will be added, otherwise its value will be replaced by the new value. All other key-value pairs will remain unchanged).

##### content___type: `str`<a id="content___type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrandCreateOrUpdateRequest`](./supr_send_python_sdk/type/brand_create_or_update_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/brand/{brand_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.brand.get_categories`<a id="suprsendbrandget_categories"></a>

API to get Brand categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_categories_response = suprsend.brand.get_categories(
    brand_id="brand_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

unique identifier of the brand you want to get default preferences for

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/brand/{brand_id}/category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.brand.list_get`<a id="suprsendbrandlist_get"></a>

API to get the list of brands available in your workspace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_get_response = suprsend.brand.list_get(
    limit="20",
    offset="0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

number of results to be returned in API response

##### offset: `str`<a id="offset-str"></a>

starting position of brand list

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/brand` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.brand.update_default_preference`<a id="suprsendbrandupdate_default_preference"></a>

API to update user default preferences for a brand

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_default_preference_response = suprsend.brand.update_default_preference(
    brand_id="brand_id_example",
    category_slug="category_slug_example",
    preference="opt_in",
    visible_to_subscriber=True,
    mandatory_channels=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### brand_id: `str`<a id="brand_id-str"></a>

unique identifier of the brand you want to update default preferences for

##### category_slug: `str`<a id="category_slug-str"></a>

notification category slug. You can get this from Notification Categories page on SuprSend dashboard -> Settings page

##### preference: `str`<a id="preference-str"></a>

set `**opt_in**` to send notifications on all channels by default <br>  set `**opt_out**` to not send notifications in this category by default. For instance, **newsletter** <br>  set `**cant_unsubscribe**`if you do not want users to completely opt-out from this category. Notifications will always be sent on mandatory channels in this category.

##### visible_to_subscriber: `bool`<a id="visible_to_subscriber-bool"></a>

set it `false` to hide a category from user's preference page

##### mandatory_channels: [`BrandUpdateDefaultPreferenceRequestMandatoryChannels`](./supr_send_python_sdk/type/brand_update_default_preference_request_mandatory_channels.py)<a id="mandatory_channels-brandupdatedefaultpreferencerequestmandatorychannelssupr_send_python_sdktypebrand_update_default_preference_request_mandatory_channelspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BrandUpdateDefaultPreferenceRequest`](./supr_send_python_sdk/type/brand_update_default_preference_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/brand/{brand_id}/category/{category_slug}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.broadcast.trigger_message_list`<a id="suprsendbroadcasttrigger_message_list"></a>

API to trigger broadcast messages on a list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_message_list_response = suprsend.broadcast.trigger_message_list(
    list_id="_list_id_",
    template="_template_slug_",
    notification_category="transactional",
    workspace_key="workspace_key_example",
    channels=["string_example"],
    data='{ "key": { "k1": "v1", "k2": "v2" } }',
    delay="string_example",
    trigger_at="1970-01-01",
    brand_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

unique identifier to user list that you want to send broadcast messages to.

##### template: `str`<a id="template-str"></a>

Unique slug name of the template created on SuprSend dashboard. You can get this by clicking on the clipboard icon next to the Template name on SuprSend templates page.

##### notification_category: `str`<a id="notification_category-str"></a>

Category in which your notification belongs. You can understand more about them in the [Notification Category](https://docs.suprsend.com/docs/notification-category) documentation

##### workspace_key: `str`<a id="workspace_key-str"></a>

##### channels: [`BroadcastTriggerMessageListRequestChannels`](./supr_send_python_sdk/type/broadcast_trigger_message_list_request_channels.py)<a id="channels-broadcasttriggermessagelistrequestchannelssupr_send_python_sdktypebroadcast_trigger_message_list_request_channelspy"></a>

##### data: `str`<a id="data-str"></a>

Mock data to replace the template variables.

##### delay: `str`<a id="delay-str"></a>

Broadcast will be halted for the time mentioned in delay, and become active once the delay period is over. Format - `XXdXXhXXmXXs` or if its number (n) then delay is in seconds (n)

##### trigger_at: `date`<a id="trigger_at-date"></a>

Trigger broadcast on a specific date-time. Format - date string in ISO 8601 eg. \\\"2022-08-27T20:14:51.643Z\\\"

##### brand_id: `str`<a id="brand_id-str"></a>

string identifier of the brand this broadcast is associated with

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BroadcastTriggerMessageListRequest`](./supr_send_python_sdk/type/broadcast_trigger_message_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{workspace_key}/broadcast` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.event.trigger_event`<a id="suprsendeventtrigger_event"></a>

API used to pass event which can then be used to trigger workflows created on SuprSend dashboard

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trigger_event_response = suprsend.event.trigger_event(
    distinct_id="_distinct_id_",
    event="_event_name_",
    user_operations=[
        {
            "unset": [],
        }
    ],
    properties="{}",
    brand_id="string_example",
    idempotency_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### distinct_id: `str`<a id="distinct_id-str"></a>

distinct_id of recipient who should receive the notification

##### event: `str`<a id="event-str"></a>

string identifier for the event like `product_purchased`

##### user_operations: [`EventTriggerEventRequestuserOperations`](./supr_send_python_sdk/type/event_trigger_event_requestuser_operations.py)<a id="user_operations-eventtriggereventrequestuseroperationssupr_send_python_sdktypeevent_trigger_event_requestuser_operationspy"></a>

##### properties: `str`<a id="properties-str"></a>

a dictionary representing event attributes like `first_name`. Event properties can be used to pass template variables in case of event based trigger

##### brand_id: `str`<a id="brand_id-str"></a>

string identifier of the brand this event is associated with

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency key (valid for 24hours)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EventTriggerEventRequest`](./supr_send_python_sdk/type/event_trigger_event_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/event` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.pref_category.get_user_preferences_all_categories`<a id="suprsendpref_categoryget_user_preferences_all_categories"></a>

API to get user category preferences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_preferences_all_categories_response = (
    suprsend.pref_category.get_user_preferences_all_categories(
        distinct_id="distinct_id_example",
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### distinct_id: `str`<a id="distinct_id-str"></a>

distinct_id of the user whose preferences should be fetched

##### tenant_id: `str`<a id="tenant_id-str"></a>

to fetch user preferences for a particular brand

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber/{distinct_id}/category` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.preference.get_user_channel_preferences`<a id="suprsendpreferenceget_user_channel_preferences"></a>

API to get user channel preferences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_channel_preferences_response = (
    suprsend.preference.get_user_channel_preferences(
        distinct_id="distinct_id_example",
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### distinct_id: `str`<a id="distinct_id-str"></a>

distinct_id of the user whose preferences should be fetched

##### tenant_id: `str`<a id="tenant_id-str"></a>

to fetch user preferences for a particular brand

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber/{distinct_id}/channel_preference` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.preference.update_channel_preferences`<a id="suprsendpreferenceupdate_channel_preferences"></a>

API to update user channel preferences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_channel_preferences_response = suprsend.preference.update_channel_preferences(
    distinct_id="distinct_id_example",
    channel_preferences=[
        {
            "channel": "email",
            "is_restricted": False,
        }
    ],
    tenant_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### distinct_id: `str`<a id="distinct_id-str"></a>

distinct_id of the user whose preferences should be fetched

##### channel_preferences: [`PreferenceUpdateChannelPreferencesRequestChannelPreferences`](./supr_send_python_sdk/type/preference_update_channel_preferences_request_channel_preferences.py)<a id="channel_preferences-preferenceupdatechannelpreferencesrequestchannelpreferencessupr_send_python_sdktypepreference_update_channel_preferences_request_channel_preferencespy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

to fetch user preferences for a particular brand

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PreferenceUpdateChannelPreferencesRequest`](./supr_send_python_sdk/type/preference_update_channel_preferences_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber/{distinct_id}/channel_preference` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.add_to_draft_list`<a id="suprsendsubscriberadd_to_draft_list"></a>

Add subscribers to a draft list with a version_id that uniquely identifies the draft list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_draft_list_response = suprsend.subscriber.add_to_draft_list(
    list_id="_list_id_",
    version_id="__version_id__",
    distinct_ids=["[]"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list to which user needs to be updated

##### version_id: `str`<a id="version_id-str"></a>

Unique string idenitifier of the draft version of the list to which user needs to be updated

##### distinct_ids: [`SubscriberAddToDraftListRequestDistinctIds`](./supr_send_python_sdk/type/subscriber_add_to_draft_list_request_distinct_ids.py)<a id="distinct_ids-subscriberaddtodraftlistrequestdistinctidssupr_send_python_sdktypesubscriber_add_to_draft_list_request_distinct_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberAddToDraftListRequest`](./supr_send_python_sdk/type/subscriber_add_to_draft_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/version/{version_id}/subscriber/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.add_to_list`<a id="suprsendsubscriberadd_to_list"></a>

API to add users / subscribers to the list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_to_list_response = suprsend.subscriber.add_to_list(
    list_id="_list_id_",
    distinct_ids=["_distinct_id1_"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list to which user needs to be updated

##### distinct_ids: [`SubscriberAddToListRequestDistinctIds`](./supr_send_python_sdk/type/subscriber_add_to_list_request_distinct_ids.py)<a id="distinct_ids-subscriberaddtolistrequestdistinctidssupr_send_python_sdktypesubscriber_add_to_list_request_distinct_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberAddToListRequest`](./supr_send_python_sdk/type/subscriber_add_to_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/subscriber/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.delete_draft_list`<a id="suprsendsubscriberdelete_draft_list"></a>

API to delete a list created in your workspace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_draft_list_response = suprsend.subscriber.delete_draft_list(
    list_id="list_id_example",
    version_id="__version_id__",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list which you want to delete

##### version_id: `str`<a id="version_id-str"></a>

Unique identifier of the draft version of the list which needs to be deleted

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/version/{version_id}/delete` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.finish_sync_draft_version`<a id="suprsendsubscriberfinish_sync_draft_version"></a>

Finishes the sync for a draft version and makes that particular version live for the given list_id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
finish_sync_draft_version_response = suprsend.subscriber.finish_sync_draft_version(
    list_id="_list_id_",
    version_id="__version_id__",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list

##### version_id: `str`<a id="version_id-str"></a>

Unique string idenitifier of the draft version of the list which needs to be made active(live)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/version/{version_id}/finish_sync` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.remove_from_draft_list`<a id="suprsendsubscriberremove_from_draft_list"></a>

Remove subscribers from a draft list with a version_id that uniquely identifies the draft list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_from_draft_list_response = suprsend.subscriber.remove_from_draft_list(
    list_id="_list_id_",
    version_id="__version_id__",
    distinct_ids=["[]"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list to which user needs to be updated

##### version_id: `str`<a id="version_id-str"></a>

Unique string idenitifier of the draft version of the list to which user needs to be updated

##### distinct_ids: [`SubscriberRemoveFromDraftListRequestDistinctIds`](./supr_send_python_sdk/type/subscriber_remove_from_draft_list_request_distinct_ids.py)<a id="distinct_ids-subscriberremovefromdraftlistrequestdistinctidssupr_send_python_sdktypesubscriber_remove_from_draft_list_request_distinct_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberRemoveFromDraftListRequest`](./supr_send_python_sdk/type/subscriber_remove_from_draft_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/version/{version_id}/subscriber/remove` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber.update_user_preferences_category`<a id="suprsendsubscriberupdate_user_preferences_category"></a>

API to update user category preferences

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_preferences_category_response = (
    suprsend.subscriber.update_user_preferences_category(
        distinct_id="distinct_id_example",
        category_slug="category_slug_example",
        preference="opt_in",
        opt_out_channels=["string_example"],
        tenant_id="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### distinct_id: `str`<a id="distinct_id-str"></a>

distinct_id of the user whose preferences should be fetched

##### category_slug: `str`<a id="category_slug-str"></a>

notification category slug. You can get this from Notification Categories page on SuprSend dashboard -> Settings page

##### preference: `str`<a id="preference-str"></a>

choose one of the options: `opt_in` if the user has allowed notification in this category and `opt_out` if user wants to discontinue notification in this category

##### opt_out_channels: [`SubscriberUpdateUserPreferencesCategoryRequestOptOutChannels`](./supr_send_python_sdk/type/subscriber_update_user_preferences_category_request_opt_out_channels.py)<a id="opt_out_channels-subscriberupdateuserpreferencescategoryrequestoptoutchannelssupr_send_python_sdktypesubscriber_update_user_preferences_category_request_opt_out_channelspy"></a>

##### tenant_id: `str`<a id="tenant_id-str"></a>

to fetch user preferences for a particular brand

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberUpdateUserPreferencesCategoryRequest`](./supr_send_python_sdk/type/subscriber_update_user_preferences_category_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber/{distinct_id}/category/{category_slug}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber_list.create_list`<a id="suprsendsubscriber_listcreate_list"></a>

API to create / manage lists to send notification to a bulk list of users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_list_response = suprsend.subscriber_list.create_list(
    list_id="_list_id_",
    list_name="_list_name_",
    list_description="_some sample description_",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list. Add an id which defines the type of users who are part of the list

##### list_name: `str`<a id="list_name-str"></a>

Name of the List. Add a name which defines the type of users in the list

##### list_description: `str`<a id="list_description-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberListCreateListRequest`](./supr_send_python_sdk/type/subscriber_list_create_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber_list.delete_list`<a id="suprsendsubscriber_listdelete_list"></a>

API to delete a list created in your workspace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_list_response = suprsend.subscriber_list.delete_list(
    list_id="list_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list which you want to delete

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/delete` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber_list.get_all_lists`<a id="suprsendsubscriber_listget_all_lists"></a>

API to get the data of all the lists created in your workspace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_lists_response = suprsend.subscriber_list.get_all_lists(
    limit="20",
    offset="0",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

number of results to be returned in API response

##### offset: `str`<a id="offset-str"></a>

starting position of brand list

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber_list.get_list_data`<a id="suprsendsubscriber_listget_list_data"></a>

API to get information corresponding to a list id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_data_response = suprsend.subscriber_list.get_list_data(
    list_id="_list_id_",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.subscriber_list.remove_subscribers_from_list`<a id="suprsendsubscriber_listremove_subscribers_from_list"></a>

API to remove users / subscribers from the list

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_subscribers_from_list_response = (
    suprsend.subscriber_list.remove_subscribers_from_list(
        list_id="_list_id_",
        distinct_ids=["_distinct_id1_"],
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique string idenitifier of the list to which user needs to be updated

##### distinct_ids: [`SubscriberListRemoveSubscribersFromListRequestDistinctIds`](./supr_send_python_sdk/type/subscriber_list_remove_subscribers_from_list_request_distinct_ids.py)<a id="distinct_ids-subscriberlistremovesubscribersfromlistrequestdistinctidssupr_send_python_sdktypesubscriber_list_remove_subscribers_from_list_request_distinct_idspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SubscriberListRemoveSubscribersFromListRequest`](./supr_send_python_sdk/type/subscriber_list_remove_subscribers_from_list_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/subscriber/remove` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.sync.list_start_sync`<a id="suprsendsynclist_start_sync"></a>

Starts sync on the active(live) version of the list, identified by list_id, and creates an empty draft version.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_start_sync_response = suprsend.sync.list_start_sync(
    list_id="_list_id_",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: `str`<a id="list_id-str"></a>

Unique identifier of the list on which the sync needs to start to create a draft version

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/subscriber_list/{list_id}/start_sync` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.template.get_content_channel`<a id="suprsendtemplateget_content_channel"></a>

APIs to fetch the content of a particular channel in a template group. It will return data for live and draft version of a template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_content_channel_response = suprsend.template.get_content_channel(
    template_slug="template_slug_example",
    channel_slug="channel_slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_slug: `str`<a id="template_slug-str"></a>

Template group slug you want to fetch content details. You'll get the template slug by clicking on copy button next to template group name on SuprSend dashboard -> template details page.

##### channel_slug: `str`<a id="channel_slug-str"></a>

add one of the template channels  - `email`, `sms`, `whatsapp`, `inbox`, `slack`, `androidpush`, `iospush`, `webpush`

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateGetContentChannelResponse`](./supr_send_python_sdk/pydantic/template_get_content_channel_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/template/{template_slug}/channel/{channel_slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.template.get_details`<a id="suprsendtemplateget_details"></a>

APIs to fetch the content of a template group. It will return data for live and draft version of a template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = suprsend.template.get_details(
    template_slug="template_slug_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_slug: `str`<a id="template_slug-str"></a>

Template group slug you want to fetch content details. You'll get the template slug by clicking on copy button next to template group name on SuprSend dashboard -> template details page.

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateGetDetailsResponse`](./supr_send_python_sdk/pydantic/template_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/template/{template_slug}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.template.get_list`<a id="suprsendtemplateget_list"></a>

APIs to fetch the list of all templates in a workspace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = suprsend.template.get_list(
    has_tag_ids_any="string_example",
    has_channels_any="string_example",
    is_active=True,
    is_archived=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### has_tag_ids_any: `str`<a id="has_tag_ids_any-str"></a>

comma separated string of tag ids attached to the template

##### has_channels_any: `str`<a id="has_channels_any-str"></a>

comma separated string of channels. Returns templates which has any of the channels present from the channel string. Use these keys for channels - `email`, `sms`, `whatsapp`, `inbox`, `slack`, `androidpush`, `iospush`, `webpush`

##### is_active: `bool`<a id="is_active-bool"></a>

Set `true` for published templates, `false` for templates which are in draft. Do not pass this key to return all templates.

##### is_archived: `bool`<a id="is_archived-bool"></a>

Set `true` to get archived templates, default = `false`

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateGetListResponse`](./supr_send_python_sdk/pydantic/template_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/template` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `suprsend.workflow.configure_trigger`<a id="suprsendworkflowconfigure_trigger"></a>

API to configure and trigger workflow dynamically

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
configure_trigger_response = suprsend.workflow.configure_trigger(
    name="_workflow_name_",
    template="_template_slug_",
    notification_category="transactional",
    users=[
        {
            "distinct_id": "_distinct_id_",
            "channels": [],
            "email": [],
            "sms": [],
            "whatsapp": [],
        }
    ],
    workspace_key="workspace_key_example",
    data='{ "key": { "k1": "v1", "k2": "v2" } }',
    delivery={
        "smart": False,
        "success": "seen",
    },
    delay="string_example",
    trigger_at="1970-01-01",
    brand_id="string_example",
    idempotency_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Unique name of the workflow. The workflow name should be easily identifiable for your reference at a later stage. You can see workflow-related analytics on the workflow page (how many notifications were sent, delivered, clicked or interacted).

##### template: `str`<a id="template-str"></a>

Unique slug name of the template created on SuprSend dashboard. You can get this by clicking on the clipboard icon next to the Template name on SuprSend templates page.

##### notification_category: `str`<a id="notification_category-str"></a>

Category in which your notification belongs. You can understand more about them in the 'Notification Category' documentation

##### users: [`WorkflowConfigureTriggerRequestUsers`](./supr_send_python_sdk/type/workflow_configure_trigger_request_users.py)<a id="users-workflowconfiguretriggerrequestuserssupr_send_python_sdktypeworkflow_configure_trigger_request_userspy"></a>

##### workspace_key: `str`<a id="workspace_key-str"></a>

##### data: `str`<a id="data-str"></a>

Mock data to replace the template variables.

##### delivery: [`WorkflowConfigureTriggerRequestDelivery`](./supr_send_python_sdk/type/workflow_configure_trigger_request_delivery.py)<a id="delivery-workflowconfiguretriggerrequestdeliverysupr_send_python_sdktypeworkflow_configure_trigger_request_deliverypy"></a>


##### delay: `str`<a id="delay-str"></a>

Workflow will be halted for the time mentioned in delay, and become active once the delay period is over. Format - `XXdXXhXXmXXs` or if its number (n) then delay is in seconds (n)

##### trigger_at: `date`<a id="trigger_at-date"></a>

Trigger workflow on a specific date-time. Format - date string in ISO 8601 eg. \\\"2022-08-27T20:14:51.643Z\\\"

##### brand_id: `str`<a id="brand_id-str"></a>

string identifier of the brand this workflow is associated with

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency_key (valid for 24hrs)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkflowConfigureTriggerRequest`](./supr_send_python_sdk/type/workflow_configure_trigger_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/{workspace_key}/trigger` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
