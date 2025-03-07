# SensorCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**data** | [**List[SensorData]**](SensorData.md) |  | [optional] 
**data_base64** | **str** |  | [optional] 
**data_from** | **datetime** |  | [optional] 
**data_to** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.sensor_create import SensorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SensorCreate from a JSON string
sensor_create_instance = SensorCreate.from_json(json)
# print the JSON string representation of the object
print(SensorCreate.to_json())

# convert the object into a dict
sensor_create_dict = sensor_create_instance.to_dict()
# create an instance of SensorCreate from a dict
sensor_create_from_dict = SensorCreate.from_dict(sensor_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


