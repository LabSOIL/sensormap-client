# TransectUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**nodes** | [**List[TransectNode]**](TransectNode.md) |  | [optional] 

## Example

```python
from sensormap_client.models.transect_update import TransectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TransectUpdate from a JSON string
transect_update_instance = TransectUpdate.from_json(json)
# print the JSON string representation of the object
print(TransectUpdate.to_json())

# convert the object into a dict
transect_update_dict = transect_update_instance.to_dict()
# create an instance of TransectUpdate from a dict
transect_update_from_dict = TransectUpdate.from_dict(transect_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


