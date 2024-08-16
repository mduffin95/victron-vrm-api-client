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

class IdSiteDynamicesssettingsBody(object):
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
        'battery_capacity': 'object',
        'battery_costs': 'object',
        'battery_flow_restriction': 'object',
        'battery_price': 'object',
        'buy_energy_provider_id': 'object',
        'buy_price_formula': 'object',
        'buy_price_schedule': 'object',
        'buy_price_type': 'object',
        'charge_power': 'object',
        'discharge_power': 'object',
        'grid_sell': 'object',
        'id_bidding_zone': 'object',
        'is_dess_soc_different': 'object',
        'is_green_mode_on': 'object',
        'is_on': 'object',
        'max_power_from_grid': 'object',
        'max_power_to_grid': 'object',
        'sell_energy_provider_id': 'object',
        'sell_price_schedule': 'object',
        'sell_price_formula': 'object',
        'sell_price_type': 'object',
        'is_periodic_full_charge_on': 'object',
        'periodic_full_charge_duration': 'object',
        'periodic_full_charge_interval': 'object'
    }

    attribute_map = {
        'battery_capacity': 'batteryCapacity',
        'battery_costs': 'batteryCosts',
        'battery_flow_restriction': 'batteryFlowRestriction',
        'battery_price': 'batteryPrice',
        'buy_energy_provider_id': 'buyEnergyProviderId',
        'buy_price_formula': 'buyPriceFormula',
        'buy_price_schedule': 'buyPriceSchedule',
        'buy_price_type': 'buyPriceType',
        'charge_power': 'chargePower',
        'discharge_power': 'dischargePower',
        'grid_sell': 'gridSell',
        'id_bidding_zone': 'idBiddingZone',
        'is_dess_soc_different': 'isDessSocDifferent',
        'is_green_mode_on': 'isGreenModeOn',
        'is_on': 'isOn',
        'max_power_from_grid': 'maxPowerFromGrid',
        'max_power_to_grid': 'maxPowerToGrid',
        'sell_energy_provider_id': 'sellEnergyProviderId',
        'sell_price_schedule': 'sellPriceSchedule',
        'sell_price_formula': 'sellPriceFormula',
        'sell_price_type': 'sellPriceType',
        'is_periodic_full_charge_on': 'isPeriodicFullChargeOn',
        'periodic_full_charge_duration': 'periodicFullChargeDuration',
        'periodic_full_charge_interval': 'periodicFullChargeInterval'
    }

    def __init__(self, battery_capacity=None, battery_costs=None, battery_flow_restriction=None, battery_price=None, buy_energy_provider_id=None, buy_price_formula=None, buy_price_schedule=None, buy_price_type=None, charge_power=None, discharge_power=None, grid_sell=None, id_bidding_zone=None, is_dess_soc_different=None, is_green_mode_on=None, is_on=None, max_power_from_grid=None, max_power_to_grid=None, sell_energy_provider_id=None, sell_price_schedule=None, sell_price_formula=None, sell_price_type=None, is_periodic_full_charge_on=None, periodic_full_charge_duration=None, periodic_full_charge_interval=None):  # noqa: E501
        """IdSiteDynamicesssettingsBody - a model defined in Swagger"""  # noqa: E501
        self._battery_capacity = None
        self._battery_costs = None
        self._battery_flow_restriction = None
        self._battery_price = None
        self._buy_energy_provider_id = None
        self._buy_price_formula = None
        self._buy_price_schedule = None
        self._buy_price_type = None
        self._charge_power = None
        self._discharge_power = None
        self._grid_sell = None
        self._id_bidding_zone = None
        self._is_dess_soc_different = None
        self._is_green_mode_on = None
        self._is_on = None
        self._max_power_from_grid = None
        self._max_power_to_grid = None
        self._sell_energy_provider_id = None
        self._sell_price_schedule = None
        self._sell_price_formula = None
        self._sell_price_type = None
        self._is_periodic_full_charge_on = None
        self._periodic_full_charge_duration = None
        self._periodic_full_charge_interval = None
        self.discriminator = None
        self.battery_capacity = battery_capacity
        self.battery_costs = battery_costs
        self.battery_flow_restriction = battery_flow_restriction
        if battery_price is not None:
            self.battery_price = battery_price
        if buy_energy_provider_id is not None:
            self.buy_energy_provider_id = buy_energy_provider_id
        if buy_price_formula is not None:
            self.buy_price_formula = buy_price_formula
        if buy_price_schedule is not None:
            self.buy_price_schedule = buy_price_schedule
        self.buy_price_type = buy_price_type
        self.charge_power = charge_power
        self.discharge_power = discharge_power
        self.grid_sell = grid_sell
        if id_bidding_zone is not None:
            self.id_bidding_zone = id_bidding_zone
        if is_dess_soc_different is not None:
            self.is_dess_soc_different = is_dess_soc_different
        if is_green_mode_on is not None:
            self.is_green_mode_on = is_green_mode_on
        self.is_on = is_on
        self.max_power_from_grid = max_power_from_grid
        self.max_power_to_grid = max_power_to_grid
        if sell_energy_provider_id is not None:
            self.sell_energy_provider_id = sell_energy_provider_id
        if sell_price_schedule is not None:
            self.sell_price_schedule = sell_price_schedule
        if sell_price_formula is not None:
            self.sell_price_formula = sell_price_formula
        self.sell_price_type = sell_price_type
        if is_periodic_full_charge_on is not None:
            self.is_periodic_full_charge_on = is_periodic_full_charge_on
        if periodic_full_charge_duration is not None:
            self.periodic_full_charge_duration = periodic_full_charge_duration
        if periodic_full_charge_interval is not None:
            self.periodic_full_charge_interval = periodic_full_charge_interval

    @property
    def battery_capacity(self):
        """Gets the battery_capacity of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Battery capacity of the system in kWh  # noqa: E501

        :return: The battery_capacity of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        """Sets the battery_capacity of this IdSiteDynamicesssettingsBody.

        Battery capacity of the system in kWh  # noqa: E501

        :param battery_capacity: The battery_capacity of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if battery_capacity is None:
            raise ValueError("Invalid value for `battery_capacity`, must not be `None`")  # noqa: E501

        self._battery_capacity = battery_capacity

    @property
    def battery_costs(self):
        """Gets the battery_costs of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Battery cycle costs per kWh - You can calculate this value using this formula: battery price / (amount of battery cycles * battery capacity)  # noqa: E501

        :return: The battery_costs of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._battery_costs

    @battery_costs.setter
    def battery_costs(self, battery_costs):
        """Sets the battery_costs of this IdSiteDynamicesssettingsBody.

        Battery cycle costs per kWh - You can calculate this value using this formula: battery price / (amount of battery cycles * battery capacity)  # noqa: E501

        :param battery_costs: The battery_costs of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if battery_costs is None:
            raise ValueError("Invalid value for `battery_costs`, must not be `None`")  # noqa: E501

        self._battery_costs = battery_costs

    @property
    def battery_flow_restriction(self):
        """Gets the battery_flow_restriction of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Do you need to disable grid charging or discharging?  * `unrestricted` - No  * `noExport` - Disable discharging battery to grid  * `noImport` - Disable charging battery from grid   # noqa: E501

        :return: The battery_flow_restriction of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._battery_flow_restriction

    @battery_flow_restriction.setter
    def battery_flow_restriction(self, battery_flow_restriction):
        """Sets the battery_flow_restriction of this IdSiteDynamicesssettingsBody.

        Do you need to disable grid charging or discharging?  * `unrestricted` - No  * `noExport` - Disable discharging battery to grid  * `noImport` - Disable charging battery from grid   # noqa: E501

        :param battery_flow_restriction: The battery_flow_restriction of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if battery_flow_restriction is None:
            raise ValueError("Invalid value for `battery_flow_restriction`, must not be `None`")  # noqa: E501

        self._battery_flow_restriction = battery_flow_restriction

    @property
    def battery_price(self):
        """Gets the battery_price of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Battery price  # noqa: E501

        :return: The battery_price of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._battery_price

    @battery_price.setter
    def battery_price(self, battery_price):
        """Sets the battery_price of this IdSiteDynamicesssettingsBody.

        Battery price  # noqa: E501

        :param battery_price: The battery_price of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._battery_price = battery_price

    @property
    def buy_energy_provider_id(self):
        """Gets the buy_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Identifier of the energy provider for buying energy (see /energy-providers)  # noqa: E501

        :return: The buy_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._buy_energy_provider_id

    @buy_energy_provider_id.setter
    def buy_energy_provider_id(self, buy_energy_provider_id):
        """Sets the buy_energy_provider_id of this IdSiteDynamicesssettingsBody.

        Identifier of the energy provider for buying energy (see /energy-providers)  # noqa: E501

        :param buy_energy_provider_id: The buy_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._buy_energy_provider_id = buy_energy_provider_id

    @property
    def buy_price_formula(self):
        """Gets the buy_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501

        A formula to apply to the raw dynamic energy prices, where p is the raw price.  # noqa: E501

        :return: The buy_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._buy_price_formula

    @buy_price_formula.setter
    def buy_price_formula(self, buy_price_formula):
        """Sets the buy_price_formula of this IdSiteDynamicesssettingsBody.

        A formula to apply to the raw dynamic energy prices, where p is the raw price.  # noqa: E501

        :param buy_price_formula: The buy_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._buy_price_formula = buy_price_formula

    @property
    def buy_price_schedule(self):
        """Gets the buy_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501


        :return: The buy_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._buy_price_schedule

    @buy_price_schedule.setter
    def buy_price_schedule(self, buy_price_schedule):
        """Sets the buy_price_schedule of this IdSiteDynamicesssettingsBody.


        :param buy_price_schedule: The buy_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._buy_price_schedule = buy_price_schedule

    @property
    def buy_price_type(self):
        """Gets the buy_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you have dynamic buy prices  # noqa: E501

        :return: The buy_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._buy_price_type

    @buy_price_type.setter
    def buy_price_type(self, buy_price_type):
        """Sets the buy_price_type of this IdSiteDynamicesssettingsBody.

        Whether or not you have dynamic buy prices  # noqa: E501

        :param buy_price_type: The buy_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if buy_price_type is None:
            raise ValueError("Invalid value for `buy_price_type`, must not be `None`")  # noqa: E501

        self._buy_price_type = buy_price_type

    @property
    def charge_power(self):
        """Gets the charge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Maximum battery charging power in kW  # noqa: E501

        :return: The charge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._charge_power

    @charge_power.setter
    def charge_power(self, charge_power):
        """Sets the charge_power of this IdSiteDynamicesssettingsBody.

        Maximum battery charging power in kW  # noqa: E501

        :param charge_power: The charge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if charge_power is None:
            raise ValueError("Invalid value for `charge_power`, must not be `None`")  # noqa: E501

        self._charge_power = charge_power

    @property
    def discharge_power(self):
        """Gets the discharge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Maximum battery discharging power in kW  # noqa: E501

        :return: The discharge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._discharge_power

    @discharge_power.setter
    def discharge_power(self, discharge_power):
        """Sets the discharge_power of this IdSiteDynamicesssettingsBody.

        Maximum battery discharging power in kW  # noqa: E501

        :param discharge_power: The discharge_power of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if discharge_power is None:
            raise ValueError("Invalid value for `discharge_power`, must not be `None`")  # noqa: E501

        self._discharge_power = discharge_power

    @property
    def grid_sell(self):
        """Gets the grid_sell of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you can sell energy to the grid.  # noqa: E501

        :return: The grid_sell of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._grid_sell

    @grid_sell.setter
    def grid_sell(self, grid_sell):
        """Sets the grid_sell of this IdSiteDynamicesssettingsBody.

        Whether or not you can sell energy to the grid.  # noqa: E501

        :param grid_sell: The grid_sell of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if grid_sell is None:
            raise ValueError("Invalid value for `grid_sell`, must not be `None`")  # noqa: E501

        self._grid_sell = grid_sell

    @property
    def id_bidding_zone(self):
        """Gets the id_bidding_zone of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Identifier of the EU bidding zone (see /bidding-zones)  # noqa: E501

        :return: The id_bidding_zone of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._id_bidding_zone

    @id_bidding_zone.setter
    def id_bidding_zone(self, id_bidding_zone):
        """Sets the id_bidding_zone of this IdSiteDynamicesssettingsBody.

        Identifier of the EU bidding zone (see /bidding-zones)  # noqa: E501

        :param id_bidding_zone: The id_bidding_zone of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._id_bidding_zone = id_bidding_zone

    @property
    def is_dess_soc_different(self):
        """Gets the is_dess_soc_different of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you want to have a separate minimum SOC for Dynamic ESS  # noqa: E501

        :return: The is_dess_soc_different of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._is_dess_soc_different

    @is_dess_soc_different.setter
    def is_dess_soc_different(self, is_dess_soc_different):
        """Sets the is_dess_soc_different of this IdSiteDynamicesssettingsBody.

        Whether or not you want to have a separate minimum SOC for Dynamic ESS  # noqa: E501

        :param is_dess_soc_different: The is_dess_soc_different of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._is_dess_soc_different = is_dess_soc_different

    @property
    def is_green_mode_on(self):
        """Gets the is_green_mode_on of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you want to have green mode turned on for Dynamic ESS  # noqa: E501

        :return: The is_green_mode_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._is_green_mode_on

    @is_green_mode_on.setter
    def is_green_mode_on(self, is_green_mode_on):
        """Sets the is_green_mode_on of this IdSiteDynamicesssettingsBody.

        Whether or not you want to have green mode turned on for Dynamic ESS  # noqa: E501

        :param is_green_mode_on: The is_green_mode_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._is_green_mode_on = is_green_mode_on

    @property
    def is_on(self):
        """Gets the is_on of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you want to enable Dynamic ESS in VRM  # noqa: E501

        :return: The is_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._is_on

    @is_on.setter
    def is_on(self, is_on):
        """Sets the is_on of this IdSiteDynamicesssettingsBody.

        Whether or not you want to enable Dynamic ESS in VRM  # noqa: E501

        :param is_on: The is_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if is_on is None:
            raise ValueError("Invalid value for `is_on`, must not be `None`")  # noqa: E501

        self._is_on = is_on

    @property
    def max_power_from_grid(self):
        """Gets the max_power_from_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Maximum power from the grid in kW  # noqa: E501

        :return: The max_power_from_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._max_power_from_grid

    @max_power_from_grid.setter
    def max_power_from_grid(self, max_power_from_grid):
        """Sets the max_power_from_grid of this IdSiteDynamicesssettingsBody.

        Maximum power from the grid in kW  # noqa: E501

        :param max_power_from_grid: The max_power_from_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if max_power_from_grid is None:
            raise ValueError("Invalid value for `max_power_from_grid`, must not be `None`")  # noqa: E501

        self._max_power_from_grid = max_power_from_grid

    @property
    def max_power_to_grid(self):
        """Gets the max_power_to_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Maximum power to the grid in kW  # noqa: E501

        :return: The max_power_to_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._max_power_to_grid

    @max_power_to_grid.setter
    def max_power_to_grid(self, max_power_to_grid):
        """Sets the max_power_to_grid of this IdSiteDynamicesssettingsBody.

        Maximum power to the grid in kW  # noqa: E501

        :param max_power_to_grid: The max_power_to_grid of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if max_power_to_grid is None:
            raise ValueError("Invalid value for `max_power_to_grid`, must not be `None`")  # noqa: E501

        self._max_power_to_grid = max_power_to_grid

    @property
    def sell_energy_provider_id(self):
        """Gets the sell_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Identifier of the energy provider for buying energy (see /energy-providers)  # noqa: E501

        :return: The sell_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._sell_energy_provider_id

    @sell_energy_provider_id.setter
    def sell_energy_provider_id(self, sell_energy_provider_id):
        """Sets the sell_energy_provider_id of this IdSiteDynamicesssettingsBody.

        Identifier of the energy provider for buying energy (see /energy-providers)  # noqa: E501

        :param sell_energy_provider_id: The sell_energy_provider_id of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._sell_energy_provider_id = sell_energy_provider_id

    @property
    def sell_price_schedule(self):
        """Gets the sell_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501


        :return: The sell_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._sell_price_schedule

    @sell_price_schedule.setter
    def sell_price_schedule(self, sell_price_schedule):
        """Sets the sell_price_schedule of this IdSiteDynamicesssettingsBody.


        :param sell_price_schedule: The sell_price_schedule of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._sell_price_schedule = sell_price_schedule

    @property
    def sell_price_formula(self):
        """Gets the sell_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501

        A formula to apply to the raw dynamic energy prices, where p is the raw price.  # noqa: E501

        :return: The sell_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._sell_price_formula

    @sell_price_formula.setter
    def sell_price_formula(self, sell_price_formula):
        """Sets the sell_price_formula of this IdSiteDynamicesssettingsBody.

        A formula to apply to the raw dynamic energy prices, where p is the raw price.  # noqa: E501

        :param sell_price_formula: The sell_price_formula of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._sell_price_formula = sell_price_formula

    @property
    def sell_price_type(self):
        """Gets the sell_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not you have dynamic sell prices  # noqa: E501

        :return: The sell_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._sell_price_type

    @sell_price_type.setter
    def sell_price_type(self, sell_price_type):
        """Sets the sell_price_type of this IdSiteDynamicesssettingsBody.

        Whether or not you have dynamic sell prices  # noqa: E501

        :param sell_price_type: The sell_price_type of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """
        if sell_price_type is None:
            raise ValueError("Invalid value for `sell_price_type`, must not be `None`")  # noqa: E501

        self._sell_price_type = sell_price_type

    @property
    def is_periodic_full_charge_on(self):
        """Gets the is_periodic_full_charge_on of this IdSiteDynamicesssettingsBody.  # noqa: E501

        Whether or not do you want to periodically charge your battery to 100% in order to extend battery life  # noqa: E501

        :return: The is_periodic_full_charge_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._is_periodic_full_charge_on

    @is_periodic_full_charge_on.setter
    def is_periodic_full_charge_on(self, is_periodic_full_charge_on):
        """Sets the is_periodic_full_charge_on of this IdSiteDynamicesssettingsBody.

        Whether or not do you want to periodically charge your battery to 100% in order to extend battery life  # noqa: E501

        :param is_periodic_full_charge_on: The is_periodic_full_charge_on of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._is_periodic_full_charge_on = is_periodic_full_charge_on

    @property
    def periodic_full_charge_duration(self):
        """Gets the periodic_full_charge_duration of this IdSiteDynamicesssettingsBody.  # noqa: E501

        How many hours should your battery stay at 100% during the periodic recharge  # noqa: E501

        :return: The periodic_full_charge_duration of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._periodic_full_charge_duration

    @periodic_full_charge_duration.setter
    def periodic_full_charge_duration(self, periodic_full_charge_duration):
        """Sets the periodic_full_charge_duration of this IdSiteDynamicesssettingsBody.

        How many hours should your battery stay at 100% during the periodic recharge  # noqa: E501

        :param periodic_full_charge_duration: The periodic_full_charge_duration of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._periodic_full_charge_duration = periodic_full_charge_duration

    @property
    def periodic_full_charge_interval(self):
        """Gets the periodic_full_charge_interval of this IdSiteDynamicesssettingsBody.  # noqa: E501

        How often should the battery be fully charged (in days)  # noqa: E501

        :return: The periodic_full_charge_interval of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :rtype: object
        """
        return self._periodic_full_charge_interval

    @periodic_full_charge_interval.setter
    def periodic_full_charge_interval(self, periodic_full_charge_interval):
        """Sets the periodic_full_charge_interval of this IdSiteDynamicesssettingsBody.

        How often should the battery be fully charged (in days)  # noqa: E501

        :param periodic_full_charge_interval: The periodic_full_charge_interval of this IdSiteDynamicesssettingsBody.  # noqa: E501
        :type: object
        """

        self._periodic_full_charge_interval = periodic_full_charge_interval

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
        if issubclass(IdSiteDynamicesssettingsBody, dict):
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
        if not isinstance(other, IdSiteDynamicesssettingsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
