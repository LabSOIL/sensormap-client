# InstrumentExperimentChannel

The API model for an instrument experiment channel.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseline_chosen_points** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_spline** | [**OneOf**](OneOf.md) |  | [optional] 
**baseline_values** | [**OneOf**](OneOf.md) |  | [optional] 
**channel_name** | **str** |  | 
**experiment_id** | **str** |  | 
**id** | **str** |  | 
**integral_chosen_pairs** | [**OneOf**](OneOf.md) |  | [optional] 
**integral_results** | [**OneOf**](OneOf.md) |  | [optional] 
**raw_values** | [**OneOf**](OneOf.md) |  | [optional] 
**time_values** | [**OneOf**](OneOf.md) |  | [optional] 

## Example

```python
from sensormap_client.models.instrument_experiment_channel import InstrumentExperimentChannel

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperimentChannel from a JSON string
instrument_experiment_channel_instance = InstrumentExperimentChannel.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperimentChannel.to_json())

# convert the object into a dict
instrument_experiment_channel_dict = instrument_experiment_channel_instance.to_dict()
# create an instance of InstrumentExperimentChannel from a dict
instrument_experiment_channel_from_dict = InstrumentExperimentChannel.from_dict(instrument_experiment_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


