# Gnss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**coord_srid** | **int** |  | [optional] 
**coord_x** | **float** |  | [optional] 
**coord_y** | **float** |  | [optional] 
**data_base64** | **str** |  | [optional] 
**elevation_gps** | **float** |  | [optional] 
**filename** | **str** |  | [optional] 
**id** | **str** |  | 
**last_updated** | **datetime** |  | 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**original_filename** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 

## Example

```python
from sensormap_client.models.gnss import Gnss

# TODO update the JSON string below
json = "{}"
# create an instance of Gnss from a JSON string
gnss_instance = Gnss.from_json(json)
# print the JSON string representation of the object
print(Gnss.to_json())

# convert the object into a dict
gnss_dict = gnss_instance.to_dict()
# create an instance of Gnss from a dict
gnss_from_dict = Gnss.from_dict(gnss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


