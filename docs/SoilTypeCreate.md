# SoilTypeCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**image** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from sensormap_client.models.soil_type_create import SoilTypeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SoilTypeCreate from a JSON string
soil_type_create_instance = SoilTypeCreate.from_json(json)
# print the JSON string representation of the object
print(SoilTypeCreate.to_json())

# convert the object into a dict
soil_type_create_dict = soil_type_create_instance.to_dict()
# create an instance of SoilTypeCreate from a dict
soil_type_create_from_dict = SoilTypeCreate.from_dict(soil_type_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


