# SensorProfileAssignmentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SensorData]**](SensorData.md) |  | [optional] 
**date_from** | **datetime** |  | 
**date_to** | **datetime** |  | 
**sensor_id** | **str** |  | 
**sensorprofile_id** | **str** |  | 

## Example

```python
from sensormap_client.models.sensor_profile_assignment_create import SensorProfileAssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SensorProfileAssignmentCreate from a JSON string
sensor_profile_assignment_create_instance = SensorProfileAssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(SensorProfileAssignmentCreate.to_json())

# convert the object into a dict
sensor_profile_assignment_create_dict = sensor_profile_assignment_create_instance.to_dict()
# create an instance of SensorProfileAssignmentCreate from a dict
sensor_profile_assignment_create_from_dict = SensorProfileAssignmentCreate.from_dict(sensor_profile_assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


