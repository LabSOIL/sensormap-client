# InstrumentExperimentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | **str** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**device_filename** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**init_e** | **float** |  | [optional] 
**instrument_model** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**quiet_time** | **float** |  | [optional] 
**run_time** | **float** |  | [optional] 
**sample_interval** | **float** |  | [optional] 
**samples** | **int** |  | [optional] 
**sensitivity** | **float** |  | [optional] 

## Example

```python
from sensormap_client.models.instrument_experiment_update import InstrumentExperimentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperimentUpdate from a JSON string
instrument_experiment_update_instance = InstrumentExperimentUpdate.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperimentUpdate.to_json())

# convert the object into a dict
instrument_experiment_update_dict = instrument_experiment_update_instance.to_dict()
# create an instance of InstrumentExperimentUpdate from a dict
instrument_experiment_update_from_dict = InstrumentExperimentUpdate.from_dict(instrument_experiment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


