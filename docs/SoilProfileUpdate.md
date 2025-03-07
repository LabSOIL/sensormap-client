# SoilProfileUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | [optional] 
**aspect** | **str** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**coord_z** | **float** |  | [optional] 
**description_horizon** | **object** |  | [optional] 
**gradient** | **str** |  | [optional] 
**lythology_surficial_deposit** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_material** | **float** |  | [optional] 
**photo** | **str** |  | [optional] 
**soil_diagram** | **str** |  | [optional] 
**soil_type_id** | **str** |  | [optional] 
**topography** | **str** |  | [optional] 
**vegetation_type** | **str** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.soil_profile_update import SoilProfileUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SoilProfileUpdate from a JSON string
soil_profile_update_instance = SoilProfileUpdate.from_json(json)
# print the JSON string representation of the object
print(SoilProfileUpdate.to_json())

# convert the object into a dict
soil_profile_update_dict = soil_profile_update_instance.to_dict()
# create an instance of SoilProfileUpdate from a dict
soil_profile_update_from_dict = SoilProfileUpdate.from_dict(soil_profile_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


