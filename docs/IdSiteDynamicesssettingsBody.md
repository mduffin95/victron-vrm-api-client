# IdSiteDynamicesssettingsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_capacity** | **object** | Battery capacity of the system in kWh | 
**battery_costs** | **object** | Battery cycle costs per kWh - You can calculate this value using this formula: battery price / (amount of battery cycles * battery capacity) | 
**battery_flow_restriction** | **object** | Do you need to disable grid charging or discharging?  * &#x60;unrestricted&#x60; - No  * &#x60;noExport&#x60; - Disable discharging battery to grid  * &#x60;noImport&#x60; - Disable charging battery from grid  | 
**battery_price** | **object** | Battery price | [optional] 
**buy_energy_provider_id** | **object** | Identifier of the energy provider for buying energy (see /energy-providers) | [optional] 
**buy_price_formula** | **object** | A formula to apply to the raw dynamic energy prices, where p is the raw price. | [optional] 
**buy_price_schedule** | **object** |  | [optional] 
**buy_price_type** | **object** | Whether or not you have dynamic buy prices | 
**charge_power** | **object** | Maximum battery charging power in kW | 
**discharge_power** | **object** | Maximum battery discharging power in kW | 
**grid_sell** | **object** | Whether or not you can sell energy to the grid. | 
**id_bidding_zone** | **object** | Identifier of the EU bidding zone (see /bidding-zones) | [optional] 
**is_dess_soc_different** | **object** | Whether or not you want to have a separate minimum SOC for Dynamic ESS | [optional] 
**is_green_mode_on** | **object** | Whether or not you want to have green mode turned on for Dynamic ESS | [optional] 
**is_on** | **object** | Whether or not you want to enable Dynamic ESS in VRM | 
**max_power_from_grid** | **object** | Maximum power from the grid in kW | 
**max_power_to_grid** | **object** | Maximum power to the grid in kW | 
**sell_energy_provider_id** | **object** | Identifier of the energy provider for buying energy (see /energy-providers) | [optional] 
**sell_price_schedule** | **object** |  | [optional] 
**sell_price_formula** | **object** | A formula to apply to the raw dynamic energy prices, where p is the raw price. | [optional] 
**sell_price_type** | **object** | Whether or not you have dynamic sell prices | 
**is_periodic_full_charge_on** | **object** | Whether or not do you want to periodically charge your battery to 100% in order to extend battery life | [optional] 
**periodic_full_charge_duration** | **object** | How many hours should your battery stay at 100% during the periodic recharge | [optional] 
**periodic_full_charge_interval** | **object** | How often should the battery be fully charged (in days) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

