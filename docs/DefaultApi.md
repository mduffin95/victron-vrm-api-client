# vrm_api_client.DefaultApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authlogin**](DefaultApi.md#authlogin) | **POST** /auth/login | Log in using an e-mail and password
[**authlogin_as_demo**](DefaultApi.md#authlogin_as_demo) | **GET** /auth/loginAsDemo | Log in as the demo account
[**authlogout**](DefaultApi.md#authlogout) | **GET** /auth/logout | Log out using a token

# **authlogin**
> InlineResponse200 authlogin(body)

Log in using an e-mail and password

Used to authenticate as a user to access authenticated routes. 2FA token must be included if 2FA is enabled on the account. Returns a bearer token (JWT).

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.DefaultApi()
body = vrm_api_client.AuthLoginBody() # AuthLoginBody | 

try:
    # Log in using an e-mail and password
    api_response = api_instance.authlogin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->authlogin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthLoginBody**](AuthLoginBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authlogin_as_demo**
> InlineResponse2001 authlogin_as_demo()

Log in as the demo account

Used to authenticate as the demo account. The demo user has limited access to a few demo installations and endpoints, intended for demonstration usage. Returns a bearer token (JWT).

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.DefaultApi()

try:
    # Log in as the demo account
    api_response = api_instance.authlogin_as_demo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->authlogin_as_demo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authlogout**
> InlineResponse2002 authlogout(x_authorization)

Log out using a token

Used to log out a user. The token provided in the authorization header will be blacklisted from the server and can no longer be used for authentication purposes.

### Example
```python
from __future__ import print_function
import time
import vrm_api_client
from vrm_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm_api_client.DefaultApi()
x_authorization = NULL # object | The bearer token to use.

try:
    # Log out using a token
    api_response = api_instance.authlogout(x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->authlogout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

