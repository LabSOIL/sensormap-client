# PlotUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | [optional] 
**aspect** | **str** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**coord_z** | **float** |  | [optional] 
**created_on** | **date** |  | [optional] 
**gradient** | [**Gradientchoices**](Gradientchoices.md) |  | [optional] 
**image** | **str** |  | [optional] 
**lithology** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**topography** | **str** |  | [optional] 
**vegetation_type** | **str** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.plot_update import PlotUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PlotUpdate from a JSON string
plot_update_instance = PlotUpdate.from_json(json)
# print the JSON string representation of the object
print(PlotUpdate.to_json())

# convert the object into a dict
plot_update_dict = plot_update_instance.to_dict()
# create an instance of PlotUpdate from a dict
plot_update_from_dict = PlotUpdate.from_dict(plot_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


