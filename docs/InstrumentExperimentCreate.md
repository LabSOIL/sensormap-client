# InstrumentExperimentCreate


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
from sensormap_client.models.instrument_experiment_create import InstrumentExperimentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of InstrumentExperimentCreate from a JSON string
instrument_experiment_create_instance = InstrumentExperimentCreate.from_json(json)
# print the JSON string representation of the object
print(InstrumentExperimentCreate.to_json())

# convert the object into a dict
instrument_experiment_create_dict = instrument_experiment_create_instance.to_dict()
# create an instance of InstrumentExperimentCreate from a dict
instrument_experiment_create_from_dict = InstrumentExperimentCreate.from_dict(instrument_experiment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


