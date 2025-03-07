# SoilProfileCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**aspect** | **str** |  | [optional] 
**coord_x** | **float** |  | 
**coord_y** | **float** |  | 
**coord_z** | **float** |  | 
**description_horizon** | **object** |  | [optional] 
**gradient** | **str** |  | 
**lythology_surficial_deposit** | **str** |  | [optional] 
**name** | **str** |  | 
**parent_material** | **float** |  | [optional] 
**photo** | **str** |  | [optional] 
**soil_diagram** | **str** |  | [optional] 
**soil_type_id** | **str** |  | 
**topography** | **str** |  | [optional] 
**vegetation_type** | **str** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.soil_profile_create import SoilProfileCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SoilProfileCreate from a JSON string
soil_profile_create_instance = SoilProfileCreate.from_json(json)
# print the JSON string representation of the object
print(SoilProfileCreate.to_json())

# convert the object into a dict
soil_profile_create_dict = soil_profile_create_instance.to_dict()
# create an instance of SoilProfileCreate from a dict
soil_profile_create_from_dict = SoilProfileCreate.from_dict(soil_profile_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


