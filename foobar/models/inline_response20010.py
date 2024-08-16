# coding: utf-8

"""
    VRM API

    ## Introduction This document provides a brief overview of some of the available endpoints and their parameters. The API is a REST API, accepting JSON as request body. You can use the try-it tool to play around with it, or use software like Postman.  ## Authentication Most endpoints require authentication, using a JWT token. This token should be placed in the `x-authorization` field in the HTTP header. There are two types of tokens. - Bearer token. Uses the `Bearer <token_value>` format. This is used when logging in to VRM, for example. Can be retrieved from [/auth/login](/operations/auth/login) or [/auth/loginAsDemo](/operations/auth/loginAsDemo). - Access token. Uses the `Token <token_value>` format. This is commonly used for third party applications using the VRM API. Can be created using [/users/{idUser}/accesstokens/create](/operations/users/idUser/accesstokens/create).  ## Rate limiting Most endpoints are by default rate limited with a rolling window of max 200 requests, where every 0.33 seconds a request gets removed from the rolling window. (so on average maximum of 3 requests per second won't get rate limited). There are different types of ratelimiting in VRM. If you receive a 429 with a JSON response, you can check the Retry-After response header to check the amount of seconds you have to wait until retrying.  ## WARNING & DISCLAIMER Whilst publicly available, Victron Energy does not offer support to professional customers or end-users that implement features using the here documented functionality, except in really specific situations (i.e such as a special arrangement with a large OEM customer).  The recommended method for support on the VRM API is to use the Modifications section on Victron Community. This space is frequently visited by many people using the API, and other methods of integrating with Victron products. Direct company support is only offered on a limited basis via your Victron representative.  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20010(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'success': 'object',
        'rate_limited': 'object',
        'alarms': 'object',
        'devices': 'object',
        'users': 'object',
        'attributes': 'object'
    }

    attribute_map = {
        'success': 'success',
        'rate_limited': 'rateLimited',
        'alarms': 'alarms',
        'devices': 'devices',
        'users': 'users',
        'attributes': 'attributes'
    }

    def __init__(self, success=None, rate_limited=None, alarms=None, devices=None, users=None, attributes=None):  # noqa: E501
        """InlineResponse20010 - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._rate_limited = None
        self._alarms = None
        self._devices = None
        self._users = None
        self._attributes = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if rate_limited is not None:
            self.rate_limited = rate_limited
        if alarms is not None:
            self.alarms = alarms
        if devices is not None:
            self.devices = devices
        if users is not None:
            self.users = users
        if attributes is not None:
            self.attributes = attributes

    @property
    def success(self):
        """Gets the success of this InlineResponse20010.  # noqa: E501

        True if the request was successful.  # noqa: E501

        :return: The success of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse20010.

        True if the request was successful.  # noqa: E501

        :param success: The success of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._success = success

    @property
    def rate_limited(self):
        """Gets the rate_limited of this InlineResponse20010.  # noqa: E501


        :return: The rate_limited of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._rate_limited

    @rate_limited.setter
    def rate_limited(self, rate_limited):
        """Sets the rate_limited of this InlineResponse20010.


        :param rate_limited: The rate_limited of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._rate_limited = rate_limited

    @property
    def alarms(self):
        """Gets the alarms of this InlineResponse20010.  # noqa: E501

        All alarms that may trigger on this installation  # noqa: E501

        :return: The alarms of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        """Sets the alarms of this InlineResponse20010.

        All alarms that may trigger on this installation  # noqa: E501

        :param alarms: The alarms of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._alarms = alarms

    @property
    def devices(self):
        """Gets the devices of this InlineResponse20010.  # noqa: E501

        All devices linked to this installation  # noqa: E501

        :return: The devices of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this InlineResponse20010.

        All devices linked to this installation  # noqa: E501

        :param devices: The devices of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._devices = devices

    @property
    def users(self):
        """Gets the users of this InlineResponse20010.  # noqa: E501

        All users for this installation that may or may not receive notifications (mail, SMS)  # noqa: E501

        :return: The users of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this InlineResponse20010.

        All users for this installation that may or may not receive notifications (mail, SMS)  # noqa: E501

        :param users: The users of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._users = users

    @property
    def attributes(self):
        """Gets the attributes of this InlineResponse20010.  # noqa: E501

        All data attributes that can be used for setting up alarms  # noqa: E501

        :return: The attributes of this InlineResponse20010.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this InlineResponse20010.

        All data attributes that can be used for setting up alarms  # noqa: E501

        :param attributes: The attributes of this InlineResponse20010.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse20010, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
