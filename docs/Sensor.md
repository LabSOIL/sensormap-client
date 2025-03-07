# Sensor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**assignments** | [**List[SensorProfileAssignment]**](SensorProfileAssignment.md) |  | 
**comment** | **str** |  | [optional] 
**data** | [**List[SensorData]**](SensorData.md) |  | 
**data_base64** | **str** |  | [optional] 
**data_from** | **datetime** |  | [optional] 
**data_to** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**manufacturer** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.sensor import Sensor

# TODO update the JSON string below
json = "{}"
# create an instance of Sensor from a JSON string
sensor_instance = Sensor.from_json(json)
# print the JSON string representation of the object
print(Sensor.to_json())

# convert the object into a dict
sensor_dict = sensor_instance.to_dict()
# create an instance of Sensor from a dict
sensor_from_dict = Sensor.from_dict(sensor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


