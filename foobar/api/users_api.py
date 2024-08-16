# coding: utf-8

"""
    VRM API

    ## Introduction This document provides a brief overview of some of the available endpoints and their parameters. The API is a REST API, accepting JSON as request body. You can use the try-it tool to play around with it, or use software like Postman.  ## Authentication Most endpoints require authentication, using a JWT token. This token should be placed in the `x-authorization` field in the HTTP header. There are two types of tokens. - Bearer token. Uses the `Bearer <token_value>` format. This is used when logging in to VRM, for example. Can be retrieved from [/auth/login](/operations/auth/login) or [/auth/loginAsDemo](/operations/auth/loginAsDemo). - Access token. Uses the `Token <token_value>` format. This is commonly used for third party applications using the VRM API. Can be created using [/users/{idUser}/accesstokens/create](/operations/users/idUser/accesstokens/create).  ## Rate limiting Most endpoints are by default rate limited with a rolling window of max 200 requests, where every 0.33 seconds a request gets removed from the rolling window. (so on average maximum of 3 requests per second won't get rate limited). There are different types of ratelimiting in VRM. If you receive a 429 with a JSON response, you can check the Retry-After response header to check the amount of seconds you have to wait until retrying.  ## WARNING & DISCLAIMER Whilst publicly available, Victron Energy does not offer support to professional customers or end-users that implement features using the here documented functionality, except in really specific situations (i.e such as a special arrangement with a large OEM customer).  The recommended method for support on the VRM API is to use the Modifications section on Victron Community. This space is frequently visited by many people using the API, and other methods of integrating with Victron products. Direct company support is only offered on a limited basis via your Victron representative.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from foobar.api_client import ApiClient


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def usersid_useraccesstokenscreate(self, body, x_authorization, id_user, **kwargs):  # noqa: E501
        """Create an access token for a user.  # noqa: E501

        Users can create personal access tokens for usage with external services. These tokens can be used as an alternative way of authentication against the VRM API. The token is returned, after which it is not possible to ever retrieve it again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokenscreate(body, x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccesstokensCreateBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_useraccesstokenscreate_with_http_info(body, x_authorization, id_user, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_useraccesstokenscreate_with_http_info(body, x_authorization, id_user, **kwargs)  # noqa: E501
            return data

    def usersid_useraccesstokenscreate_with_http_info(self, body, x_authorization, id_user, **kwargs):  # noqa: E501
        """Create an access token for a user.  # noqa: E501

        Users can create personal access tokens for usage with external services. These tokens can be used as an alternative way of authentication against the VRM API. The token is returned, after which it is not possible to ever retrieve it again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokenscreate_with_http_info(body, x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccesstokensCreateBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_authorization', 'id_user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_useraccesstokenscreate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `usersid_useraccesstokenscreate`")  # noqa: E501
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_useraccesstokenscreate`")  # noqa: E501
        # verify the required parameter 'id_user' is set
        if ('id_user' not in params or
                params['id_user'] is None):
            raise ValueError("Missing the required parameter `id_user` when calling `usersid_useraccesstokenscreate`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_user' in params:
            path_params['idUser'] = params['id_user']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/accesstokens/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersid_useraccesstokenslist(self, x_authorization, id_user, **kwargs):  # noqa: E501
        """List all access tokens for a user.  # noqa: E501

        Retrieves a list of all access token details for this user, excluding the actual token itself. Always returns tokens for the requesting user, never for another, regardless of account type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokenslist(x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_useraccesstokenslist_with_http_info(x_authorization, id_user, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_useraccesstokenslist_with_http_info(x_authorization, id_user, **kwargs)  # noqa: E501
            return data

    def usersid_useraccesstokenslist_with_http_info(self, x_authorization, id_user, **kwargs):  # noqa: E501
        """List all access tokens for a user.  # noqa: E501

        Retrieves a list of all access token details for this user, excluding the actual token itself. Always returns tokens for the requesting user, never for another, regardless of account type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokenslist_with_http_info(x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_user']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_useraccesstokenslist" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_useraccesstokenslist`")  # noqa: E501
        # verify the required parameter 'id_user' is set
        if ('id_user' not in params or
                params['id_user'] is None):
            raise ValueError("Missing the required parameter `id_user` when calling `usersid_useraccesstokenslist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_user' in params:
            path_params['idUser'] = params['id_user']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/accesstokens/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersid_useraccesstokensrevoke(self, x_authorization, id_user, id_access_token, **kwargs):  # noqa: E501
        """Revoke an access token for a user.  # noqa: E501

        Revokes one or more personal access token for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokensrevoke(x_authorization, id_user, id_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :param object id_access_token: Access token to revoke, or wildcard '*' to revoke all. (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_useraccesstokensrevoke_with_http_info(x_authorization, id_user, id_access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_useraccesstokensrevoke_with_http_info(x_authorization, id_user, id_access_token, **kwargs)  # noqa: E501
            return data

    def usersid_useraccesstokensrevoke_with_http_info(self, x_authorization, id_user, id_access_token, **kwargs):  # noqa: E501
        """Revoke an access token for a user.  # noqa: E501

        Revokes one or more personal access token for a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraccesstokensrevoke_with_http_info(x_authorization, id_user, id_access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :param object id_access_token: Access token to revoke, or wildcard '*' to revoke all. (required)
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_user', 'id_access_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_useraccesstokensrevoke" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_useraccesstokensrevoke`")  # noqa: E501
        # verify the required parameter 'id_user' is set
        if ('id_user' not in params or
                params['id_user'] is None):
            raise ValueError("Missing the required parameter `id_user` when calling `usersid_useraccesstokensrevoke`")  # noqa: E501
        # verify the required parameter 'id_access_token' is set
        if ('id_access_token' not in params or
                params['id_access_token'] is None):
            raise ValueError("Missing the required parameter `id_access_token` when calling `usersid_useraccesstokensrevoke`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_user' in params:
            path_params['idUser'] = params['id_user']  # noqa: E501
        if 'id_access_token' in params:
            path_params['idAccessToken'] = params['id_access_token']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/accesstokens/{idAccessToken}/revoke', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersid_useraddsite(self, body, x_authorization, **kwargs):  # noqa: E501
        """Adds a new site  # noqa: E501

        Adds a new site to the user. An email will be sent when the procedure is done.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraddsite(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdUserAddsiteBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_useraddsite_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_useraddsite_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
            return data

    def usersid_useraddsite_with_http_info(self, body, x_authorization, **kwargs):  # noqa: E501
        """Adds a new site  # noqa: E501

        Adds a new site to the user. An email will be sent when the procedure is done.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_useraddsite_with_http_info(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdUserAddsiteBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_useraddsite" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `usersid_useraddsite`")  # noqa: E501
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_useraddsite`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/addsite', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2003',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersid_userget_site_id(self, body, x_authorization, **kwargs):  # noqa: E501
        """Returns site id given site identifier  # noqa: E501

        Retrieves the site id from user's installations given site identifier. Admins can retrieve any installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_userget_site_id(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdUserGetsiteidBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_userget_site_id_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_userget_site_id_with_http_info(body, x_authorization, **kwargs)  # noqa: E501
            return data

    def usersid_userget_site_id_with_http_info(self, body, x_authorization, **kwargs):  # noqa: E501
        """Returns site id given site identifier  # noqa: E501

        Retrieves the site id from user's installations given site identifier. Admins can retrieve any installation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_userget_site_id_with_http_info(body, x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdUserGetsiteidBody body: (required)
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_userget_site_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `usersid_userget_site_id`")  # noqa: E501
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_userget_site_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/get-site-id', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2008',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersid_userinstallations(self, x_authorization, id_user, **kwargs):  # noqa: E501
        """All installations/sites for a given user  # noqa: E501

        Retrieves a list of installations to which the user is connected. Normal users can only retrieve their own installations, dealers only those of their linked customers and admins those of all users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_userinstallations(x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :param object extended: If 1, include all optional response values.
        :param object id_site: Id of the site we want to retrieve.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersid_userinstallations_with_http_info(x_authorization, id_user, **kwargs)  # noqa: E501
        else:
            (data) = self.usersid_userinstallations_with_http_info(x_authorization, id_user, **kwargs)  # noqa: E501
            return data

    def usersid_userinstallations_with_http_info(self, x_authorization, id_user, **kwargs):  # noqa: E501
        """All installations/sites for a given user  # noqa: E501

        Retrieves a list of installations to which the user is connected. Normal users can only retrieve their own installations, dealers only those of their linked customers and admins those of all users.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersid_userinstallations_with_http_info(x_authorization, id_user, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_user: User id. (required)
        :param object extended: If 1, include all optional response values.
        :param object id_site: Id of the site we want to retrieve.
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_user', 'extended', 'id_site']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersid_userinstallations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersid_userinstallations`")  # noqa: E501
        # verify the required parameter 'id_user' is set
        if ('id_user' not in params or
                params['id_user'] is None):
            raise ValueError("Missing the required parameter `id_user` when calling `usersid_userinstallations`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_user' in params:
            path_params['idUser'] = params['id_user']  # noqa: E501

        query_params = []
        if 'extended' in params:
            query_params.append(('extended', params['extended']))  # noqa: E501
        if 'id_site' in params:
            query_params.append(('idSite', params['id_site']))  # noqa: E501

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/{idUser}/installations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def usersme(self, x_authorization, **kwargs):  # noqa: E501
        """Basic information about logged in user  # noqa: E501

        Retrieves id, name, email and country of the user that is currently logged in  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersme(x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.usersme_with_http_info(x_authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.usersme_with_http_info(x_authorization, **kwargs)  # noqa: E501
            return data

    def usersme_with_http_info(self, x_authorization, **kwargs):  # noqa: E501
        """Basic information about logged in user  # noqa: E501

        Retrieves id, name, email and country of the user that is currently logged in  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.usersme_with_http_info(x_authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method usersme" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `usersme`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_authorization' in params:
            header_params['x-authorization'] = params['x_authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/users/me', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
