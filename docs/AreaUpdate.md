# AreaUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.area_update import AreaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AreaUpdate from a JSON string
area_update_instance = AreaUpdate.from_json(json)
# print the JSON string representation of the object
print(AreaUpdate.to_json())

# convert the object into a dict
area_update_dict = area_update_instance.to_dict()
# create an instance of AreaUpdate from a dict
area_update_from_dict = AreaUpdate.from_dict(area_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


