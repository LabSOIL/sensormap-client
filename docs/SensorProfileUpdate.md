# SensorProfileUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**coord_z** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.sensor_profile_update import SensorProfileUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfileUpdate from a JSON string
sensor_profile_update_instance = SensorProfileUpdate.from_json(json)
# print the JSON string representation of the object
print(SensorProfileUpdate.to_json())

# convert the object into a dict
sensor_profile_update_dict = sensor_profile_update_instance.to_dict()
# create an instance of SensorProfileUpdate from a dict
sensor_profile_update_from_dict = SensorProfileUpdate.from_dict(sensor_profile_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


