# GnssUpdate


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
from sensormap_client.models.gnss_update import GnssUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GnssUpdate from a JSON string
gnss_update_instance = GnssUpdate.from_json(json)
# print the JSON string representation of the object
print(GnssUpdate.to_json())

# convert the object into a dict
gnss_update_dict = gnss_update_instance.to_dict()
# create an instance of GnssUpdate from a dict
gnss_update_from_dict = GnssUpdate.from_dict(gnss_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


