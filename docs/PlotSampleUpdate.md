# PlotSampleUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**al_ug_per_g** | **float** |  | [optional] 
**archea_per_g** | **float** |  | [optional] 
**bacteria_per_g** | **float** |  | [optional] 
**c** | **float** |  | [optional] 
**ca_ug_per_g** | **float** |  | [optional] 
**cl_ug_per_g** | **float** |  | [optional] 
**clay_percent** | **float** |  | [optional] 
**cn** | **float** |  | [optional] 
**fe_ug_per_g** | **float** |  | [optional] 
**fungi_per_g** | **float** |  | [optional] 
**k_ug_per_g** | **float** |  | [optional] 
**loi** | **float** |  | [optional] 
**lower_depth_cm** | **float** |  | [optional] 
**methanogens_per_g** | **float** |  | [optional] 
**methanotrophs_per_g** | **float** |  | [optional] 
**mfc** | **float** |  | [optional] 
**mg_ug_per_g** | **float** |  | [optional] 
**mn_ug_per_g** | **float** |  | [optional] 
**n** | **float** |  | [optional] 
**na_ug_per_g** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**p_ug_per_g** | **float** |  | [optional] 
**ph** | **float** |  | [optional] 
**plot_id** | **str** |  | [optional] 
**replicate** | **int** |  | [optional] 
**rh** | **float** |  | [optional] 
**s_ug_per_g** | **float** |  | [optional] 
**sample_weight** | **float** |  | [optional] 
**sand_percent** | **float** |  | [optional] 
**si_ug_per_g** | **float** |  | [optional] 
**silt_percent** | **float** |  | [optional] 
**subsample_replica_weight** | **float** |  | [optional] 
**subsample_weight** | **float** |  | [optional] 
**upper_depth_cm** | **float** |  | [optional] 

## Example

```python
from sensormap_client.models.plot_sample_update import PlotSampleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PlotSampleUpdate from a JSON string
plot_sample_update_instance = PlotSampleUpdate.from_json(json)
# print the JSON string representation of the object
print(PlotSampleUpdate.to_json())

# convert the object into a dict
plot_sample_update_dict = plot_sample_update_instance.to_dict()
# create an instance of PlotSampleUpdate from a dict
plot_sample_update_from_dict = PlotSampleUpdate.from_dict(plot_sample_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


