# ClosestSensorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** |  | 
**elevation_difference** | **float** |  | 
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from sensormap_client.models.closest_sensor_profile import ClosestSensorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClosestSensorProfile from a JSON string
closest_sensor_profile_instance = ClosestSensorProfile.from_json(json)
# print the JSON string representation of the object
print(ClosestSensorProfile.to_json())

# convert the object into a dict
closest_sensor_profile_dict = closest_sensor_profile_instance.to_dict()
# create an instance of ClosestSensorProfile from a dict
closest_sensor_profile_from_dict = ClosestSensorProfile.from_dict(closest_sensor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


