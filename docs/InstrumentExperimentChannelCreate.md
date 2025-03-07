# InstrumentExperimentChannelCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_chosen_points** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_spline** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_values** | [**OneOf**](OneOf.md) |  | [optional] 
**channel_name** | **str** |  | 
**experiment_id** | **str** |  | 
**integral_chosen_pairs** | [**OneOf**](OneOf.md) |  | [optional] 
**integral_results** | [**OneOf**](OneOf.md) |  | [optional] 
**raw_values** | [**OneOf**](OneOf.md) |  | [optional] 
**time_values** | [**OneOf**](OneOf.md) |  | [optional] 

## Example

```python
from sensormap_client.models.instrument_experiment_channel_create import InstrumentExperimentChannelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperimentChannelCreate from a JSON string
instrument_experiment_channel_create_instance = InstrumentExperimentChannelCreate.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperimentChannelCreate.to_json())

# convert the object into a dict
instrument_experiment_channel_create_dict = instrument_experiment_channel_create_instance.to_dict()
# create an instance of InstrumentExperimentChannelCreate from a dict
instrument_experiment_channel_create_from_dict = InstrumentExperimentChannelCreate.from_dict(instrument_experiment_channel_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


