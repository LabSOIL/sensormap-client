# Area


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**geom** | **object** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**name** | **str** |  | [optional] 
**plots** | [**List[Plot]**](Plot.md) |  | 
**project** | [**Project**](Project.md) |  | [optional] 
**project_id** | **str** |  | 
**sensor_profiles** | [**List[SensorProfile]**](SensorProfile.md) |  | 
**soil_profiles** | [**List[SoilProfile]**](SoilProfile.md) |  | 
**transects** | [**List[Transect]**](Transect.md) |  | 

## Example

```python
from sensormap_client.models.area import Area

# TODO update the JSON string below
json = "{}"
# create an instance of Area from a JSON string
area_instance = Area.from_json(json)
# print the JSON string representation of the object
print(Area.to_json())

# convert the object into a dict
area_dict = area_instance.to_dict()
# create an instance of Area from a dict
area_from_dict = Area.from_dict(area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


