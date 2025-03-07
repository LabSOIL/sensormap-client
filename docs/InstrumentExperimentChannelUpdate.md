# InstrumentExperimentChannelUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_chosen_points** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_spline** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_values** | [**OneOf**](OneOf.md) |  | [optional] 
**channel_name** | **str** |  | [optional] 
**experiment_id** | **str** |  | [optional] 
**integral_chosen_pairs** | [**OneOf**](OneOf.md) |  | [optional] 
**integral_results** | [**OneOf**](OneOf.md) |  | [optional] 
**raw_values** | [**OneOf**](OneOf.md) |  | [optional] 
**time_values** | [**OneOf**](OneOf.md) |  | [optional] 

## Example

```python
from sensormap_client.models.instrument_experiment_channel_update import InstrumentExperimentChannelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperimentChannelUpdate from a JSON string
instrument_experiment_channel_update_instance = InstrumentExperimentChannelUpdate.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperimentChannelUpdate.to_json())

# convert the object into a dict
instrument_experiment_channel_update_dict = instrument_experiment_channel_update_instance.to_dict()
# create an instance of InstrumentExperimentChannelUpdate from a dict
instrument_experiment_channel_update_from_dict = InstrumentExperimentChannelUpdate.from_dict(instrument_experiment_channel_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


