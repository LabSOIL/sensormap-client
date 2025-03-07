# Plot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | [**Area**](Area.md) |  | [optional] 
**area_id** | **str** |  | 
**aspect** | **str** |  | [optional] 
**coord_srid** | **int** |  | 
**coord_x** | **float** |  | 
**coord_y** | **float** |  | 
**coord_z** | **float** |  | 
**created_on** | **date** |  | [optional] 
**gradient** | [**Gradientchoices**](Gradientchoices.md) |  | 
**id** | **str** |  | 
**image** | **str** |  | [optional] 
**last_updated** | **datetime** |  | 
**lithology** | **str** |  | [optional] 
**name** | **str** |  | 
**nearest_sensor_profiles** | [**List[ClosestSensorProfile]**](ClosestSensorProfile.md) |  | 
**samples** | [**List[PlotSample]**](PlotSample.md) |  | 
**topography** | **str** |  | [optional] 
**transects** | [**List[Transect]**](Transect.md) |  | 
**vegetation_type** | **str** |  | [optional] 
**weather** | **str** |  | [optional] 

## Example

```python
from sensormap_client.models.plot import Plot

# TODO update the JSON string below
json = "{}"
# create an instance of Plot from a JSON string
plot_instance = Plot.from_json(json)
# print the JSON string representation of the object
print(Plot.to_json())

# convert the object into a dict
plot_dict = plot_instance.to_dict()
# create an instance of Plot from a dict
plot_from_dict = Plot.from_dict(plot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


