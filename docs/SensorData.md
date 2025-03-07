# SensorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_flat** | **int** |  | 
**instrument_seq** | **int** |  | 
**sensor_id** | **str** |  | 
**shake** | **int** |  | 
**soil_moisture_count** | **int** |  | 
**temperature_1** | **float** |  | 
**temperature_2** | **float** |  | 
**temperature_3** | **float** |  | 
**temperature_average** | **float** |  | 
**time_utc** | **datetime** |  | 

## Example

```python
from sensormap_client.models.sensor_data import SensorData

# TODO update the JSON string below
json = "{}"
# create an instance of SensorData from a JSON string
sensor_data_instance = SensorData.from_json(json)
# print the JSON string representation of the object
print(SensorData.to_json())

# convert the object into a dict
sensor_data_dict = sensor_data_instance.to_dict()
# create an instance of SensorData from a dict
sensor_data_from_dict = SensorData.from_dict(sensor_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


