# SoilType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 
**image** | **str** |  | [optional] 
**last_updated** | **datetime** |  | 
**name** | **str** |  | 

## Example

```python
from sensormap_client.models.soil_type import SoilType

# TODO update the JSON string below
json = "{}"
# create an instance of SoilType from a JSON string
soil_type_instance = SoilType.from_json(json)
# print the JSON string representation of the object
print(SoilType.to_json())

# convert the object into a dict
soil_type_dict = soil_type_instance.to_dict()
# create an instance of SoilType from a dict
soil_type_from_dict = SoilType.from_dict(soil_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


