# SensorProfileAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SensorData]**](SensorData.md) |  | [optional] 
**date_from** | **datetime** |  | 
**date_to** | **datetime** |  | 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**sensor** | [**Sensor**](Sensor.md) |  | [optional] 
**sensor_id** | **str** |  | 
**sensor_profile** | [**SensorProfile**](SensorProfile.md) |  | [optional] 
**sensorprofile_id** | **str** |  | 

## Example

```python
from sensormap_client.models.sensor_profile_assignment import SensorProfileAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfileAssignment from a JSON string
sensor_profile_assignment_instance = SensorProfileAssignment.from_json(json)
# print the JSON string representation of the object
print(SensorProfileAssignment.to_json())

# convert the object into a dict
sensor_profile_assignment_dict = sensor_profile_assignment_instance.to_dict()
# create an instance of SensorProfileAssignment from a dict
sensor_profile_assignment_from_dict = SensorProfileAssignment.from_dict(sensor_profile_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


