# Transect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**area_id** | **str** |  | 
**date_created** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**name** | **str** |  | 
**nodes** | [**List[TransectNode]**](TransectNode.md) |  | 

## Example

```python
from sensormap_client.models.transect import Transect

# TODO update the JSON string below
json = "{}"
# create an instance of Transect from a JSON string
transect_instance = Transect.from_json(json)
# print the JSON string representation of the object
print(Transect.to_json())

# convert the object into a dict
transect_dict = transect_instance.to_dict()
# create an instance of Transect from a dict
transect_from_dict = Transect.from_dict(transect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


