# coding: utf-8

# flake8: noqa
"""
    VRM API

    ## Introduction This document provides a brief overview of some of the available endpoints and their parameters. The API is a REST API, accepting JSON as request body. You can use the try-it tool to play around with it, or use software like Postman.  ## Authentication Most endpoints require authentication, using a JWT token. This token should be placed in the `x-authorization` field in the HTTP header. There are two types of tokens. - Bearer token. Uses the `Bearer <token_value>` format. This is used when logging in to VRM, for example. Can be retrieved from [/auth/login](/operations/auth/login) or [/auth/loginAsDemo](/operations/auth/loginAsDemo). - Access token. Uses the `Token <token_value>` format. This is commonly used for third party applications using the VRM API. Can be created using [/users/{idUser}/accesstokens/create](/operations/users/idUser/accesstokens/create).  ## Rate limiting Most endpoints are by default rate limited with a rolling window of max 200 requests, where every 0.33 seconds a request gets removed from the rolling window. (so on average maximum of 3 requests per second won't get rate limited). There are different types of ratelimiting in VRM. If you receive a 429 with a JSON response, you can check the Retry-After response header to check the amount of seconds you have to wait until retrying.  ## WARNING & DISCLAIMER Whilst publicly available, Victron Energy does not offer support to professional customers or end-users that implement features using the here documented functionality, except in really specific situations (i.e such as a special arrangement with a large OEM customer).  The recommended method for support on the VRM API is to use the Modifications section on Victron Community. This space is frequently visited by many people using the API, and other methods of integrating with Victron products. Direct company support is only offered on a limited basis via your Victron representative.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from vrm-api-client.models.accesstokens_create_body import AccesstokensCreateBody
from vrm-api-client.models.auth_login_body import AuthLoginBody
from vrm-api-client.models.id_site_alarms_body import IdSiteAlarmsBody
from vrm-api-client.models.id_site_alarms_body1 import IdSiteAlarmsBody1
from vrm-api-client.models.id_site_alarms_body2 import IdSiteAlarmsBody2
from vrm-api-client.models.id_site_clearalarm_body import IdSiteClearalarmBody
from vrm-api-client.models.id_site_dynamicesssettings_body import IdSiteDynamicesssettingsBody
from vrm-api-client.models.id_site_invite_body import IdSiteInviteBody
from vrm-api-client.models.id_site_settings_body import IdSiteSettingsBody
from vrm-api-client.models.id_user_addsite_body import IdUserAddsiteBody
from vrm-api-client.models.id_user_getsiteid_body import IdUserGetsiteidBody
from vrm-api-client.models.inline_response200 import InlineResponse200
from vrm-api-client.models.inline_response2001 import InlineResponse2001
from vrm-api-client.models.inline_response20010 import InlineResponse20010
from vrm-api-client.models.inline_response20011 import InlineResponse20011
from vrm-api-client.models.inline_response20012 import InlineResponse20012
from vrm-api-client.models.inline_response20013 import InlineResponse20013
from vrm-api-client.models.inline_response20014 import InlineResponse20014
from vrm-api-client.models.inline_response20015 import InlineResponse20015
from vrm-api-client.models.inline_response20016 import InlineResponse20016
from vrm-api-client.models.inline_response20017 import InlineResponse20017
from vrm-api-client.models.inline_response20018 import InlineResponse20018
from vrm-api-client.models.inline_response20019 import InlineResponse20019
from vrm-api-client.models.inline_response2002 import InlineResponse2002
from vrm-api-client.models.inline_response20020 import InlineResponse20020
from vrm-api-client.models.inline_response20021 import InlineResponse20021
from vrm-api-client.models.inline_response20022 import InlineResponse20022
from vrm-api-client.models.inline_response20023 import InlineResponse20023
from vrm-api-client.models.inline_response20024 import InlineResponse20024
from vrm-api-client.models.inline_response20025 import InlineResponse20025
from vrm-api-client.models.inline_response20026 import InlineResponse20026
from vrm-api-client.models.inline_response20027 import InlineResponse20027
from vrm-api-client.models.inline_response20028 import InlineResponse20028
from vrm-api-client.models.inline_response2003 import InlineResponse2003
from vrm-api-client.models.inline_response2004 import InlineResponse2004
from vrm-api-client.models.inline_response2005 import InlineResponse2005
from vrm-api-client.models.inline_response2006 import InlineResponse2006
from vrm-api-client.models.inline_response2007 import InlineResponse2007
from vrm-api-client.models.inline_response2008 import InlineResponse2008
from vrm-api-client.models.inline_response2009 import InlineResponse2009
from vrm-api-client.models.inline_response401 import InlineResponse401
from vrm-api-client.models.inline_response403 import InlineResponse403
from vrm-api-client.models.inline_response4031 import InlineResponse4031
from vrm-api-client.models.inline_response404 import InlineResponse404
