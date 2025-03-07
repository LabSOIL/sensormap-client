# SoilProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**aspect** | **str** |  | [optional] 
**coord_srid** | **int** |  | 
**coord_x** | **float** |  | 
**coord_y** | **float** |  | 
**coord_z** | **float** |  | 
**created_on** | **datetime** |  | [optional] 
**description_horizon** | **object** |  | [optional] 
**gradient** | **str** |  | 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
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
from sensormap_client.models.soil_profile import SoilProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SoilProfile from a JSON string
soil_profile_instance = SoilProfile.from_json(json)
# print the JSON string representation of the object
print(SoilProfile.to_json())

# convert the object into a dict
soil_profile_dict = soil_profile_instance.to_dict()
# create an instance of SoilProfile from a dict
soil_profile_from_dict = SoilProfile.from_dict(soil_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


