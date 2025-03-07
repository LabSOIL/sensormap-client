# TransectNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**plot** | [**Plot**](Plot.md) |  | [optional] 
**plot_id** | **str** |  | 

## Example

```python
from sensormap_client.models.transect_node import TransectNode

# TODO update the JSON string below
json = "{}"
# create an instance of TransectNode from a JSON string
transect_node_instance = TransectNode.from_json(json)
# print the JSON string representation of the object
print(TransectNode.to_json())

# convert the object into a dict
transect_node_dict = transect_node_instance.to_dict()
# create an instance of TransectNode from a dict
transect_node_from_dict = TransectNode.from_dict(transect_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


