# SoilTypeUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.soil_type_update import SoilTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SoilTypeUpdate from a JSON string
soil_type_update_instance = SoilTypeUpdate.from_json(json)
# print the JSON string representation of the object
print(SoilTypeUpdate.to_json())

# convert the object into a dict
soil_type_update_dict = soil_type_update_instance.to_dict()
# create an instance of SoilTypeUpdate from a dict
soil_type_update_from_dict = SoilTypeUpdate.from_dict(soil_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


