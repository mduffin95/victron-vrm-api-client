# vrm-api-client.SummaryWidgetsApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installationsid_sitewidgets_battery_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_battery_summary) | **GET** /installations/{idSite}/widgets/BatterySummary | Battery summary data
[**installationsid_sitewidgets_bms_diagnostics**](SummaryWidgetsApi.md#installationsid_sitewidgets_bms_diagnostics) | **GET** /installations/{idSite}/widgets/BMSDiagnostics | BMS diagnostics summary data
[**installationsid_sitewidgets_dc_meter**](SummaryWidgetsApi.md#installationsid_sitewidgets_dc_meter) | **GET** /installations/{idSite}/widgets/DCMeter | DC meter summary data
[**installationsid_sitewidgets_ev_charger_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_ev_charger_summary) | **GET** /installations/{idSite}/widgets/EvChargerSummary | EV charger summary data
[**installationsid_sitewidgets_global_link_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_global_link_summary) | **GET** /installations/{idSite}/widgets/GlobalLinkSummary | GlobalLink summary data
[**installationsid_sitewidgets_historic_data**](SummaryWidgetsApi.md#installationsid_sitewidgets_historic_data) | **GET** /installations/{idSite}/widgets/HistoricData | Historic summary data
[**installationsid_sitewidgets_io_extender_in_out**](SummaryWidgetsApi.md#installationsid_sitewidgets_io_extender_in_out) | **GET** /installations/{idSite}/widgets/IOExtenderInOut | IO extender input and output summary data
[**installationsid_sitewidgets_lithium_bms**](SummaryWidgetsApi.md#installationsid_sitewidgets_lithium_bms) | **GET** /installations/{idSite}/widgets/LithiumBMS | Lithium BMS summary data
[**installationsid_sitewidgets_meteorological_sensor**](SummaryWidgetsApi.md#installationsid_sitewidgets_meteorological_sensor) | **GET** /installations/{idSite}/widgets/MeteorologicalSensor | Meteorological summary data
[**installationsid_sitewidgets_motor_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_motor_summary) | **GET** /installations/{idSite}/widgets/MotorSummary | Motor summary data
[**installationsid_sitewidgets_pv_inverter_status**](SummaryWidgetsApi.md#installationsid_sitewidgets_pv_inverter_status) | **GET** /installations/{idSite}/widgets/PVInverterStatus | PV inverter summary data
[**installationsid_sitewidgets_solar_charger_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_solar_charger_summary) | **GET** /installations/{idSite}/widgets/SolarChargerSummary | Solar charger summary data
[**installationsid_sitewidgets_status**](SummaryWidgetsApi.md#installationsid_sitewidgets_status) | **GET** /installations/{idSite}/widgets/Status | System overview summary data
[**installationsid_sitewidgets_tank_summary**](SummaryWidgetsApi.md#installationsid_sitewidgets_tank_summary) | **GET** /installations/{idSite}/widgets/TankSummary | Tank summary data
[**installationsid_sitewidgets_temp_summary_and_graph**](SummaryWidgetsApi.md#installationsid_sitewidgets_temp_summary_and_graph) | **GET** /installations/{idSite}/widgets/TempSummaryAndGraph | Temperature summary data

# **installationsid_sitewidgets_battery_summary**
> InlineResponse20028 installationsid_sitewidgets_battery_summary(x_authorization, id_site, instance=instance)

Battery summary data

Retrieves battery summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Battery summary data
    api_response = api_instance.installationsid_sitewidgets_battery_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_battery_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_bms_diagnostics**
> InlineResponse20028 installationsid_sitewidgets_bms_diagnostics(x_authorization, id_site, instance=instance)

BMS diagnostics summary data

Retrieves BMS diagnostics summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # BMS diagnostics summary data
    api_response = api_instance.installationsid_sitewidgets_bms_diagnostics(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_bms_diagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_dc_meter**
> InlineResponse20028 installationsid_sitewidgets_dc_meter(x_authorization, id_site, instance=instance)

DC meter summary data

Retrieves DC meter summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # DC meter summary data
    api_response = api_instance.installationsid_sitewidgets_dc_meter(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_dc_meter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_ev_charger_summary**
> InlineResponse20028 installationsid_sitewidgets_ev_charger_summary(x_authorization, id_site, instance=instance)

EV charger summary data

Retrieves EV charger summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # EV charger summary data
    api_response = api_instance.installationsid_sitewidgets_ev_charger_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_ev_charger_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_global_link_summary**
> InlineResponse20028 installationsid_sitewidgets_global_link_summary(x_authorization, id_site, instance=instance)

GlobalLink summary data

Retrieves GlobalLink summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # GlobalLink summary data
    api_response = api_instance.installationsid_sitewidgets_global_link_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_global_link_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_historic_data**
> InlineResponse20028 installationsid_sitewidgets_historic_data(x_authorization, id_site, instance=instance)

Historic summary data

Retrieves historic summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Historic summary data
    api_response = api_instance.installationsid_sitewidgets_historic_data(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_historic_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_io_extender_in_out**
> InlineResponse20028 installationsid_sitewidgets_io_extender_in_out(x_authorization, id_site, instance=instance)

IO extender input and output summary data

Retrieves IO extender input and output summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # IO extender input and output summary data
    api_response = api_instance.installationsid_sitewidgets_io_extender_in_out(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_io_extender_in_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_lithium_bms**
> InlineResponse20028 installationsid_sitewidgets_lithium_bms(x_authorization, id_site, instance=instance)

Lithium BMS summary data

Retrieves lithium BMS summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Lithium BMS summary data
    api_response = api_instance.installationsid_sitewidgets_lithium_bms(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_lithium_bms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_meteorological_sensor**
> InlineResponse20028 installationsid_sitewidgets_meteorological_sensor(x_authorization, id_site, instance=instance)

Meteorological summary data

Retrieves meteorological summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Meteorological summary data
    api_response = api_instance.installationsid_sitewidgets_meteorological_sensor(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_meteorological_sensor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_motor_summary**
> InlineResponse20028 installationsid_sitewidgets_motor_summary(x_authorization, id_site, instance=instance)

Motor summary data

Retrieves motor summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Motor summary data
    api_response = api_instance.installationsid_sitewidgets_motor_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_motor_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_pv_inverter_status**
> InlineResponse20028 installationsid_sitewidgets_pv_inverter_status(x_authorization, id_site, instance=instance)

PV inverter summary data

Retrieves PV inverter summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # PV inverter summary data
    api_response = api_instance.installationsid_sitewidgets_pv_inverter_status(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_pv_inverter_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_solar_charger_summary**
> InlineResponse20028 installationsid_sitewidgets_solar_charger_summary(x_authorization, id_site, instance=instance)

Solar charger summary data

Retrieves solar charger summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Solar charger summary data
    api_response = api_instance.installationsid_sitewidgets_solar_charger_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_solar_charger_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_status**
> InlineResponse20028 installationsid_sitewidgets_status(x_authorization, id_site, instance=instance)

System overview summary data

Retrieves system overview summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # System overview summary data
    api_response = api_instance.installationsid_sitewidgets_status(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_tank_summary**
> InlineResponse20028 installationsid_sitewidgets_tank_summary(x_authorization, id_site, instance=instance)

Tank summary data

Retrieves tank summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Tank summary data
    api_response = api_instance.installationsid_sitewidgets_tank_summary(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_tank_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_temp_summary_and_graph**
> InlineResponse20028 installationsid_sitewidgets_temp_summary_and_graph(x_authorization, id_site, instance=instance)

Temperature summary data

Retrieves temperature summary data for an overview, grouped by data attribute.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.SummaryWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)

try:
    # Temperature summary data
    api_response = api_instance.installationsid_sitewidgets_temp_summary_and_graph(x_authorization, id_site, instance=instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SummaryWidgetsApi->installationsid_sitewidgets_temp_summary_and_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_site** | [**object**](.md)| Installation id | 
 **instance** | [**object**](.md)| Instance for which to retrieve data, defaults to 0. | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

