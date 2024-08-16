# vrm-api-client.UsersApi

All URIs are relative to *https://vrmapi.victronenergy.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersid_useraccesstokenscreate**](UsersApi.md#usersid_useraccesstokenscreate) | **POST** /users/{idUser}/accesstokens/create | Create an access token for a user.
[**usersid_useraccesstokenslist**](UsersApi.md#usersid_useraccesstokenslist) | **GET** /users/{idUser}/accesstokens/list | List all access tokens for a user.
[**usersid_useraccesstokensrevoke**](UsersApi.md#usersid_useraccesstokensrevoke) | **GET** /users/{idUser}/accesstokens/{idAccessToken}/revoke | Revoke an access token for a user.
[**usersid_useraddsite**](UsersApi.md#usersid_useraddsite) | **POST** /users/{idUser}/addsite | Adds a new site
[**usersid_userget_site_id**](UsersApi.md#usersid_userget_site_id) | **POST** /users/{idUser}/get-site-id | Returns site id given site identifier
[**usersid_userinstallations**](UsersApi.md#usersid_userinstallations) | **GET** /users/{idUser}/installations | All installations/sites for a given user
[**usersme**](UsersApi.md#usersme) | **GET** /users/me | Basic information about logged in user

# **usersid_useraccesstokenscreate**
> InlineResponse2005 usersid_useraccesstokenscreate(body, x_authorization, id_user)

Create an access token for a user.

Users can create personal access tokens for usage with external services. These tokens can be used as an alternative way of authentication against the VRM API. The token is returned, after which it is not possible to ever retrieve it again.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
body = vrm-api-client.AccesstokensCreateBody() # AccesstokensCreateBody | 
x_authorization = NULL # object | The bearer token to use.
id_user = NULL # object | User id.

try:
    # Create an access token for a user.
    api_response = api_instance.usersid_useraccesstokenscreate(body, x_authorization, id_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_useraccesstokenscreate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccesstokensCreateBody**](AccesstokensCreateBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_user** | [**object**](.md)| User id. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersid_useraccesstokenslist**
> InlineResponse2006 usersid_useraccesstokenslist(x_authorization, id_user)

List all access tokens for a user.

Retrieves a list of all access token details for this user, excluding the actual token itself. Always returns tokens for the requesting user, never for another, regardless of account type.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
x_authorization = NULL # object | The bearer token to use.
id_user = NULL # object | User id.

try:
    # List all access tokens for a user.
    api_response = api_instance.usersid_useraccesstokenslist(x_authorization, id_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_useraccesstokenslist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_user** | [**object**](.md)| User id. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersid_useraccesstokensrevoke**
> InlineResponse2007 usersid_useraccesstokensrevoke(x_authorization, id_user, id_access_token)

Revoke an access token for a user.

Revokes one or more personal access token for a user.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
x_authorization = NULL # object | The bearer token to use.
id_user = NULL # object | User id.
id_access_token = NULL # object | Access token to revoke, or wildcard '*' to revoke all.

try:
    # Revoke an access token for a user.
    api_response = api_instance.usersid_useraccesstokensrevoke(x_authorization, id_user, id_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_useraccesstokensrevoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_user** | [**object**](.md)| User id. | 
 **id_access_token** | [**object**](.md)| Access token to revoke, or wildcard &#x27;*&#x27; to revoke all. | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersid_useraddsite**
> InlineResponse2003 usersid_useraddsite(body, x_authorization)

Adds a new site

Adds a new site to the user. An email will be sent when the procedure is done.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
body = vrm-api-client.IdUserAddsiteBody() # IdUserAddsiteBody | 
x_authorization = NULL # object | The bearer token to use.

try:
    # Adds a new site
    api_response = api_instance.usersid_useraddsite(body, x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_useraddsite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdUserAddsiteBody**](IdUserAddsiteBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersid_userget_site_id**
> InlineResponse2008 usersid_userget_site_id(body, x_authorization)

Returns site id given site identifier

Retrieves the site id from user's installations given site identifier. Admins can retrieve any installation.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
body = vrm-api-client.IdUserGetsiteidBody() # IdUserGetsiteidBody | 
x_authorization = NULL # object | The bearer token to use.

try:
    # Returns site id given site identifier
    api_response = api_instance.usersid_userget_site_id(body, x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_userget_site_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdUserGetsiteidBody**](IdUserGetsiteidBody.md)|  | 
 **x_authorization** | [**object**](.md)| The bearer token to use. | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersid_userinstallations**
> InlineResponse2004 usersid_userinstallations(x_authorization, id_user, extended=extended, id_site=id_site)

All installations/sites for a given user

Retrieves a list of installations to which the user is connected. Normal users can only retrieve their own installations, dealers only those of their linked customers and admins those of all users.

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
x_authorization = NULL # object | The bearer token to use.
id_user = NULL # object | User id.
extended = NULL # object | If 1, include all optional response values. (optional)
id_site = NULL # object | Id of the site we want to retrieve. (optional)

try:
    # All installations/sites for a given user
    api_response = api_instance.usersid_userinstallations(x_authorization, id_user, extended=extended, id_site=id_site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersid_userinstallations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 
 **id_user** | [**object**](.md)| User id. | 
 **extended** | [**object**](.md)| If 1, include all optional response values. | [optional] 
 **id_site** | [**object**](.md)| Id of the site we want to retrieve. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **usersme**
> InlineResponse2009 usersme(x_authorization)

Basic information about logged in user

Retrieves id, name, email and country of the user that is currently logged in

### Example
```python
from __future__ import print_function
import time
import vrm-api-client
from vrm-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vrm-api-client.UsersApi()
x_authorization = NULL # object | The bearer token to use.

try:
    # Basic information about logged in user
    api_response = api_instance.usersme(x_authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->usersme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_authorization** | [**object**](.md)| The bearer token to use. | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

