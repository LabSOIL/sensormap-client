# GnssCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**data_base64** | **str** |  | [optional] 
**elevation_gps** | **float** |  | [optional] 
**filename** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**original_filename** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from sensormap_client.models.gnss_create import GnssCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GnssCreate from a JSON string
gnss_create_instance = GnssCreate.from_json(json)
# print the JSON string representation of the object
print(GnssCreate.to_json())

# convert the object into a dict
gnss_create_dict = gnss_create_instance.to_dict()
# create an instance of GnssCreate from a dict
gnss_create_from_dict = GnssCreate.from_dict(gnss_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


