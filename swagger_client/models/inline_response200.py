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

class InlineResponse200(object):
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
        'token': 'object',
        'id_user': 'object',
        'verification_mode': 'object',
        'verification_sent': 'object'
    }

    attribute_map = {
        'token': 'token',
        'id_user': 'idUser',
        'verification_mode': 'verification_mode',
        'verification_sent': 'verification_sent'
    }

    def __init__(self, token=None, id_user=None, verification_mode=None, verification_sent=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._id_user = None
        self._verification_mode = None
        self._verification_sent = None
        self.discriminator = None
        self.token = token
        self.id_user = id_user
        self.verification_mode = verification_mode
        self.verification_sent = verification_sent

    @property
    def token(self):
        """Gets the token of this InlineResponse200.  # noqa: E501

        The bearer token that was generated.  # noqa: E501

        :return: The token of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this InlineResponse200.

        The bearer token that was generated.  # noqa: E501

        :param token: The token of this InlineResponse200.  # noqa: E501
        :type: object
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def id_user(self):
        """Gets the id_user of this InlineResponse200.  # noqa: E501

        The id of the user for which the token was generated.  # noqa: E501

        :return: The id_user of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        """Sets the id_user of this InlineResponse200.

        The id of the user for which the token was generated.  # noqa: E501

        :param id_user: The id_user of this InlineResponse200.  # noqa: E501
        :type: object
        """
        if id_user is None:
            raise ValueError("Invalid value for `id_user`, must not be `None`")  # noqa: E501

        self._id_user = id_user

    @property
    def verification_mode(self):
        """Gets the verification_mode of this InlineResponse200.  # noqa: E501

        Which mode is used for verfying a login for this account.  # noqa: E501

        :return: The verification_mode of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._verification_mode

    @verification_mode.setter
    def verification_mode(self, verification_mode):
        """Sets the verification_mode of this InlineResponse200.

        Which mode is used for verfying a login for this account.  # noqa: E501

        :param verification_mode: The verification_mode of this InlineResponse200.  # noqa: E501
        :type: object
        """
        if verification_mode is None:
            raise ValueError("Invalid value for `verification_mode`, must not be `None`")  # noqa: E501

        self._verification_mode = verification_mode

    @property
    def verification_sent(self):
        """Gets the verification_sent of this InlineResponse200.  # noqa: E501

        Whether a verification code was sent, for 2FA.  # noqa: E501

        :return: The verification_sent of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._verification_sent

    @verification_sent.setter
    def verification_sent(self, verification_sent):
        """Sets the verification_sent of this InlineResponse200.

        Whether a verification code was sent, for 2FA.  # noqa: E501

        :param verification_sent: The verification_sent of this InlineResponse200.  # noqa: E501
        :type: object
        """
        if verification_sent is None:
            raise ValueError("Invalid value for `verification_sent`, must not be `None`")  # noqa: E501

        self._verification_sent = verification_sent

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
