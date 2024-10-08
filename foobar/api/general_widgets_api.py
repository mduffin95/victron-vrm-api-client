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


class GeneralWidgetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def installationsid_sitewidgets_gps(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """GPS data for an installation  # noqa: E501

        Retrieves GPS data for the specified installation, used in the GPS widget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_gps(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.installationsid_sitewidgets_gps_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
        else:
            (data) = self.installationsid_sitewidgets_gps_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
            return data

    def installationsid_sitewidgets_gps_with_http_info(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """GPS data for an installation  # noqa: E501

        Retrieves GPS data for the specified installation, used in the GPS widget.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_gps_with_http_info(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_site', 'instance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method installationsid_sitewidgets_gps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `installationsid_sitewidgets_gps`")  # noqa: E501
        # verify the required parameter 'id_site' is set
        if ('id_site' not in params or
                params['id_site'] is None):
            raise ValueError("Missing the required parameter `id_site` when calling `installationsid_sitewidgets_gps`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_site' in params:
            path_params['idSite'] = params['id_site']  # noqa: E501

        query_params = []
        if 'instance' in params:
            query_params.append(('instance', params['instance']))  # noqa: E501

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
            '/installations/{idSite}/widgets/GPS', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20025',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def installationsid_sitewidgets_graph(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """Graph series for a given installation and set of attributes  # noqa: E501

        Retrieves data points for a graph for the given installation and data attributes. Data attributes should be given as id's, codes or both. If not given a timeframe, data for the last day will be retrieved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_graph(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object attribute_codes: Attribute codes for which to retrieve series, repeated for each attribute.
        :param object attribute_ids: Attribute id's for which to retrieve series, repeated for each attribute.
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :param object start: Timestamp from which to fetch data, defaults to one day ago.
        :param object end: Timestamp to which to fetch data, defaults to now.
        :param object width: Width of the graph in pixels, defaults to 768.
        :param object points_per_pixel: The amount of datapoints per pixel of the width of the graph, defaults to two.
        :param object use_min_max: If 1, include the mean, min and max for each datapoint. Else, include only one value per datapoint.
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.installationsid_sitewidgets_graph_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
        else:
            (data) = self.installationsid_sitewidgets_graph_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
            return data

    def installationsid_sitewidgets_graph_with_http_info(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """Graph series for a given installation and set of attributes  # noqa: E501

        Retrieves data points for a graph for the given installation and data attributes. Data attributes should be given as id's, codes or both. If not given a timeframe, data for the last day will be retrieved.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_graph_with_http_info(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object attribute_codes: Attribute codes for which to retrieve series, repeated for each attribute.
        :param object attribute_ids: Attribute id's for which to retrieve series, repeated for each attribute.
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :param object start: Timestamp from which to fetch data, defaults to one day ago.
        :param object end: Timestamp to which to fetch data, defaults to now.
        :param object width: Width of the graph in pixels, defaults to 768.
        :param object points_per_pixel: The amount of datapoints per pixel of the width of the graph, defaults to two.
        :param object use_min_max: If 1, include the mean, min and max for each datapoint. Else, include only one value per datapoint.
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_site', 'attribute_codes', 'attribute_ids', 'instance', 'start', 'end', 'width', 'points_per_pixel', 'use_min_max']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method installationsid_sitewidgets_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `installationsid_sitewidgets_graph`")  # noqa: E501
        # verify the required parameter 'id_site' is set
        if ('id_site' not in params or
                params['id_site'] is None):
            raise ValueError("Missing the required parameter `id_site` when calling `installationsid_sitewidgets_graph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_site' in params:
            path_params['idSite'] = params['id_site']  # noqa: E501

        query_params = []
        if 'attribute_codes' in params:
            query_params.append(('attributeCodes[]', params['attribute_codes']))  # noqa: E501
        if 'attribute_ids' in params:
            query_params.append(('attributeIds[]', params['attribute_ids']))  # noqa: E501
        if 'instance' in params:
            query_params.append(('instance', params['instance']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'points_per_pixel' in params:
            query_params.append(('pointsPerPixel', params['points_per_pixel']))  # noqa: E501
        if 'use_min_max' in params:
            query_params.append(('useMinMax', params['use_min_max']))  # noqa: E501

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
            '/installations/{idSite}/widgets/Graph', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20024',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def installationsid_sitewidgets_hours_of_ac(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """Hours of AC for an installation  # noqa: E501

        Retrieves hours of AC for an installation. If no timeframe is specified, data from the last day will be used.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_hours_of_ac(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :param object start: Timestamp from which to fetch data, defaults to one day ago.
        :param object end: Timestamp to which to fetch data, defaults to now.
        :return: InlineResponse20026
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.installationsid_sitewidgets_hours_of_ac_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
        else:
            (data) = self.installationsid_sitewidgets_hours_of_ac_with_http_info(x_authorization, id_site, **kwargs)  # noqa: E501
            return data

    def installationsid_sitewidgets_hours_of_ac_with_http_info(self, x_authorization, id_site, **kwargs):  # noqa: E501
        """Hours of AC for an installation  # noqa: E501

        Retrieves hours of AC for an installation. If no timeframe is specified, data from the last day will be used.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.installationsid_sitewidgets_hours_of_ac_with_http_info(x_authorization, id_site, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object x_authorization: The bearer token to use. (required)
        :param object id_site: Installation id (required)
        :param object instance: Instance for which to retrieve data, defaults to 0.
        :param object start: Timestamp from which to fetch data, defaults to one day ago.
        :param object end: Timestamp to which to fetch data, defaults to now.
        :return: InlineResponse20026
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_authorization', 'id_site', 'instance', 'start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method installationsid_sitewidgets_hours_of_ac" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_authorization' is set
        if ('x_authorization' not in params or
                params['x_authorization'] is None):
            raise ValueError("Missing the required parameter `x_authorization` when calling `installationsid_sitewidgets_hours_of_ac`")  # noqa: E501
        # verify the required parameter 'id_site' is set
        if ('id_site' not in params or
                params['id_site'] is None):
            raise ValueError("Missing the required parameter `id_site` when calling `installationsid_sitewidgets_hours_of_ac`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_site' in params:
            path_params['idSite'] = params['id_site']  # noqa: E501

        query_params = []
        if 'instance' in params:
            query_params.append(('instance', params['instance']))  # noqa: E501
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501

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
            '/installations/{idSite}/widgets/HoursOfAc', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20026',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
