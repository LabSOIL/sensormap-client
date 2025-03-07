# SensorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**assignments** | [**List[SensorProfileAssignment]**](SensorProfileAssignment.md) |  | 
**coord_srid** | **int** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**coord_z** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**name** | **str** |  | 

## Example

```python
from sensormap_client.models.sensor_profile import SensorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfile from a JSON string
sensor_profile_instance = SensorProfile.from_json(json)
# print the JSON string representation of the object
print(SensorProfile.to_json())

# convert the object into a dict
sensor_profile_dict = sensor_profile_instance.to_dict()
# create an instance of SensorProfile from a dict
sensor_profile_from_dict = SensorProfile.from_dict(sensor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


