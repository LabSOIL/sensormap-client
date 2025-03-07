# SensorProfileCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**coord_z** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from sensormap_client.models.sensor_profile_create import SensorProfileCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfileCreate from a JSON string
sensor_profile_create_instance = SensorProfileCreate.from_json(json)
# print the JSON string representation of the object
print(SensorProfileCreate.to_json())

# convert the object into a dict
sensor_profile_create_dict = sensor_profile_create_instance.to_dict()
# create an instance of SensorProfileCreate from a dict
sensor_profile_create_from_dict = SensorProfileCreate.from_dict(sensor_profile_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


