# vrm-api-client.InstallationsApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installations_id_site_alarms_delete**](InstallationsApi.md#installations_id_site_alarms_delete) | **DELETE** /installations/{idSite}/alarms | Delete Alarm
[**installations_id_site_alarms_get**](InstallationsApi.md#installations_id_site_alarms_get) | **GET** /installations/{idSite}/alarms | Get Alarms
[**installations_id_site_alarms_post**](InstallationsApi.md#installations_id_site_alarms_post) | **POST** /installations/{idSite}/alarms | Add Alarm
[**installations_id_site_alarms_put**](InstallationsApi.md#installations_id_site_alarms_put) | **PUT** /installations/{idSite}/alarms | Edit Alarm
[**installations_id_site_dynamic_ess_settings_get**](InstallationsApi.md#installations_id_site_dynamic_ess_settings_get) | **GET** /installations/{idSite}/dynamic-ess-settings | Dynamic ESS configuration
[**installations_id_site_dynamic_ess_settings_post**](InstallationsApi.md#installations_id_site_dynamic_ess_settings_post) | **POST** /installations/{idSite}/dynamic-ess-settings | Dynamic ESS configuration
[**installations_id_site_invite_post**](InstallationsApi.md#installations_id_site_invite_post) | **POST** /installations/{idSite}/invite | Invite user to installation
[**installationsid_siteclear_alarm**](InstallationsApi.md#installationsid_siteclear_alarm) | **POST** /installations/{idSite}/clear-alarm | Clear alarm
[**installationsid_sitedata_download**](InstallationsApi.md#installationsid_sitedata_download) | **GET** /installations/{idSite}/data-download | Download installation data
[**installationsid_sitediagnostics**](InstallationsApi.md#installationsid_sitediagnostics) | **GET** /installations/{idSite}/diagnostics | Diagnostic data for an installation
[**installationsid_sitegps_download**](InstallationsApi.md#installationsid_sitegps_download) | **GET** /installations/{idSite}/gps-download | GPS tracks for an installation
[**installationsid_siteoverallstats**](InstallationsApi.md#installationsid_siteoverallstats) | **GET** /installations/{idSite}/overallstats | Overall installation stats
[**installationsid_sitesettings**](InstallationsApi.md#installationsid_sitesettings) | **POST** /installations/{idSite}/settings | Update settings for a specific installation
[**installationsid_sitestats**](InstallationsApi.md#installationsid_sitestats) | **GET** /installations/{idSite}/stats | Installation stats
[**installationsid_sitesystem_overview**](InstallationsApi.md#installationsid_sitesystem_overview) | **GET** /installations/{idSite}/system-overview | Connected devices for a given installation
[**installationsid_sitetags**](InstallationsApi.md#installationsid_sitetags) | **GET** /installations/{idSite}/tags | Get installation tags

# **installations_id_site_alarms_delete**
> InlineResponse20013 installations_id_site_alarms_delete(body, x_authorization, id_site)

Delete Alarm

Deletes an alarm already linked to an installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
body = vrm-api-client.IdSiteAlarmsBody2() # IdSiteAlarmsBody2 | 
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation ID

try:
    # Delete Alarm
    api_response = api_instance.installations_id_site_alarms_delete(body, x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_alarms_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSiteAlarmsBody2**](IdSiteAlarmsBody2.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation ID | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_alarms_get**
> InlineResponse20010 installations_id_site_alarms_get(x_authorization, id_site)

Get Alarms

Gets all information about alarms for a specific installation. Next to that, it also receives all data required to create new alarms

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation ID

try:
    # Get Alarms
    api_response = api_instance.installations_id_site_alarms_get(x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_alarms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation ID | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_alarms_post**
> InlineResponse20012 installations_id_site_alarms_post(body, x_authorization, id_site)

Add Alarm

Adds an alarm to an installation. Note that there are two different types of alarms; alarms on enums and alarms on numbers (floats). Note that for floats the AlarmEnabled and NotifyAfterSeconds use PascalCase and for enums they use camelCase. You'll get a warning if the wrong case is used.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
body = vrm-api-client.IdSiteAlarmsBody1() # IdSiteAlarmsBody1 | 
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation ID

try:
    # Add Alarm
    api_response = api_instance.installations_id_site_alarms_post(body, x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_alarms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSiteAlarmsBody1**](IdSiteAlarmsBody1.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation ID | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_alarms_put**
> InlineResponse20011 installations_id_site_alarms_put(body, x_authorization, id_site)

Edit Alarm

Edits an alarm already linked to an installation. Note that there are two different types of alarms; alarms on enums and alarms on numbers (floats). Note that for floats the AlarmEnabled and NotifyAfterSeconds use PascalCase and for enums they use camelCase. You'll get a warning if the wrong case is used.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
body = vrm-api-client.IdSiteAlarmsBody() # IdSiteAlarmsBody | 
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation ID

try:
    # Edit Alarm
    api_response = api_instance.installations_id_site_alarms_put(body, x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_alarms_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSiteAlarmsBody**](IdSiteAlarmsBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation ID | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_dynamic_ess_settings_get**
> InlineResponse20017 installations_id_site_dynamic_ess_settings_get(id, x_authorization)

Dynamic ESS configuration

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
id = NULL # object | The ID of the installation
x_authorization = NULL # object | The bearer token to use.

try:
    # Dynamic ESS configuration
    api_response = api_instance.installations_id_site_dynamic_ess_settings_get(id, x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_dynamic_ess_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| The ID of the installation | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_dynamic_ess_settings_post**
> InlineResponse20017 installations_id_site_dynamic_ess_settings_post(x_authorization, id, body=body)

Dynamic ESS configuration

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id = NULL # object | The ID of the installation
body = vrm-api-client.IdSiteDynamicesssettingsBody() # IdSiteDynamicesssettingsBody |  (optional)

try:
    # Dynamic ESS configuration
    api_response = api_instance.installations_id_site_dynamic_ess_settings_post(x_authorization, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_dynamic_ess_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id** | [**object**](.md)| The ID of the installation | 
 **body** | [**IdSiteDynamicesssettingsBody**](IdSiteDynamicesssettingsBody.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installations_id_site_invite_post**
> InlineResponse20023 installations_id_site_invite_post(body, x_authorization, id_site)

Invite user to installation

Sends an invitation to a user to gain access to a specific installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
body = vrm-api-client.IdSiteInviteBody() # IdSiteInviteBody | 
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation ID

try:
    # Invite user to installation
    api_response = api_instance.installations_id_site_invite_post(body, x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installations_id_site_invite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSiteInviteBody**](IdSiteInviteBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation ID | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_siteclear_alarm**
> InlineResponse20014 installationsid_siteclear_alarm(body, x_authorization, id_site)

Clear alarm

Clears alarms and marks them as cleared by the user in Event Logs.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
body = vrm-api-client.IdSiteClearalarmBody() # IdSiteClearalarmBody | 
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | ID of the installation.

try:
    # Clear alarm
    api_response = api_instance.installationsid_siteclear_alarm(body, x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_siteclear_alarm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdSiteClearalarmBody**](IdSiteClearalarmBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| ID of the installation. | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitedata_download**
> InlineResponse20019 installationsid_sitedata_download(x_authorization, id_site, start=start, end=end, datatype=datatype, format=format, debug=debug, _async=_async)

Download installation data

Retrieves a base64 encoded string containing the specified installation data, in the specified format.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)
datatype = NULL # object | Type of data to export, defaults to log. (optional)
format = NULL # object | Export data file format, defaults to csv. (optional)
debug = NULL # object | Include debug attributes, only for admins and restricted admins, defaults to false. (optional)
_async = NULL # object | If true, the request is executed asynchronously and the result is not included in the response but sent to the email address of the requesting account. (optional)

try:
    # Download installation data
    api_response = api_instance.installationsid_sitedata_download(x_authorization, id_site, start=start, end=end, datatype=datatype, format=format, debug=debug, _async=_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitedata_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **start** | [**object**](.md)| Timestamp from which to fetch data, defaults to one day ago. | [optional] 
 **end** | [**object**](.md)| Timestamp to which to fetch data, defaults to now. | [optional] 
 **datatype** | [**object**](.md)| Type of data to export, defaults to log. | [optional] 
 **format** | [**object**](.md)| Export data file format, defaults to csv. | [optional] 
 **debug** | [**object**](.md)| Include debug attributes, only for admins and restricted admins, defaults to false. | [optional] 
 **_async** | [**object**](.md)| If true, the request is executed asynchronously and the result is not included in the response but sent to the email address of the requesting account. | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitediagnostics**
> InlineResponse20016 installationsid_sitediagnostics(x_authorization, id_site, count=count, page=page)

Diagnostic data for an installation

Retrieves log data for an installation. This endpoint is only accessible to users with access to the installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
count = NULL # object | How many records to fetch, 100 if not specified. (optional)
page = NULL # object | Which page to fetch, 1 if not specified. (optional)

try:
    # Diagnostic data for an installation
    api_response = api_instance.installationsid_sitediagnostics(x_authorization, id_site, count=count, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitediagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **count** | [**object**](.md)| How many records to fetch, 100 if not specified. | [optional] 
 **page** | [**object**](.md)| Which page to fetch, 1 if not specified. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitegps_download**
> installationsid_sitegps_download(x_authorization, id_site, start, end)

GPS tracks for an installation

Retrieves GPS tracks for an installation as a KML file.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
start = NULL # object | Timestamp from which to fetch data.
end = NULL # object | Timestamp to which to fetch data.

try:
    # GPS tracks for an installation
    api_instance.installationsid_sitegps_download(x_authorization, id_site, start, end)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitegps_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **start** | [**object**](.md)| Timestamp from which to fetch data. | 
 **end** | [**object**](.md)| Timestamp to which to fetch data. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.google-earth.kml+xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_siteoverallstats**
> InlineResponse20021 installationsid_siteoverallstats(x_authorization, id_site, type=type, attribute_codes=attribute_codes)

Overall installation stats

Retrieves installation stats grouped by the last year, month, week and day. If the datatype is set to custom, one or more attributes can be provided using the attributeCodes[] parameter.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
type = NULL # object | Type of data to fetch, defaults to live_feed. If set to custom, the attributeCodes[] parameter must be provided. (optional)
attribute_codes = NULL # object | Attribute codes for which to retrieve series, repeated for each attribute. Required at least once if datatype is set to custom. (optional)

try:
    # Overall installation stats
    api_response = api_instance.installationsid_siteoverallstats(x_authorization, id_site, type=type, attribute_codes=attribute_codes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_siteoverallstats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **type** | [**object**](.md)| Type of data to fetch, defaults to live_feed. If set to custom, the attributeCodes[] parameter must be provided. | [optional] 
 **attribute_codes** | [**object**](.md)| Attribute codes for which to retrieve series, repeated for each attribute. Required at least once if datatype is set to custom. | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitesettings**
> InlineResponse20022 installationsid_sitesettings(x_authorization, id, body=body)

Update settings for a specific installation

Allows the user to modify settings related to a specific installation identified by its ID. You can send one or more of the fields you want to update at once.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id = NULL # object | The ID of the installation
body = vrm-api-client.IdSiteSettingsBody() # IdSiteSettingsBody |  (optional)

try:
    # Update settings for a specific installation
    api_response = api_instance.installationsid_sitesettings(x_authorization, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitesettings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id** | [**object**](.md)| The ID of the installation | 
 **body** | [**IdSiteSettingsBody**](IdSiteSettingsBody.md)|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitestats**
> InlineResponse20020 installationsid_sitestats(x_authorization, id_site, start=start, end=end, type=type, interval=interval, attribute_codes=attribute_codes, show_instance=show_instance)

Installation stats

Retrieves installation stats for the specified period, or one day if none specified. If the datatype is set to custom, one or more attributes can be provided using the attributeCodes[] parameter.  There is a maximum allowed time period for each interval, which is: * 31 days for 15 minutes * 31 days for hours * 180 days for days * 140 days for weeks * 24 months for months * 5 years for years 

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)
type = NULL # object | Type of data to fetch, defaults to live_feed. If set to custom, the attributeCodes[] parameter must be provided. (optional)
interval = NULL # object | Time between retrieved data points, defaults to hours. (optional)
attribute_codes = NULL # object | Attribute codes for which to retrieve series, repeated for each attribute. Required at least once if datatype is set to custom. (optional)
show_instance = NULL # object | If included, attributes will be grouped by instance. (optional)

try:
    # Installation stats
    api_response = api_instance.installationsid_sitestats(x_authorization, id_site, start=start, end=end, type=type, interval=interval, attribute_codes=attribute_codes, show_instance=show_instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitestats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **start** | [**object**](.md)| Timestamp from which to fetch data, defaults to one day ago. | [optional] 
 **end** | [**object**](.md)| Timestamp to which to fetch data, defaults to now. | [optional] 
 **type** | [**object**](.md)| Type of data to fetch, defaults to live_feed. If set to custom, the attributeCodes[] parameter must be provided. | [optional] 
 **interval** | [**object**](.md)| Time between retrieved data points, defaults to hours. | [optional] 
 **attribute_codes** | [**object**](.md)| Attribute codes for which to retrieve series, repeated for each attribute. Required at least once if datatype is set to custom. | [optional] 
 **show_instance** | [**object**](.md)| If included, attributes will be grouped by instance. | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitesystem_overview**
> InlineResponse20015 installationsid_sitesystem_overview(x_authorization, id_site)

Connected devices for a given installation

Retrieves a list of devices to which are connected to this installation. This endpoint is only accessible to users with access to the installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id

try:
    # Connected devices for a given installation
    api_response = api_instance.installationsid_sitesystem_overview(x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitesystem_overview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitetags**
> InlineResponse20018 installationsid_sitetags(x_authorization, id_site)

Get installation tags

Tags for an installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.InstallationsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id

try:
    # Get installation tags
    api_response = api_instance.installationsid_sitetags(x_authorization, id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsApi->installationsid_sitetags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

