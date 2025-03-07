# TransectCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**nodes** | [**List[TransectNode]**](TransectNode.md) |  | [optional] 

## Example

```python
from sensormap_client.models.transect_create import TransectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TransectCreate from a JSON string
transect_create_instance = TransectCreate.from_json(json)
# print the JSON string representation of the object
print(TransectCreate.to_json())

# convert the object into a dict
transect_create_dict = transect_create_instance.to_dict()
# create an instance of TransectCreate from a dict
transect_create_from_dict = TransectCreate.from_dict(transect_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


