# InstrumentExperiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[InstrumentExperimentChannel]**](InstrumentExperimentChannel.md) |  | 
**data_source** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**device_filename** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**id** | **str** |  | 
**init_e** | **float** |  | [optional] 
**instrument_model** | **str** |  | [optional] 
**last_updated** | **datetime** |  | 
**name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**quiet_time** | **float** |  | [optional] 
**run_time** | **float** |  | [optional] 
**sample_interval** | **float** |  | [optional] 
**samples** | **int** |  | [optional] 
**sensitivity** | **float** |  | [optional] 

## Example

```python
from sensormap_client.models.instrument_experiment import InstrumentExperiment

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperiment from a JSON string
instrument_experiment_instance = InstrumentExperiment.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperiment.to_json())

# convert the object into a dict
instrument_experiment_dict = instrument_experiment_instance.to_dict()
# create an instance of InstrumentExperiment from a dict
instrument_experiment_from_dict = InstrumentExperiment.from_dict(instrument_experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


