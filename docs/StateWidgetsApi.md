# vrm_api_client.StateWidgetsApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**installationsid_sitewidgets_battery_external_relay_state_command**](StateWidgetsApi.md#installationsid_sitewidgets_battery_external_relay_state_command) | **GET** /installations/{idSite}/widgets/BatteryExternalRelayState | Battery external relay state graph data
[**installationsid_sitewidgets_battery_monitor_warnings_and_alarms**](StateWidgetsApi.md#installationsid_sitewidgets_battery_monitor_warnings_and_alarms) | **GET** /installations/{idSite}/widgets/BatteryMonitorWarningsAndAlarms | Battery monitor warnings and alarms graph data
[**installationsid_sitewidgets_battery_relay_state**](StateWidgetsApi.md#installationsid_sitewidgets_battery_relay_state) | **GET** /installations/{idSite}/widgets/BatteryRelayState | Battery relay state graph data
[**installationsid_sitewidgets_charger_relay_state**](StateWidgetsApi.md#installationsid_sitewidgets_charger_relay_state) | **GET** /installations/{idSite}/widgets/ChargerRelayState | Charger relay state graph data
[**installationsid_sitewidgets_charger_state**](StateWidgetsApi.md#installationsid_sitewidgets_charger_state) | **GET** /installations/{idSite}/widgets/ChargerState | Charger state graph data
[**installationsid_sitewidgets_ess_battery_life_state**](StateWidgetsApi.md#installationsid_sitewidgets_ess_battery_life_state) | **GET** /installations/{idSite}/widgets/EssBatteryLifeState | ESS battery life state graph data
[**installationsid_sitewidgets_fuel_cell_state**](StateWidgetsApi.md#installationsid_sitewidgets_fuel_cell_state) | **GET** /installations/{idSite}/widgets/FuelCellState | Fuel cell state graph data
[**installationsid_sitewidgets_gateway_relay_state**](StateWidgetsApi.md#installationsid_sitewidgets_gateway_relay_state) | **GET** /installations/{idSite}/widgets/GatewayRelayState | Gateway relay state graph data
[**installationsid_sitewidgets_gateway_relay_two_state**](StateWidgetsApi.md#installationsid_sitewidgets_gateway_relay_two_state) | **GET** /installations/{idSite}/widgets/GatewayRelayTwoState | Gateway relay two state graph data
[**installationsid_sitewidgets_generator_state**](StateWidgetsApi.md#installationsid_sitewidgets_generator_state) | **GET** /installations/{idSite}/widgets/GeneratorState | Generator state graph data
[**installationsid_sitewidgets_input_state**](StateWidgetsApi.md#installationsid_sitewidgets_input_state) | **GET** /installations/{idSite}/widgets/InputState | Input state graph data
[**installationsid_sitewidgets_inverter_charger_state**](StateWidgetsApi.md#installationsid_sitewidgets_inverter_charger_state) | **GET** /installations/{idSite}/widgets/InverterChargerState | Inverter charger state graph data
[**installationsid_sitewidgets_inverter_charger_warnings_and_alarms**](StateWidgetsApi.md#installationsid_sitewidgets_inverter_charger_warnings_and_alarms) | **GET** /installations/{idSite}/widgets/InverterChargerWarningsAndAlarms | Inverter charger warnings and alarms graph data
[**installationsid_sitewidgets_inverter_state**](StateWidgetsApi.md#installationsid_sitewidgets_inverter_state) | **GET** /installations/{idSite}/widgets/InverterState | Inverter state graph data
[**installationsid_sitewidgets_mppt_state**](StateWidgetsApi.md#installationsid_sitewidgets_mppt_state) | **GET** /installations/{idSite}/widgets/MPPTState | MPPT state graph data
[**installationsid_sitewidgets_solar_charger_relay_state**](StateWidgetsApi.md#installationsid_sitewidgets_solar_charger_relay_state) | **GET** /installations/{idSite}/widgets/SolarChargerRelayState | Solar charger relay state graph data
[**installationsid_sitewidgets_ve_bus_state**](StateWidgetsApi.md#installationsid_sitewidgets_ve_bus_state) | **GET** /installations/{idSite}/widgets/VeBusState | VE Bus state graph data
[**installationsid_sitewidgets_ve_bus_warnings_and_alarms**](StateWidgetsApi.md#installationsid_sitewidgets_ve_bus_warnings_and_alarms) | **GET** /installations/{idSite}/widgets/VeBusWarningsAndAlarms | VE Bus warnings and alarms graph data

# **installationsid_sitewidgets_battery_external_relay_state_command**
> InlineResponse20027 installationsid_sitewidgets_battery_external_relay_state_command(x_authorization, id_site, instance=instance, start=start, end=end)

Battery external relay state graph data

Retrieves battery external relay state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Battery external relay state graph data
    api_response = api_instance.installationsid_sitewidgets_battery_external_relay_state_command(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_battery_external_relay_state_command: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_battery_monitor_warnings_and_alarms**
> InlineResponse20027 installationsid_sitewidgets_battery_monitor_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)

Battery monitor warnings and alarms graph data

Retrieves battery monitor warnings and alarms data for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Battery monitor warnings and alarms graph data
    api_response = api_instance.installationsid_sitewidgets_battery_monitor_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_battery_monitor_warnings_and_alarms: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_battery_relay_state**
> InlineResponse20027 installationsid_sitewidgets_battery_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)

Battery relay state graph data

Retrieves battery relay state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Battery relay state graph data
    api_response = api_instance.installationsid_sitewidgets_battery_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_battery_relay_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_charger_relay_state**
> InlineResponse20027 installationsid_sitewidgets_charger_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)

Charger relay state graph data

Retrieves charger relay state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Charger relay state graph data
    api_response = api_instance.installationsid_sitewidgets_charger_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_charger_relay_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_charger_state**
> InlineResponse20027 installationsid_sitewidgets_charger_state(x_authorization, id_site, instance=instance, start=start, end=end)

Charger state graph data

Retrieves charger state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Charger state graph data
    api_response = api_instance.installationsid_sitewidgets_charger_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_charger_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_ess_battery_life_state**
> InlineResponse20027 installationsid_sitewidgets_ess_battery_life_state(x_authorization, id_site, instance=instance, start=start, end=end)

ESS battery life state graph data

Retrieves ESS battery life state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # ESS battery life state graph data
    api_response = api_instance.installationsid_sitewidgets_ess_battery_life_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_ess_battery_life_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_fuel_cell_state**
> InlineResponse20027 installationsid_sitewidgets_fuel_cell_state(x_authorization, id_site, instance=instance, start=start, end=end)

Fuel cell state graph data

Retrieves fuel cell state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Fuel cell state graph data
    api_response = api_instance.installationsid_sitewidgets_fuel_cell_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_fuel_cell_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_gateway_relay_state**
> InlineResponse20027 installationsid_sitewidgets_gateway_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)

Gateway relay state graph data

Retrieves gateway relay state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Gateway relay state graph data
    api_response = api_instance.installationsid_sitewidgets_gateway_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_gateway_relay_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_gateway_relay_two_state**
> InlineResponse20027 installationsid_sitewidgets_gateway_relay_two_state(x_authorization, id_site, instance=instance, start=start, end=end)

Gateway relay two state graph data

Retrieves gateway relay two state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Gateway relay two state graph data
    api_response = api_instance.installationsid_sitewidgets_gateway_relay_two_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_gateway_relay_two_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_generator_state**
> InlineResponse20027 installationsid_sitewidgets_generator_state(x_authorization, id_site, instance=instance, start=start, end=end)

Generator state graph data

Retrieves generator state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Generator state graph data
    api_response = api_instance.installationsid_sitewidgets_generator_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_generator_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_input_state**
> InlineResponse20027 installationsid_sitewidgets_input_state(x_authorization, id_site, instance=instance, start=start, end=end)

Input state graph data

Retrieves input state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Input state graph data
    api_response = api_instance.installationsid_sitewidgets_input_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_input_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_inverter_charger_state**
> InlineResponse20027 installationsid_sitewidgets_inverter_charger_state(x_authorization, id_site, instance=instance, start=start, end=end)

Inverter charger state graph data

Retrieves inverter charger state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Inverter charger state graph data
    api_response = api_instance.installationsid_sitewidgets_inverter_charger_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_inverter_charger_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_inverter_charger_warnings_and_alarms**
> InlineResponse20027 installationsid_sitewidgets_inverter_charger_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)

Inverter charger warnings and alarms graph data

Retrieves inverter warning and alarm state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Inverter charger warnings and alarms graph data
    api_response = api_instance.installationsid_sitewidgets_inverter_charger_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_inverter_charger_warnings_and_alarms: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_inverter_state**
> InlineResponse20027 installationsid_sitewidgets_inverter_state(x_authorization, id_site, instance=instance, start=start, end=end)

Inverter state graph data

Retrieves inverter state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Inverter state graph data
    api_response = api_instance.installationsid_sitewidgets_inverter_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_inverter_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_mppt_state**
> InlineResponse20027 installationsid_sitewidgets_mppt_state(x_authorization, id_site, instance=instance, start=start, end=end)

MPPT state graph data

Retrieves MPPT state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # MPPT state graph data
    api_response = api_instance.installationsid_sitewidgets_mppt_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_mppt_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_solar_charger_relay_state**
> InlineResponse20027 installationsid_sitewidgets_solar_charger_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)

Solar charger relay state graph data

Retrieves solar charger relay state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # Solar charger relay state graph data
    api_response = api_instance.installationsid_sitewidgets_solar_charger_relay_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_solar_charger_relay_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_ve_bus_state**
> InlineResponse20027 installationsid_sitewidgets_ve_bus_state(x_authorization, id_site, instance=instance, start=start, end=end)

VE Bus state graph data

Retrieves VE Bus state changes for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # VE Bus state graph data
    api_response = api_instance.installationsid_sitewidgets_ve_bus_state(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_ve_bus_state: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **installationsid_sitewidgets_ve_bus_warnings_and_alarms**
> InlineResponse20027 installationsid_sitewidgets_ve_bus_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)

VE Bus warnings and alarms graph data

Retrieves VE Bus warnings and alarms data for a state graph. If not given a timeframe, data for the last day will be retrieved.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.StateWidgetsApi()
x_authorization = NULL # object | The bearer token to use.
id_site = NULL # object | Installation id
instance = NULL # object | Instance for which to retrieve data, defaults to 0. (optional)
start = NULL # object | Timestamp from which to fetch data, defaults to one day ago. (optional)
end = NULL # object | Timestamp to which to fetch data, defaults to now. (optional)

try:
    # VE Bus warnings and alarms graph data
    api_response = api_instance.installationsid_sitewidgets_ve_bus_warnings_and_alarms(x_authorization, id_site, instance=instance, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StateWidgetsApi->installationsid_sitewidgets_ve_bus_warnings_and_alarms: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

