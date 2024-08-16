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

class IdSiteInviteBody(object):
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
        'name': 'object',
        'email': 'object',
        'access_level': 'object'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'access_level': 'accessLevel'
    }

    def __init__(self, name=None, email=None, access_level=None):  # noqa: E501
        """IdSiteInviteBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._email = None
        self._access_level = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if access_level is not None:
            self.access_level = access_level

    @property
    def name(self):
        """Gets the name of this IdSiteInviteBody.  # noqa: E501


        :return: The name of this IdSiteInviteBody.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdSiteInviteBody.


        :param name: The name of this IdSiteInviteBody.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this IdSiteInviteBody.  # noqa: E501


        :return: The email of this IdSiteInviteBody.  # noqa: E501
        :rtype: object
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IdSiteInviteBody.


        :param email: The email of this IdSiteInviteBody.  # noqa: E501
        :type: object
        """

        self._email = email

    @property
    def access_level(self):
        """Gets the access_level of this IdSiteInviteBody.  # noqa: E501

        The access level the invited user should have. Value 0 gives demo rights, value 1 gives user rights, and value 2 gives admin rights.  # noqa: E501

        :return: The access_level of this IdSiteInviteBody.  # noqa: E501
        :rtype: object
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        """Sets the access_level of this IdSiteInviteBody.

        The access level the invited user should have. Value 0 gives demo rights, value 1 gives user rights, and value 2 gives admin rights.  # noqa: E501

        :param access_level: The access_level of this IdSiteInviteBody.  # noqa: E501
        :type: object
        """

        self._access_level = access_level

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
        if issubclass(IdSiteInviteBody, dict):
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
        if not isinstance(other, IdSiteInviteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
