# PlotCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area_id** | **str** |  | 
**aspect** | **str** |  | [optional] 
**coord_x** | **float** |  | 
**coord_y** | **float** |  | 
**coord_z** | **float** |  | 
**created_on** | **date** |  | [optional] 
**gradient** | [**Gradientchoices**](Gradientchoices.md) |  | [optional] 
**image** | **str** |  | [optional] 
**lithology** | **str** |  | [optional] 
**name** | **str** |  | 
**topography** | **str** |  | [optional] 
**vegetation_type** | **str** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.plot_create import PlotCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PlotCreate from a JSON string
plot_create_instance = PlotCreate.from_json(json)
# print the JSON string representation of the object
print(PlotCreate.to_json())

# convert the object into a dict
plot_create_dict = plot_create_instance.to_dict()
# create an instance of PlotCreate from a dict
plot_create_from_dict = PlotCreate.from_dict(plot_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


