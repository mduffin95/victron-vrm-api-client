# vrm-api-client.GeneralWidgetsApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installationsid_sitewidgets_gps**](GeneralWidgetsApi.md#installationsid_sitewidgets_gps) | **GET** /installations/{idSite}/widgets/GPS | GPS data for an installation
[**installationsid_sitewidgets_graph**](GeneralWidgetsApi.md#installationsid_sitewidgets_graph) | **GET** /installations/{idSite}/widgets/Graph | Graph series for a given installation and set of attributes
[**installationsid_sitewidgets_hours_of_ac**](GeneralWidgetsApi.md#installationsid_sitewidgets_hours_of_ac) | **GET** /installations/{idSite}/widgets/HoursOfAc | Hours of AC for an installation

# **installationsid_sitewidgets_gps**
> InlineResponse20025 installationsid_sitewidgets_gps(x_authorization, id_site, instance=instance)

GPS data for an installation

Retrieves GPS data for the specified installation, used in the GPS widget.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.GeneralWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # GPS data for an installation
    api_response = api_instance.installationsid_sitewidgets_gps(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralWidgetsApi->installationsid_sitewidgets_gps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_graph**
> InlineResponse20024 installationsid_sitewidgets_graph(x_authorization, id_site, attribute_codes=attribute_codes, attribute_ids=attribute_ids, instance=instance, start=start, end=end, width=width, points_per_pixel=points_per_pixel, use_min_max=use_min_max)

Graph series for a given installation and set of attributes

Retrieves data points for a graph for the given installation and data attributes. Data attributes should be given as id's, codes or both. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.GeneralWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
attribute_codes = NULL # object | Attribute codes for which to retrieve series, repeated for each attribute. (optional)
attribute_ids = NULL # object | Attribute id's for which to retrieve series, repeated for each attribute. (optional)
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)
width = NULL # object | Width of the graph in pixels, defaults to 768. (optional)
points_per_pixel = NULL # object | The amount of datapoints per pixel of the width of the graph, defaults to two. (optional)
use_min_max = NULL # object | If 1, include the mean, min and max for each datapoint. Else, include only one value per datapoint. (optional)

try:
    # Graph series for a given installation and set of attributes
    api_response = api_instance.installationsid_sitewidgets_graph(x_authorization, id_site, attribute_codes=attribute_codes, attribute_ids=attribute_ids, instance=instance, start=start, end=end, width=width, points_per_pixel=points_per_pixel, use_min_max=use_min_max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralWidgetsApi->installationsid_sitewidgets_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **attribute_codes** | [**object**](.md)| Attribute codes for which to retrieve series, repeated for each attribute. | [optional] 
 **attribute_ids** | [**object**](.md)| Attribute id&#x27;s for which to retrieve series, repeated for each attribute. | [optional] 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 
 **start** | [**object**](.md)| Timestamp from which to fetch data, defaults to one day ago. | [optional] 
 **end** | [**object**](.md)| Timestamp to which to fetch data, defaults to now. | [optional] 
 **width** | [**object**](.md)| Width of the graph in pixels, defaults to 768. | [optional] 
 **points_per_pixel** | [**object**](.md)| The amount of datapoints per pixel of the width of the graph, defaults to two. | [optional] 
 **use_min_max** | [**object**](.md)| If 1, include the mean, min and max for each datapoint. Else, include only one value per datapoint. | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_hours_of_ac**
> InlineResponse20026 installationsid_sitewidgets_hours_of_ac(x_authorization, id_site, instance=instance, start=start, end=end)

Hours of AC for an installation

Retrieves hours of AC for an installation. If no timeframe is specified, data from the last day will be used.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.GeneralWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Hours of AC for an installation
    api_response = api_instance.installationsid_sitewidgets_hours_of_ac(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralWidgetsApi->installationsid_sitewidgets_hours_of_ac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 
 **start** | [**object**](.md)| Timestamp from which to fetch data, defaults to one day ago. | [optional] 
 **end** | [**object**](.md)| Timestamp to which to fetch data, defaults to now. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

