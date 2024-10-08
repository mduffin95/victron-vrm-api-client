# coding: utf-8

"""
    VRM API

    ## Introduction This document provides a brief overview of some of the available endpoints and their parameters. The API is a REST API, accepting JSON as request body. You can use the try-it tool to play around with it, or use software like Postman.  ## Authentication Most endpoints require authentication, using a JWT token. This token should be placed in the `x-authorization` field in the HTTP header. There are two types of tokens. - Bearer token. Uses the `Bearer <token_value>` format. This is used when logging in to VRM, for example. Can be retrieved from [/auth/login](/operations/auth/login) or [/auth/loginAsDemo](/operations/auth/loginAsDemo). - Access token. Uses the `Token <token_value>` format. This is commonly used for third party applications using the VRM API. Can be created using [/users/{idUser}/accesstokens/create](/operations/users/idUser/accesstokens/create).  ## Rate limiting Most endpoints are by default rate limited with a rolling window of max 200 requests, where every 0.33 seconds a request gets removed from the rolling window. (so on average maximum of 3 requests per second won't get rate limited). There are different types of ratelimiting in VRM. If you receive a 429 with a JSON response, you can check the Retry-After response header to check the amount of seconds you have to wait until retrying.  ## WARNING & DISCLAIMER Whilst publicly available, Victron Energy does not offer support to professional customers or end-users that implement features using the here documented functionality, except in really specific situations (i.e such as a special arrangement with a large OEM customer).  The recommended method for support on the VRM API is to use the Modifications section on Victron Community. This space is frequently visited by many people using the API, and other methods of integrating with Victron products. Direct company support is only offered on a limited basis via your Victron representative.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.installations_api import InstallationsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInstallationsApi(unittest.TestCase):
    """InstallationsApi unit test stubs"""

    def setUp(self):
        self.api = InstallationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_installations_id_site_alarms_delete(self):
        """Test case for installations_id_site_alarms_delete

        Delete Alarm  # noqa: E501
        """
        pass

    def test_installations_id_site_alarms_get(self):
        """Test case for installations_id_site_alarms_get

        Get Alarms  # noqa: E501
        """
        pass

    def test_installations_id_site_alarms_post(self):
        """Test case for installations_id_site_alarms_post

        Add Alarm  # noqa: E501
        """
        pass

    def test_installations_id_site_alarms_put(self):
        """Test case for installations_id_site_alarms_put

        Edit Alarm  # noqa: E501
        """
        pass

    def test_installations_id_site_dynamic_ess_settings_get(self):
        """Test case for installations_id_site_dynamic_ess_settings_get

        Dynamic ESS configuration  # noqa: E501
        """
        pass

    def test_installations_id_site_dynamic_ess_settings_post(self):
        """Test case for installations_id_site_dynamic_ess_settings_post

        Dynamic ESS configuration  # noqa: E501
        """
        pass

    def test_installations_id_site_invite_post(self):
        """Test case for installations_id_site_invite_post

        Invite user to installation  # noqa: E501
        """
        pass

    def test_installationsid_siteclear_alarm(self):
        """Test case for installationsid_siteclear_alarm

        Clear alarm  # noqa: E501
        """
        pass

    def test_installationsid_sitedata_download(self):
        """Test case for installationsid_sitedata_download

        Download installation data  # noqa: E501
        """
        pass

    def test_installationsid_sitediagnostics(self):
        """Test case for installationsid_sitediagnostics

        Diagnostic data for an installation  # noqa: E501
        """
        pass

    def test_installationsid_sitegps_download(self):
        """Test case for installationsid_sitegps_download

        GPS tracks for an installation  # noqa: E501
        """
        pass

    def test_installationsid_siteoverallstats(self):
        """Test case for installationsid_siteoverallstats

        Overall installation stats  # noqa: E501
        """
        pass

    def test_installationsid_sitesettings(self):
        """Test case for installationsid_sitesettings

        Update settings for a specific installation  # noqa: E501
        """
        pass

    def test_installationsid_sitestats(self):
        """Test case for installationsid_sitestats

        Installation stats  # noqa: E501
        """
        pass

    def test_installationsid_sitesystem_overview(self):
        """Test case for installationsid_sitesystem_overview

        Connected devices for a given installation  # noqa: E501
        """
        pass

    def test_installationsid_sitetags(self):
        """Test case for installationsid_sitetags

        Get installation tags  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
