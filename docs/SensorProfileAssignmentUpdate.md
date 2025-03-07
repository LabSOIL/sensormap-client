# SensorProfileAssignmentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SensorData]**](SensorData.md) |  | [optional] 
**date_from** | **datetime** |  | [optional] 
**date_to** | **datetime** |  | [optional] 
**sensor_id** | **str** |  | [optional] 
**sensorprofile_id** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.sensor_profile_assignment_update import SensorProfileAssignmentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfileAssignmentUpdate from a JSON string
sensor_profile_assignment_update_instance = SensorProfileAssignmentUpdate.from_json(json)
# print the JSON string representation of the object
print(SensorProfileAssignmentUpdate.to_json())

# convert the object into a dict
sensor_profile_assignment_update_dict = sensor_profile_assignment_update_instance.to_dict()
# create an instance of SensorProfileAssignmentUpdate from a dict
sensor_profile_assignment_update_from_dict = SensorProfileAssignmentUpdate.from_dict(sensor_profile_assignment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


