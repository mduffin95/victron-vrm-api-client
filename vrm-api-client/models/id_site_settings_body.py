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

class IdSiteSettingsBody(object):
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
        'description': 'object',
        'notes': 'object',
        'phonenumber': 'object',
        'no_data_alarm_timeout': 'object',
        'no_data_alarm_active': 'object',
        'geofence': 'object',
        'geofence_enabled': 'object',
        'alarm_monitoring': 'object',
        'realtime_updates': 'object',
        'inverter_charger_control': 'object'
    }

    attribute_map = {
        'description': 'description',
        'notes': 'notes',
        'phonenumber': 'phonenumber',
        'no_data_alarm_timeout': 'noDataAlarmTimeout',
        'no_data_alarm_active': 'noDataAlarmActive',
        'geofence': 'geofence',
        'geofence_enabled': 'geofenceEnabled',
        'alarm_monitoring': 'alarmMonitoring',
        'realtime_updates': 'realtimeUpdates',
        'inverter_charger_control': 'inverterChargerControl'
    }

    def __init__(self, description=None, notes=None, phonenumber=None, no_data_alarm_timeout=None, no_data_alarm_active=None, geofence=None, geofence_enabled=None, alarm_monitoring=None, realtime_updates=None, inverter_charger_control=None):  # noqa: E501
        """IdSiteSettingsBody - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._notes = None
        self._phonenumber = None
        self._no_data_alarm_timeout = None
        self._no_data_alarm_active = None
        self._geofence = None
        self._geofence_enabled = None
        self._alarm_monitoring = None
        self._realtime_updates = None
        self._inverter_charger_control = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if notes is not None:
            self.notes = notes
        if phonenumber is not None:
            self.phonenumber = phonenumber
        if no_data_alarm_timeout is not None:
            self.no_data_alarm_timeout = no_data_alarm_timeout
        if no_data_alarm_active is not None:
            self.no_data_alarm_active = no_data_alarm_active
        if geofence is not None:
            self.geofence = geofence
        if geofence_enabled is not None:
            self.geofence_enabled = geofence_enabled
        if alarm_monitoring is not None:
            self.alarm_monitoring = alarm_monitoring
        if realtime_updates is not None:
            self.realtime_updates = realtime_updates
        if inverter_charger_control is not None:
            self.inverter_charger_control = inverter_charger_control

    @property
    def description(self):
        """Gets the description of this IdSiteSettingsBody.  # noqa: E501

        Name of the installation  # noqa: E501

        :return: The description of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdSiteSettingsBody.

        Name of the installation  # noqa: E501

        :param description: The description of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def notes(self):
        """Gets the notes of this IdSiteSettingsBody.  # noqa: E501

        Any additional notes related to the installation.  # noqa: E501

        :return: The notes of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this IdSiteSettingsBody.

        Any additional notes related to the installation.  # noqa: E501

        :param notes: The notes of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._notes = notes

    @property
    def phonenumber(self):
        """Gets the phonenumber of this IdSiteSettingsBody.  # noqa: E501

        Phone number associated with the installation.  # noqa: E501

        :return: The phonenumber of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        """Sets the phonenumber of this IdSiteSettingsBody.

        Phone number associated with the installation.  # noqa: E501

        :param phonenumber: The phonenumber of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._phonenumber = phonenumber

    @property
    def no_data_alarm_timeout(self):
        """Gets the no_data_alarm_timeout of this IdSiteSettingsBody.  # noqa: E501

        Timeout for no data alarm.  # noqa: E501

        :return: The no_data_alarm_timeout of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._no_data_alarm_timeout

    @no_data_alarm_timeout.setter
    def no_data_alarm_timeout(self, no_data_alarm_timeout):
        """Sets the no_data_alarm_timeout of this IdSiteSettingsBody.

        Timeout for no data alarm.  # noqa: E501

        :param no_data_alarm_timeout: The no_data_alarm_timeout of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._no_data_alarm_timeout = no_data_alarm_timeout

    @property
    def no_data_alarm_active(self):
        """Gets the no_data_alarm_active of this IdSiteSettingsBody.  # noqa: E501

        Indicates if the no data alarm is active.  # noqa: E501

        :return: The no_data_alarm_active of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._no_data_alarm_active

    @no_data_alarm_active.setter
    def no_data_alarm_active(self, no_data_alarm_active):
        """Sets the no_data_alarm_active of this IdSiteSettingsBody.

        Indicates if the no data alarm is active.  # noqa: E501

        :param no_data_alarm_active: The no_data_alarm_active of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._no_data_alarm_active = no_data_alarm_active

    @property
    def geofence(self):
        """Gets the geofence of this IdSiteSettingsBody.  # noqa: E501

        Geofence settings for the installation.  # noqa: E501

        :return: The geofence of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._geofence

    @geofence.setter
    def geofence(self, geofence):
        """Sets the geofence of this IdSiteSettingsBody.

        Geofence settings for the installation.  # noqa: E501

        :param geofence: The geofence of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._geofence = geofence

    @property
    def geofence_enabled(self):
        """Gets the geofence_enabled of this IdSiteSettingsBody.  # noqa: E501

        Indicates if geofencing is enabled.  # noqa: E501

        :return: The geofence_enabled of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._geofence_enabled

    @geofence_enabled.setter
    def geofence_enabled(self, geofence_enabled):
        """Sets the geofence_enabled of this IdSiteSettingsBody.

        Indicates if geofencing is enabled.  # noqa: E501

        :param geofence_enabled: The geofence_enabled of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._geofence_enabled = geofence_enabled

    @property
    def alarm_monitoring(self):
        """Gets the alarm_monitoring of this IdSiteSettingsBody.  # noqa: E501

        Indicates if alarm monitoring is active.  # noqa: E501

        :return: The alarm_monitoring of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._alarm_monitoring

    @alarm_monitoring.setter
    def alarm_monitoring(self, alarm_monitoring):
        """Sets the alarm_monitoring of this IdSiteSettingsBody.

        Indicates if alarm monitoring is active.  # noqa: E501

        :param alarm_monitoring: The alarm_monitoring of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._alarm_monitoring = alarm_monitoring

    @property
    def realtime_updates(self):
        """Gets the realtime_updates of this IdSiteSettingsBody.  # noqa: E501

        Indicates if real-time updates are enabled.  # noqa: E501

        :return: The realtime_updates of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._realtime_updates

    @realtime_updates.setter
    def realtime_updates(self, realtime_updates):
        """Sets the realtime_updates of this IdSiteSettingsBody.

        Indicates if real-time updates are enabled.  # noqa: E501

        :param realtime_updates: The realtime_updates of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._realtime_updates = realtime_updates

    @property
    def inverter_charger_control(self):
        """Gets the inverter_charger_control of this IdSiteSettingsBody.  # noqa: E501

        Indicates if inverter charger control is active.  # noqa: E501

        :return: The inverter_charger_control of this IdSiteSettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._inverter_charger_control

    @inverter_charger_control.setter
    def inverter_charger_control(self, inverter_charger_control):
        """Sets the inverter_charger_control of this IdSiteSettingsBody.

        Indicates if inverter charger control is active.  # noqa: E501

        :param inverter_charger_control: The inverter_charger_control of this IdSiteSettingsBody.  # noqa: E501
        :type: object
        """

        self._inverter_charger_control = inverter_charger_control

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
        if issubclass(IdSiteSettingsBody, dict):
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
        if not isinstance(other, IdSiteSettingsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
