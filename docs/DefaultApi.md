# sensormap_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_one_area**](DefaultApi.md#create_one_area) | **POST** /api/areas | Create one area
[**create_one_assignment__sensor_profile**](DefaultApi.md#create_one_assignment__sensor_profile) | **POST** /api/sensor_profile_assignments | Create one assignment (sensor profile)
[**create_one_channel__instrument_experiment**](DefaultApi.md#create_one_channel__instrument_experiment) | **POST** /api/instrument_channels | Create one channel (instrument experiment)
[**create_one_experiment__lab_instrument**](DefaultApi.md#create_one_experiment__lab_instrument) | **POST** /api/instruments | Create one experiment (lab instrument)
[**create_one_gnss_recording**](DefaultApi.md#create_one_gnss_recording) | **POST** /api/gnss | Create one GNSS recording
[**create_one_plot**](DefaultApi.md#create_one_plot) | **POST** /api/plots | Create one plot
[**create_one_profile__sensor**](DefaultApi.md#create_one_profile__sensor) | **POST** /api/sensor_profiles | Create one profile (sensor)
[**create_one_project**](DefaultApi.md#create_one_project) | **POST** /api/projects | Create one project
[**create_one_sample__plot**](DefaultApi.md#create_one_sample__plot) | **POST** /api/plot_samples | Create one sample (plot)
[**create_one_sensor**](DefaultApi.md#create_one_sensor) | **POST** /api/sensors | Create one sensor
[**create_one_soil_profile**](DefaultApi.md#create_one_soil_profile) | **POST** /api/soil_profiles | Create one soil profile
[**create_one_soil_type**](DefaultApi.md#create_one_soil_type) | **POST** /api/soil_types | Create one soil type
[**create_one_transect**](DefaultApi.md#create_one_transect) | **POST** /api/transects | Create one transect
[**delete_many_areas**](DefaultApi.md#delete_many_areas) | **DELETE** /api/areas | Delete many areas
[**delete_many_assignments__sensor_profile**](DefaultApi.md#delete_many_assignments__sensor_profile) | **DELETE** /api/sensor_profile_assignments | Delete many assignments (sensor profile)
[**delete_many_channels__instrument_experiment**](DefaultApi.md#delete_many_channels__instrument_experiment) | **DELETE** /api/instrument_channels | Delete many channels (instrument experiment)
[**delete_many_experiments__lab_instrument**](DefaultApi.md#delete_many_experiments__lab_instrument) | **DELETE** /api/instruments | Delete many experiments (lab instrument)
[**delete_many_gnss_recordings**](DefaultApi.md#delete_many_gnss_recordings) | **DELETE** /api/gnss | Delete many GNSS recordings
[**delete_many_plots**](DefaultApi.md#delete_many_plots) | **DELETE** /api/plots | Delete many plots
[**delete_many_profiles__sensor**](DefaultApi.md#delete_many_profiles__sensor) | **DELETE** /api/sensor_profiles | Delete many profiles (sensor)
[**delete_many_projects**](DefaultApi.md#delete_many_projects) | **DELETE** /api/projects | Delete many projects
[**delete_many_samples__plot**](DefaultApi.md#delete_many_samples__plot) | **DELETE** /api/plot_samples | Delete many samples (plot)
[**delete_many_sensors**](DefaultApi.md#delete_many_sensors) | **DELETE** /api/sensors | Delete many sensors
[**delete_many_soil_profiles**](DefaultApi.md#delete_many_soil_profiles) | **DELETE** /api/soil_profiles | Delete many soil profiles
[**delete_many_soil_types**](DefaultApi.md#delete_many_soil_types) | **DELETE** /api/soil_types | Delete many soil types
[**delete_many_transects**](DefaultApi.md#delete_many_transects) | **DELETE** /api/transects | Delete many transects
[**delete_one_area**](DefaultApi.md#delete_one_area) | **DELETE** /api/areas/{id} | Delete one area
[**delete_one_assignment__sensor_profile**](DefaultApi.md#delete_one_assignment__sensor_profile) | **DELETE** /api/sensor_profile_assignments/{id} | Delete one assignment (sensor profile)
[**delete_one_channel__instrument_experiment**](DefaultApi.md#delete_one_channel__instrument_experiment) | **DELETE** /api/instrument_channels/{id} | Delete one channel (instrument experiment)
[**delete_one_experiment__lab_instrument**](DefaultApi.md#delete_one_experiment__lab_instrument) | **DELETE** /api/instruments/{id} | Delete one experiment (lab instrument)
[**delete_one_gnss_recording**](DefaultApi.md#delete_one_gnss_recording) | **DELETE** /api/gnss/{id} | Delete one GNSS recording
[**delete_one_plot**](DefaultApi.md#delete_one_plot) | **DELETE** /api/plots/{id} | Delete one plot
[**delete_one_profile__sensor**](DefaultApi.md#delete_one_profile__sensor) | **DELETE** /api/sensor_profiles/{id} | Delete one profile (sensor)
[**delete_one_project**](DefaultApi.md#delete_one_project) | **DELETE** /api/projects/{id} | Delete one project
[**delete_one_sample__plot**](DefaultApi.md#delete_one_sample__plot) | **DELETE** /api/plot_samples/{id} | Delete one sample (plot)
[**delete_one_sensor**](DefaultApi.md#delete_one_sensor) | **DELETE** /api/sensors/{id} | Delete one sensor
[**delete_one_soil_profile**](DefaultApi.md#delete_one_soil_profile) | **DELETE** /api/soil_profiles/{id} | Delete one soil profile
[**delete_one_soil_type**](DefaultApi.md#delete_one_soil_type) | **DELETE** /api/soil_types/{id} | Delete one soil type
[**delete_one_transect**](DefaultApi.md#delete_one_transect) | **DELETE** /api/transects/{id} | Delete one transect
[**delete_sensor_data**](DefaultApi.md#delete_sensor_data) | **DELETE** /api/sensors/{id}/data | Delete sensor data
[**get_all_areas**](DefaultApi.md#get_all_areas) | **GET** /api/areas | Get all areas
[**get_all_assignments__sensor_profile**](DefaultApi.md#get_all_assignments__sensor_profile) | **GET** /api/sensor_profile_assignments | Get all assignments (sensor profile)
[**get_all_channels__instrument_experiment**](DefaultApi.md#get_all_channels__instrument_experiment) | **GET** /api/instrument_channels | Get all channels (instrument experiment)
[**get_all_experiments__lab_instrument**](DefaultApi.md#get_all_experiments__lab_instrument) | **GET** /api/instruments | Get all experiments (lab instrument)
[**get_all_gnss_recordings**](DefaultApi.md#get_all_gnss_recordings) | **GET** /api/gnss | Get all GNSS recordings
[**get_all_plots**](DefaultApi.md#get_all_plots) | **GET** /api/plots | Get all plots
[**get_all_profiles__sensor**](DefaultApi.md#get_all_profiles__sensor) | **GET** /api/sensor_profiles | Get all profiles (sensor)
[**get_all_projects**](DefaultApi.md#get_all_projects) | **GET** /api/projects | Get all projects
[**get_all_samples__plot**](DefaultApi.md#get_all_samples__plot) | **GET** /api/plot_samples | Get all samples (plot)
[**get_all_sensors**](DefaultApi.md#get_all_sensors) | **GET** /api/sensors | Get all sensors
[**get_all_soil_profiles**](DefaultApi.md#get_all_soil_profiles) | **GET** /api/soil_profiles | Get all soil profiles
[**get_all_soil_types**](DefaultApi.md#get_all_soil_types) | **GET** /api/soil_types | Get all soil types
[**get_all_transects**](DefaultApi.md#get_all_transects) | **GET** /api/transects | Get all transects
[**get_filtered_data**](DefaultApi.md#get_filtered_data) | **GET** /api/instruments/{id}/filtered | Get filtered experiment (lab instrument) data
[**get_one**](DefaultApi.md#get_one) | **GET** /api/sensor_profiles/{id} | Get one profile (sensor)
[**get_one_area**](DefaultApi.md#get_one_area) | **GET** /api/areas/{id} | Get one area
[**get_one_assignment__sensor_profile**](DefaultApi.md#get_one_assignment__sensor_profile) | **GET** /api/sensor_profile_assignments/{id} | Get one assignment (sensor profile)
[**get_one_channel__instrument_experiment**](DefaultApi.md#get_one_channel__instrument_experiment) | **GET** /api/instrument_channels/{id} | Get one channel (instrument experiment)
[**get_one_experiment__lab_instrument**](DefaultApi.md#get_one_experiment__lab_instrument) | **GET** /api/instruments/{id} | Get one experiment (lab instrument)
[**get_one_gnss_recording**](DefaultApi.md#get_one_gnss_recording) | **GET** /api/gnss/{id} | Get one GNSS recording
[**get_one_plot**](DefaultApi.md#get_one_plot) | **GET** /api/plots/{id} | Get one plot
[**get_one_project**](DefaultApi.md#get_one_project) | **GET** /api/projects/{id} | Get one project
[**get_one_sample__plot**](DefaultApi.md#get_one_sample__plot) | **GET** /api/plot_samples/{id} | Get one sample (plot)
[**get_one_sensor**](DefaultApi.md#get_one_sensor) | **GET** /api/sensors/{id} | Get one sensor
[**get_one_soil_profile**](DefaultApi.md#get_one_soil_profile) | **GET** /api/soil_profiles/{id} | Get one soil profile
[**get_one_soil_type**](DefaultApi.md#get_one_soil_type) | **GET** /api/soil_types/{id} | Get one soil type
[**get_one_transect**](DefaultApi.md#get_one_transect) | **GET** /api/transects/{id} | Get one transect
[**get_raw_data**](DefaultApi.md#get_raw_data) | **GET** /api/instruments/{id}/raw | Get raw experiment (lab instrument) data
[**get_summary_data**](DefaultApi.md#get_summary_data) | **GET** /api/instruments/{id}/summary | Get summary data for experiment (lab instrument)
[**get_ui_config**](DefaultApi.md#get_ui_config) | **GET** /api/config | 
[**healthz**](DefaultApi.md#healthz) | **GET** /healthz | 
[**update_one_area**](DefaultApi.md#update_one_area) | **PUT** /api/areas/{id} | Update one area
[**update_one_assignment__sensor_profile**](DefaultApi.md#update_one_assignment__sensor_profile) | **PUT** /api/sensor_profile_assignments/{id} | Update one assignment (sensor profile)
[**update_one_channel__instrument_experiment**](DefaultApi.md#update_one_channel__instrument_experiment) | **PUT** /api/instrument_channels/{id} | Update one channel (instrument experiment)
[**update_one_experiment__lab_instrument**](DefaultApi.md#update_one_experiment__lab_instrument) | **PUT** /api/instruments/{id} | Update one experiment (lab instrument)
[**update_one_gnss_recording**](DefaultApi.md#update_one_gnss_recording) | **PUT** /api/gnss/{id} | Update one GNSS recording
[**update_one_plot**](DefaultApi.md#update_one_plot) | **PUT** /api/plots/{id} | Update one plot
[**update_one_profile__sensor**](DefaultApi.md#update_one_profile__sensor) | **PUT** /api/sensor_profiles/{id} | Update one profile (sensor)
[**update_one_project**](DefaultApi.md#update_one_project) | **PUT** /api/projects/{id} | Update one project
[**update_one_sample__plot**](DefaultApi.md#update_one_sample__plot) | **PUT** /api/plot_samples/{id} | Update one sample (plot)
[**update_one_sensor**](DefaultApi.md#update_one_sensor) | **PUT** /api/sensors/{id} | Update one sensor
[**update_one_soil_profile**](DefaultApi.md#update_one_soil_profile) | **PUT** /api/soil_profiles/{id} | Update one soil profile
[**update_one_soil_type**](DefaultApi.md#update_one_soil_type) | **PUT** /api/soil_types/{id} | Update one soil type
[**update_one_transect**](DefaultApi.md#update_one_transect) | **PUT** /api/transects/{id} | Update one transect


# **create_one_area**
> Area create_one_area(area_create)

Create one area

Creates a new area.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.area import Area
from sensormap_client.models.area_create import AreaCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    area_create = sensormap_client.AreaCreate() # AreaCreate | 

    try:
        # Create one area
        api_response = api_instance.create_one_area(area_create)
        print("The response of DefaultApi->create_one_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_create** | [**AreaCreate**](AreaCreate.md)|  | 

### Return type

[**Area**](Area.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_assignment__sensor_profile**
> SensorProfileAssignment create_one_assignment__sensor_profile(sensor_profile_assignment_create)

Create one assignment (sensor profile)

Creates a new assignment (sensor profile).

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile_assignment import SensorProfileAssignment
from sensormap_client.models.sensor_profile_assignment_create import SensorProfileAssignmentCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    sensor_profile_assignment_create = sensormap_client.SensorProfileAssignmentCreate() # SensorProfileAssignmentCreate | 

    try:
        # Create one assignment (sensor profile)
        api_response = api_instance.create_one_assignment__sensor_profile(sensor_profile_assignment_create)
        print("The response of DefaultApi->create_one_assignment__sensor_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_assignment__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_profile_assignment_create** | [**SensorProfileAssignmentCreate**](SensorProfileAssignmentCreate.md)|  | 

### Return type

[**SensorProfileAssignment**](SensorProfileAssignment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_channel__instrument_experiment**
> InstrumentExperimentChannel create_one_channel__instrument_experiment(instrument_experiment_channel_create)

Create one channel (instrument experiment)

Creates a new channel (instrument experiment).

This represents the data for a specific channel during the recording in the lab instrument.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment_channel import InstrumentExperimentChannel
from sensormap_client.models.instrument_experiment_channel_create import InstrumentExperimentChannelCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    instrument_experiment_channel_create = sensormap_client.InstrumentExperimentChannelCreate() # InstrumentExperimentChannelCreate | 

    try:
        # Create one channel (instrument experiment)
        api_response = api_instance.create_one_channel__instrument_experiment(instrument_experiment_channel_create)
        print("The response of DefaultApi->create_one_channel__instrument_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_channel__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_experiment_channel_create** | [**InstrumentExperimentChannelCreate**](InstrumentExperimentChannelCreate.md)|  | 

### Return type

[**InstrumentExperimentChannel**](InstrumentExperimentChannel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_experiment__lab_instrument**
> InstrumentExperiment create_one_experiment__lab_instrument(instrument_experiment_create)

Create one experiment (lab instrument)

Creates a new experiment (lab instrument).

This represents a specific lab experiment and coincides with the channel data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment import InstrumentExperiment
from sensormap_client.models.instrument_experiment_create import InstrumentExperimentCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    instrument_experiment_create = sensormap_client.InstrumentExperimentCreate() # InstrumentExperimentCreate | 

    try:
        # Create one experiment (lab instrument)
        api_response = api_instance.create_one_experiment__lab_instrument(instrument_experiment_create)
        print("The response of DefaultApi->create_one_experiment__lab_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_experiment__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_experiment_create** | [**InstrumentExperimentCreate**](InstrumentExperimentCreate.md)|  | 

### Return type

[**InstrumentExperiment**](InstrumentExperiment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_gnss_recording**
> Gnss create_one_gnss_recording(gnss_create)

Create one GNSS recording

Creates a new GNSS recording.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.gnss import Gnss
from sensormap_client.models.gnss_create import GnssCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    gnss_create = sensormap_client.GnssCreate() # GnssCreate | 

    try:
        # Create one GNSS recording
        api_response = api_instance.create_one_gnss_recording(gnss_create)
        print("The response of DefaultApi->create_one_gnss_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_gnss_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gnss_create** | [**GnssCreate**](GnssCreate.md)|  | 

### Return type

[**Gnss**](Gnss.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_plot**
> Plot create_one_plot(plot_create)

Create one plot

Creates a new plot.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot import Plot
from sensormap_client.models.plot_create import PlotCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    plot_create = sensormap_client.PlotCreate() # PlotCreate | 

    try:
        # Create one plot
        api_response = api_instance.create_one_plot(plot_create)
        print("The response of DefaultApi->create_one_plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plot_create** | [**PlotCreate**](PlotCreate.md)|  | 

### Return type

[**Plot**](Plot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_profile__sensor**
> SensorProfile create_one_profile__sensor(sensor_profile_create)

Create one profile (sensor)

Creates a new profile (sensor).

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile import SensorProfile
from sensormap_client.models.sensor_profile_create import SensorProfileCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    sensor_profile_create = sensormap_client.SensorProfileCreate() # SensorProfileCreate | 

    try:
        # Create one profile (sensor)
        api_response = api_instance.create_one_profile__sensor(sensor_profile_create)
        print("The response of DefaultApi->create_one_profile__sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_profile__sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_profile_create** | [**SensorProfileCreate**](SensorProfileCreate.md)|  | 

### Return type

[**SensorProfile**](SensorProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_project**
> Project create_one_project(project_create)

Create one project

Creates a new project.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.project import Project
from sensormap_client.models.project_create import ProjectCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    project_create = sensormap_client.ProjectCreate() # ProjectCreate | 

    try:
        # Create one project
        api_response = api_instance.create_one_project(project_create)
        print("The response of DefaultApi->create_one_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_sample__plot**
> PlotSample create_one_sample__plot(plot_sample_create)

Create one sample (plot)

Creates a new sample (plot).

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot_sample import PlotSample
from sensormap_client.models.plot_sample_create import PlotSampleCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    plot_sample_create = sensormap_client.PlotSampleCreate() # PlotSampleCreate | 

    try:
        # Create one sample (plot)
        api_response = api_instance.create_one_sample__plot(plot_sample_create)
        print("The response of DefaultApi->create_one_sample__plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_sample__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plot_sample_create** | [**PlotSampleCreate**](PlotSampleCreate.md)|  | 

### Return type

[**PlotSample**](PlotSample.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_sensor**
> Sensor create_one_sensor(sensor_create)

Create one sensor

Creates a new sensor.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor import Sensor
from sensormap_client.models.sensor_create import SensorCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    sensor_create = sensormap_client.SensorCreate() # SensorCreate | 

    try:
        # Create one sensor
        api_response = api_instance.create_one_sensor(sensor_create)
        print("The response of DefaultApi->create_one_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sensor_create** | [**SensorCreate**](SensorCreate.md)|  | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_soil_profile**
> SoilProfile create_one_soil_profile(soil_profile_create)

Create one soil profile

Creates a new soil profile.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_profile import SoilProfile
from sensormap_client.models.soil_profile_create import SoilProfileCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    soil_profile_create = sensormap_client.SoilProfileCreate() # SoilProfileCreate | 

    try:
        # Create one soil profile
        api_response = api_instance.create_one_soil_profile(soil_profile_create)
        print("The response of DefaultApi->create_one_soil_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_soil_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soil_profile_create** | [**SoilProfileCreate**](SoilProfileCreate.md)|  | 

### Return type

[**SoilProfile**](SoilProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_soil_type**
> SoilType create_one_soil_type(soil_type_create)

Create one soil type

Creates a new soil type.

A categorisation of soil that is associated to a soil profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_type import SoilType
from sensormap_client.models.soil_type_create import SoilTypeCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    soil_type_create = sensormap_client.SoilTypeCreate() # SoilTypeCreate | 

    try:
        # Create one soil type
        api_response = api_instance.create_one_soil_type(soil_type_create)
        print("The response of DefaultApi->create_one_soil_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_soil_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soil_type_create** | [**SoilTypeCreate**](SoilTypeCreate.md)|  | 

### Return type

[**SoilType**](SoilType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_transect**
> Transect create_one_transect(transect_create)

Create one transect

Creates a new transect.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.transect import Transect
from sensormap_client.models.transect_create import TransectCreate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    transect_create = sensormap_client.TransectCreate() # TransectCreate | 

    try:
        # Create one transect
        api_response = api_instance.create_one_transect(transect_create)
        print("The response of DefaultApi->create_one_transect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_one_transect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transect_create** | [**TransectCreate**](TransectCreate.md)|  | 

### Return type

[**Transect**](Transect.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Resource created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_areas**
> List[str] delete_many_areas(request_body)

Delete many areas

Deletes many areas by their IDs.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many areas
        api_response = api_instance.delete_many_areas(request_body)
        print("The response of DefaultApi->delete_many_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_assignments__sensor_profile**
> List[str] delete_many_assignments__sensor_profile(request_body)

Delete many assignments (sensor profile)

Deletes many assignments (sensor profile) by their IDs.

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many assignments (sensor profile)
        api_response = api_instance.delete_many_assignments__sensor_profile(request_body)
        print("The response of DefaultApi->delete_many_assignments__sensor_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_assignments__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_channels__instrument_experiment**
> List[str] delete_many_channels__instrument_experiment(request_body)

Delete many channels (instrument experiment)

Deletes many channels (instrument experiment) by their IDs.

This represents the data for a specific channel during the recording in the lab instrument.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many channels (instrument experiment)
        api_response = api_instance.delete_many_channels__instrument_experiment(request_body)
        print("The response of DefaultApi->delete_many_channels__instrument_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_channels__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_experiments__lab_instrument**
> List[str] delete_many_experiments__lab_instrument(request_body)

Delete many experiments (lab instrument)

Deletes many experiments (lab instrument) by their IDs.

This represents a specific lab experiment and coincides with the channel data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many experiments (lab instrument)
        api_response = api_instance.delete_many_experiments__lab_instrument(request_body)
        print("The response of DefaultApi->delete_many_experiments__lab_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_experiments__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_gnss_recordings**
> List[str] delete_many_gnss_recordings(request_body)

Delete many GNSS recordings

Deletes many GNSS recordings by their IDs.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many GNSS recordings
        api_response = api_instance.delete_many_gnss_recordings(request_body)
        print("The response of DefaultApi->delete_many_gnss_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_gnss_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_plots**
> List[str] delete_many_plots(request_body)

Delete many plots

Deletes many plots by their IDs.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many plots
        api_response = api_instance.delete_many_plots(request_body)
        print("The response of DefaultApi->delete_many_plots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_plots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_profiles__sensor**
> List[str] delete_many_profiles__sensor(request_body)

Delete many profiles (sensor)

Deletes many profiles (sensor) by their IDs.

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many profiles (sensor)
        api_response = api_instance.delete_many_profiles__sensor(request_body)
        print("The response of DefaultApi->delete_many_profiles__sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_profiles__sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_projects**
> List[str] delete_many_projects(request_body)

Delete many projects

Deletes many projects by their IDs.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many projects
        api_response = api_instance.delete_many_projects(request_body)
        print("The response of DefaultApi->delete_many_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_samples__plot**
> List[str] delete_many_samples__plot(request_body)

Delete many samples (plot)

Deletes many samples (plot) by their IDs.

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many samples (plot)
        api_response = api_instance.delete_many_samples__plot(request_body)
        print("The response of DefaultApi->delete_many_samples__plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_samples__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_sensors**
> List[str] delete_many_sensors(request_body)

Delete many sensors

Deletes many sensors by their IDs.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many sensors
        api_response = api_instance.delete_many_sensors(request_body)
        print("The response of DefaultApi->delete_many_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_soil_profiles**
> List[str] delete_many_soil_profiles(request_body)

Delete many soil profiles

Deletes many soil profiles by their IDs.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many soil profiles
        api_response = api_instance.delete_many_soil_profiles(request_body)
        print("The response of DefaultApi->delete_many_soil_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_soil_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_soil_types**
> List[str] delete_many_soil_types(request_body)

Delete many soil types

Deletes many soil types by their IDs.

A categorisation of soil that is associated to a soil profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many soil types
        api_response = api_instance.delete_many_soil_types(request_body)
        print("The response of DefaultApi->delete_many_soil_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_soil_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_transects**
> List[str] delete_many_transects(request_body)

Delete many transects

Deletes many transects by their IDs.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    request_body = ['request_body_example'] # List[str] | 

    try:
        # Delete many transects
        api_response = api_instance.delete_many_transects(request_body)
        print("The response of DefaultApi->delete_many_transects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_many_transects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resources deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_area**
> delete_one_area(id)

Delete one area

Deletes one area by its ID.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one area
        api_instance.delete_one_area(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_assignment__sensor_profile**
> delete_one_assignment__sensor_profile(id)

Delete one assignment (sensor profile)

Deletes one assignment (sensor profile) by its ID.

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one assignment (sensor profile)
        api_instance.delete_one_assignment__sensor_profile(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_assignment__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_channel__instrument_experiment**
> delete_one_channel__instrument_experiment(id)

Delete one channel (instrument experiment)

Deletes one channel (instrument experiment) by its ID.

This represents the data for a specific channel during the recording in the lab instrument.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one channel (instrument experiment)
        api_instance.delete_one_channel__instrument_experiment(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_channel__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_experiment__lab_instrument**
> delete_one_experiment__lab_instrument(id)

Delete one experiment (lab instrument)

Deletes one experiment (lab instrument) by its ID.

This represents a specific lab experiment and coincides with the channel data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one experiment (lab instrument)
        api_instance.delete_one_experiment__lab_instrument(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_experiment__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_gnss_recording**
> delete_one_gnss_recording(id)

Delete one GNSS recording

Deletes one GNSS recording by its ID.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one GNSS recording
        api_instance.delete_one_gnss_recording(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_gnss_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_plot**
> delete_one_plot(id)

Delete one plot

Deletes one plot by its ID.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one plot
        api_instance.delete_one_plot(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_profile__sensor**
> delete_one_profile__sensor(id)

Delete one profile (sensor)

Deletes one profile (sensor) by its ID.

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one profile (sensor)
        api_instance.delete_one_profile__sensor(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_profile__sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_project**
> delete_one_project(id)

Delete one project

Deletes one project by its ID.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one project
        api_instance.delete_one_project(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_sample__plot**
> delete_one_sample__plot(id)

Delete one sample (plot)

Deletes one sample (plot) by its ID.

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one sample (plot)
        api_instance.delete_one_sample__plot(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_sample__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_sensor**
> delete_one_sensor(id)

Delete one sensor

Deletes one sensor by its ID.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one sensor
        api_instance.delete_one_sensor(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_soil_profile**
> delete_one_soil_profile(id)

Delete one soil profile

Deletes one soil profile by its ID.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one soil profile
        api_instance.delete_one_soil_profile(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_soil_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_soil_type**
> delete_one_soil_type(id)

Delete one soil type

Deletes one soil type by its ID.

A categorisation of soil that is associated to a soil profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one soil type
        api_instance.delete_one_soil_type(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_soil_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_one_transect**
> delete_one_transect(id)

Delete one transect

Deletes one transect by its ID.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete one transect
        api_instance.delete_one_transect(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_one_transect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Resource deleted successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sensor_data**
> delete_sensor_data(id)

Delete sensor data

Deletes all data for a sensor by its given ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | Sensor ID

    try:
        # Delete sensor data
        api_instance.delete_sensor_data(id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_sensor_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Sensor ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sensor data deleted |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_areas**
> List[Area] get_all_areas(filter=filter, range=range, sort=sort)

Get all areas

Retrieves all areas.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

Additional sortable columns: 
- id

- name.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.area import Area
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{\"id\":\"550e8400-e29b-41d4-a716-446655440000\",\"name\":\"example\",\"q\":\"search text\"}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all areas
        api_response = api_instance.get_all_areas(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_areas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_areas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Area]**](Area.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assignments__sensor_profile**
> List[SensorProfileAssignment] get_all_assignments__sensor_profile(filter=filter, range=range, sort=sort)

Get all assignments (sensor profile)

Retrieves all assignments (sensor profile).

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

Additional sortable columns: 
- id

- sensor_id

- sensorprofile_id

- date_from

- date_to

- last_updated.

Additional filterable columns: .

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile_assignment import SensorProfileAssignment
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all assignments (sensor profile)
        api_response = api_instance.get_all_assignments__sensor_profile(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_assignments__sensor_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_assignments__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[SensorProfileAssignment]**](SensorProfileAssignment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channels__instrument_experiment**
> List[InstrumentExperimentChannel] get_all_channels__instrument_experiment(filter=filter, range=range, sort=sort)

Get all channels (instrument experiment)

Retrieves all channels (instrument experiment).

This represents the data for a specific channel during the recording in the lab instrument.

Additional sortable columns: 
- id

- channel_name.

Additional filterable columns: 
- channel_name.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment_channel import InstrumentExperimentChannel
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all channels (instrument experiment)
        api_response = api_instance.get_all_channels__instrument_experiment(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_channels__instrument_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_channels__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[InstrumentExperimentChannel]**](InstrumentExperimentChannel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_experiments__lab_instrument**
> List[InstrumentExperiment] get_all_experiments__lab_instrument(filter=filter, range=range, sort=sort)

Get all experiments (lab instrument)

Retrieves all experiments (lab instrument).

This represents a specific lab experiment and coincides with the channel data.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment import InstrumentExperiment
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all experiments (lab instrument)
        api_response = api_instance.get_all_experiments__lab_instrument(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_experiments__lab_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_experiments__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[InstrumentExperiment]**](InstrumentExperiment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_gnss_recordings**
> List[Gnss] get_all_gnss_recordings(filter=filter, range=range, sort=sort)

Get all GNSS recordings

Retrieves all GNSS recordings.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

Additional sortable columns: 
- id

- name

- last_updated

- coord_x

- coord_y

- coord_srid

- elevation_gps

- latitude

- longitude

- original_filename

- time.

Additional filterable columns: 
- name

- original_filename

- comment.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.gnss import Gnss
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all GNSS recordings
        api_response = api_instance.get_all_gnss_recordings(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_gnss_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_gnss_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Gnss]**](Gnss.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_plots**
> List[Plot] get_all_plots(filter=filter, range=range, sort=sort)

Get all plots

Retrieves all plots.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- vegetation_type

- topography

- aspect

- weather

- lithology.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot import Plot
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all plots
        api_response = api_instance.get_all_plots(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_plots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_plots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Plot]**](Plot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_profiles__sensor**
> List[SensorProfile] get_all_profiles__sensor(filter=filter, range=range, sort=sort)

Get all profiles (sensor)

Retrieves all profiles (sensor).

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile import SensorProfile
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all profiles (sensor)
        api_response = api_instance.get_all_profiles__sensor(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_profiles__sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_profiles__sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[SensorProfile]**](SensorProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> List[Project] get_all_projects(filter=filter, range=range, sort=sort)

Get all projects

Retrieves all projects.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

Additional sortable columns: 
- id

- name

- description

- color

- last_updated.

Additional filterable columns: 
- name

- description

- color.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.project import Project
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all projects
        api_response = api_instance.get_all_projects(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Project]**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_samples__plot**
> List[PlotSample] get_all_samples__plot(filter=filter, range=range, sort=sort)

Get all samples (plot)

Retrieves all samples (plot).

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

Additional sortable columns: 
- id

- name.

Additional filterable columns: 
- name.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot_sample import PlotSample
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all samples (plot)
        api_response = api_instance.get_all_samples__plot(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_samples__plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_samples__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[PlotSample]**](PlotSample.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sensors**
> List[Sensor] get_all_sensors(filter=filter, range=range, sort=sort)

Get all sensors

Retrieves all sensors.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor import Sensor
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all sensors
        api_response = api_instance.get_all_sensors(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_sensors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_sensors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Sensor]**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_soil_profiles**
> List[SoilProfile] get_all_soil_profiles(filter=filter, range=range, sort=sort)

Get all soil profiles

Retrieves all soil profiles.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- gradient

- weather

- topography

- vegetation_type

- aspect

- lythology_surficial_deposit.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_profile import SoilProfile
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all soil profiles
        api_response = api_instance.get_all_soil_profiles(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_soil_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_soil_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[SoilProfile]**](SoilProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_soil_types**
> List[SoilType] get_all_soil_types(filter=filter, range=range, sort=sort)

Get all soil types

Retrieves all soil types.

A categorisation of soil that is associated to a soil profile.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_type import SoilType
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all soil types
        api_response = api_instance.get_all_soil_types(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_soil_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_soil_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[SoilType]**](SoilType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_transects**
> List[Transect] get_all_transects(filter=filter, range=range, sort=sort)

Get all transects

Retrieves all transects.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

Additional sortable columns: 
- id

- name

- last_updated.

Additional filterable columns: 
- name

- description.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.transect import Transect
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    filter = '{id=550e8400-e29b-41d4-a716-446655440000, name=example, q=search text}' # str | JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: `{\"q\": \"search text\"}` - Filtering by a single ID: `{\"id\": \"550e8400-e29b-41d4-a716-446655440000\"}` - Filtering by multiple IDs: `{\"id\": [\"550e8400-e29b-41d4-a716-446655440000\", \"550e8400-e29b-41d4-a716-446655440001\"]}` - Filtering on other columns: `{\"name\": \"example\"}` (optional)
    range = '[0,9]' # str | Range for pagination in the format \"[start, end]\".  Example: `[0,9]` (optional)
    sort = '[\"id\", \"ASC\"]' # str | Sort order for the results in the format '[\"column\", \"order\"]'.  Example: `[\"id\", \"ASC\"]` (optional)

    try:
        # Get all transects
        api_response = api_instance.get_all_transects(filter=filter, range=range, sort=sort)
        print("The response of DefaultApi->get_all_transects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_all_transects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter for querying resources.  This parameter supports various filtering options: - Free text search: &#x60;{\&quot;q\&quot;: \&quot;search text\&quot;}&#x60; - Filtering by a single ID: &#x60;{\&quot;id\&quot;: \&quot;550e8400-e29b-41d4-a716-446655440000\&quot;}&#x60; - Filtering by multiple IDs: &#x60;{\&quot;id\&quot;: [\&quot;550e8400-e29b-41d4-a716-446655440000\&quot;, \&quot;550e8400-e29b-41d4-a716-446655440001\&quot;]}&#x60; - Filtering on other columns: &#x60;{\&quot;name\&quot;: \&quot;example\&quot;}&#x60; | [optional] 
 **range** | **str**| Range for pagination in the format \&quot;[start, end]\&quot;.  Example: &#x60;[0,9]&#x60; | [optional] 
 **sort** | **str**| Sort order for the results in the format &#39;[\&quot;column\&quot;, \&quot;order\&quot;]&#39;.  Example: &#x60;[\&quot;id\&quot;, \&quot;ASC\&quot;]&#x60; | [optional] 

### Return type

[**List[Transect]**](Transect.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of resources |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filtered_data**
> List[List[object]] get_filtered_data(id)

Get filtered experiment (lab instrument) data

Returns baseline-filtered CSV data built by slicing each channel’s baseline_values according to the 'start' and 'end' markers in each channel’s integral_results.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | Experiment ID

    try:
        # Get filtered experiment (lab instrument) data
        api_response = api_instance.get_filtered_data(id)
        print("The response of DefaultApi->get_filtered_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_filtered_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Experiment ID | 

### Return type

**List[List[object]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Filtered data found |  -  |
**404** | Experiment not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one**
> SensorProfile get_one(id, high_resolution)

Get one profile (sensor)

Retrieves one profile (sensor) by its ID.

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile import SensorProfile
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | SensorProfile ID
    high_resolution = True # bool | High resolution data flag

    try:
        # Get one profile (sensor)
        api_response = api_instance.get_one(id, high_resolution)
        print("The response of DefaultApi->get_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SensorProfile ID | 
 **high_resolution** | **bool**| High resolution data flag | 

### Return type

[**SensorProfile**](SensorProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SensorProfile found |  -  |
**404** | SensorProfile not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_area**
> Area get_one_area(id)

Get one area

Retrieves one area by its ID.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.area import Area
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one area
        api_response = api_instance.get_one_area(id)
        print("The response of DefaultApi->get_one_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Area**](Area.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_assignment__sensor_profile**
> SensorProfileAssignment get_one_assignment__sensor_profile(id)

Get one assignment (sensor profile)

Retrieves one assignment (sensor profile) by its ID.

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile_assignment import SensorProfileAssignment
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one assignment (sensor profile)
        api_response = api_instance.get_one_assignment__sensor_profile(id)
        print("The response of DefaultApi->get_one_assignment__sensor_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_assignment__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SensorProfileAssignment**](SensorProfileAssignment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_channel__instrument_experiment**
> InstrumentExperimentChannel get_one_channel__instrument_experiment(id)

Get one channel (instrument experiment)

Retrieves one channel (instrument experiment) by its ID.

This represents the data for a specific channel during the recording in the lab instrument.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment_channel import InstrumentExperimentChannel
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one channel (instrument experiment)
        api_response = api_instance.get_one_channel__instrument_experiment(id)
        print("The response of DefaultApi->get_one_channel__instrument_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_channel__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InstrumentExperimentChannel**](InstrumentExperimentChannel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_experiment__lab_instrument**
> InstrumentExperiment get_one_experiment__lab_instrument(id)

Get one experiment (lab instrument)

Retrieves one experiment (lab instrument) by its ID.

This represents a specific lab experiment and coincides with the channel data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment import InstrumentExperiment
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one experiment (lab instrument)
        api_response = api_instance.get_one_experiment__lab_instrument(id)
        print("The response of DefaultApi->get_one_experiment__lab_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_experiment__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**InstrumentExperiment**](InstrumentExperiment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_gnss_recording**
> Gnss get_one_gnss_recording(id)

Get one GNSS recording

Retrieves one GNSS recording by its ID.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.gnss import Gnss
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one GNSS recording
        api_response = api_instance.get_one_gnss_recording(id)
        print("The response of DefaultApi->get_one_gnss_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_gnss_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Gnss**](Gnss.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_plot**
> Plot get_one_plot(id)

Get one plot

Retrieves one plot by its ID.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot import Plot
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one plot
        api_response = api_instance.get_one_plot(id)
        print("The response of DefaultApi->get_one_plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Plot**](Plot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_project**
> Project get_one_project(id)

Get one project

Retrieves one project by its ID.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.project import Project
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one project
        api_response = api_instance.get_one_project(id)
        print("The response of DefaultApi->get_one_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_sample__plot**
> PlotSample get_one_sample__plot(id)

Get one sample (plot)

Retrieves one sample (plot) by its ID.

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot_sample import PlotSample
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one sample (plot)
        api_response = api_instance.get_one_sample__plot(id)
        print("The response of DefaultApi->get_one_sample__plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_sample__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PlotSample**](PlotSample.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_sensor**
> Sensor get_one_sensor(id, high_resolution)

Get one sensor

Retrieves one sensor by its ID.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor import Sensor
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | Sensor ID
    high_resolution = True # bool | High resolution data flag

    try:
        # Get one sensor
        api_response = api_instance.get_one_sensor(id, high_resolution)
        print("The response of DefaultApi->get_one_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Sensor ID | 
 **high_resolution** | **bool**| High resolution data flag | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sensor found |  -  |
**404** | Sensor not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_soil_profile**
> SoilProfile get_one_soil_profile(id)

Get one soil profile

Retrieves one soil profile by its ID.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_profile import SoilProfile
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one soil profile
        api_response = api_instance.get_one_soil_profile(id)
        print("The response of DefaultApi->get_one_soil_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_soil_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SoilProfile**](SoilProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_soil_type**
> SoilType get_one_soil_type(id)

Get one soil type

Retrieves one soil type by its ID.

A categorisation of soil that is associated to a soil profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_type import SoilType
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one soil type
        api_response = api_instance.get_one_soil_type(id)
        print("The response of DefaultApi->get_one_soil_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_soil_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SoilType**](SoilType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_one_transect**
> Transect get_one_transect(id)

Get one transect

Retrieves one transect by its ID.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.transect import Transect
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get one transect
        api_response = api_instance.get_one_transect(id)
        print("The response of DefaultApi->get_one_transect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_one_transect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Transect**](Transect.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested resource |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_data**
> List[List[str]] get_raw_data(id)

Get raw experiment (lab instrument) data

Returns CSV data (as JSON) built from the raw time and raw_values of each channel.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | Experiment ID

    try:
        # Get raw experiment (lab instrument) data
        api_response = api_instance.get_raw_data(id)
        print("The response of DefaultApi->get_raw_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_raw_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Experiment ID | 

### Return type

**List[List[str]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Raw data found |  -  |
**404** | Experiment not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_data**
> List[List[str]] get_summary_data(id)

Get summary data for experiment (lab instrument)

Returns CSV data (as JSON) built from each channel’s integral_results.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | Experiment ID

    try:
        # Get summary data for experiment (lab instrument)
        api_response = api_instance.get_summary_data(id)
        print("The response of DefaultApi->get_summary_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_summary_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Experiment ID | 

### Return type

**List[List[str]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary data found |  -  |
**404** | Experiment not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ui_config**
> str get_ui_config()

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)

    try:
        api_response = api_instance.get_ui_config()
        print("The response of DefaultApi->get_ui_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ui_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web UI configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthz**
> str healthz()

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)

    try:
        api_response = api_instance.healthz()
        print("The response of DefaultApi->healthz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->healthz: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kubernetes health check |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_area**
> Area update_one_area(id, area_update)

Update one area

Updates one area by its ID.

Areas are the main entities in the system. They are the main container for all other entities. They are associated with a project and contain plots, sensor profiles, soil profiles, and transects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.area import Area
from sensormap_client.models.area_update import AreaUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    area_update = sensormap_client.AreaUpdate() # AreaUpdate | 

    try:
        # Update one area
        api_response = api_instance.update_one_area(id, area_update)
        print("The response of DefaultApi->update_one_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **area_update** | [**AreaUpdate**](AreaUpdate.md)|  | 

### Return type

[**Area**](Area.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_assignment__sensor_profile**
> SensorProfileAssignment update_one_assignment__sensor_profile(id, sensor_profile_assignment_update)

Update one assignment (sensor profile)

Updates one assignment (sensor profile) by its ID.

This is a record of a sensor being assigned to a sensor profile for a specific time period, should a sensor move or be changed over time. It therefore helps piece the data together for a sensor profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile_assignment import SensorProfileAssignment
from sensormap_client.models.sensor_profile_assignment_update import SensorProfileAssignmentUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    sensor_profile_assignment_update = sensormap_client.SensorProfileAssignmentUpdate() # SensorProfileAssignmentUpdate | 

    try:
        # Update one assignment (sensor profile)
        api_response = api_instance.update_one_assignment__sensor_profile(id, sensor_profile_assignment_update)
        print("The response of DefaultApi->update_one_assignment__sensor_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_assignment__sensor_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sensor_profile_assignment_update** | [**SensorProfileAssignmentUpdate**](SensorProfileAssignmentUpdate.md)|  | 

### Return type

[**SensorProfileAssignment**](SensorProfileAssignment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_channel__instrument_experiment**
> InstrumentExperimentChannel update_one_channel__instrument_experiment(id, instrument_experiment_channel_update)

Update one channel (instrument experiment)

Updates one channel (instrument experiment) by its ID.

This represents the data for a specific channel during the recording in the lab instrument.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment_channel import InstrumentExperimentChannel
from sensormap_client.models.instrument_experiment_channel_update import InstrumentExperimentChannelUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    instrument_experiment_channel_update = sensormap_client.InstrumentExperimentChannelUpdate() # InstrumentExperimentChannelUpdate | 

    try:
        # Update one channel (instrument experiment)
        api_response = api_instance.update_one_channel__instrument_experiment(id, instrument_experiment_channel_update)
        print("The response of DefaultApi->update_one_channel__instrument_experiment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_channel__instrument_experiment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **instrument_experiment_channel_update** | [**InstrumentExperimentChannelUpdate**](InstrumentExperimentChannelUpdate.md)|  | 

### Return type

[**InstrumentExperimentChannel**](InstrumentExperimentChannel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_experiment__lab_instrument**
> InstrumentExperiment update_one_experiment__lab_instrument(id, instrument_experiment_update)

Update one experiment (lab instrument)

Updates one experiment (lab instrument) by its ID.

This represents a specific lab experiment and coincides with the channel data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.instrument_experiment import InstrumentExperiment
from sensormap_client.models.instrument_experiment_update import InstrumentExperimentUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    instrument_experiment_update = sensormap_client.InstrumentExperimentUpdate() # InstrumentExperimentUpdate | 

    try:
        # Update one experiment (lab instrument)
        api_response = api_instance.update_one_experiment__lab_instrument(id, instrument_experiment_update)
        print("The response of DefaultApi->update_one_experiment__lab_instrument:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_experiment__lab_instrument: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **instrument_experiment_update** | [**InstrumentExperimentUpdate**](InstrumentExperimentUpdate.md)|  | 

### Return type

[**InstrumentExperiment**](InstrumentExperiment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_gnss_recording**
> Gnss update_one_gnss_recording(id, gnss_update)

Update one GNSS recording

Updates one GNSS recording by its ID.

GNSS recordings taken from the field are stored here to help propagate to other resources (soil profiles, plots, sensor profiles, etc.)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.gnss import Gnss
from sensormap_client.models.gnss_update import GnssUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    gnss_update = sensormap_client.GnssUpdate() # GnssUpdate | 

    try:
        # Update one GNSS recording
        api_response = api_instance.update_one_gnss_recording(id, gnss_update)
        print("The response of DefaultApi->update_one_gnss_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_gnss_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **gnss_update** | [**GnssUpdate**](GnssUpdate.md)|  | 

### Return type

[**Gnss**](Gnss.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_plot**
> Plot update_one_plot(id, plot_update)

Update one plot

Updates one plot by its ID.

This is a record of a plot, which is a specific area of land that is being studied. It is used to collect samples and data for analysis.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot import Plot
from sensormap_client.models.plot_update import PlotUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    plot_update = sensormap_client.PlotUpdate() # PlotUpdate | 

    try:
        # Update one plot
        api_response = api_instance.update_one_plot(id, plot_update)
        print("The response of DefaultApi->update_one_plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **plot_update** | [**PlotUpdate**](PlotUpdate.md)|  | 

### Return type

[**Plot**](Plot.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_profile__sensor**
> SensorProfile update_one_profile__sensor(id, sensor_profile_update)

Update one profile (sensor)

Updates one profile (sensor) by its ID.

A sensor profile represents a geographical location where a sensor is placed. The assignments that belong to it define the time periods for which sensor is active and the data it collects.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor_profile import SensorProfile
from sensormap_client.models.sensor_profile_update import SensorProfileUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    sensor_profile_update = sensormap_client.SensorProfileUpdate() # SensorProfileUpdate | 

    try:
        # Update one profile (sensor)
        api_response = api_instance.update_one_profile__sensor(id, sensor_profile_update)
        print("The response of DefaultApi->update_one_profile__sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_profile__sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sensor_profile_update** | [**SensorProfileUpdate**](SensorProfileUpdate.md)|  | 

### Return type

[**SensorProfile**](SensorProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_project**
> Project update_one_project(id, project_update)

Update one project

Updates one project by its ID.

This resource allows the data hierarchically beneath each area to be allocated to a specific project. This is useful for grouping data together for analysis. The colour provides a visual representation of the project in the UI.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.project import Project
from sensormap_client.models.project_update import ProjectUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    project_update = sensormap_client.ProjectUpdate() # ProjectUpdate | 

    try:
        # Update one project
        api_response = api_instance.update_one_project(id, project_update)
        print("The response of DefaultApi->update_one_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_sample__plot**
> PlotSample update_one_sample__plot(id, plot_sample_update)

Update one sample (plot)

Updates one sample (plot) by its ID.

This resource represents a sample taken from a plot. It contains the data collected from the sample, such as pH, organic carbon, nitrogen, and other soil properties.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.plot_sample import PlotSample
from sensormap_client.models.plot_sample_update import PlotSampleUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    plot_sample_update = sensormap_client.PlotSampleUpdate() # PlotSampleUpdate | 

    try:
        # Update one sample (plot)
        api_response = api_instance.update_one_sample__plot(id, plot_sample_update)
        print("The response of DefaultApi->update_one_sample__plot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_sample__plot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **plot_sample_update** | [**PlotSampleUpdate**](PlotSampleUpdate.md)|  | 

### Return type

[**PlotSample**](PlotSample.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_sensor**
> Sensor update_one_sensor(id, sensor_update)

Update one sensor

Updates one sensor by its ID.

A sensor is a physical device placed in the field that collects moisture and temperature data that can then be associated with a plot (via a sensor profile and its assignments).

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.sensor import Sensor
from sensormap_client.models.sensor_update import SensorUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    sensor_update = sensormap_client.SensorUpdate() # SensorUpdate | 

    try:
        # Update one sensor
        api_response = api_instance.update_one_sensor(id, sensor_update)
        print("The response of DefaultApi->update_one_sensor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_sensor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sensor_update** | [**SensorUpdate**](SensorUpdate.md)|  | 

### Return type

[**Sensor**](Sensor.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_soil_profile**
> SoilProfile update_one_soil_profile(id, soil_profile_update)

Update one soil profile

Updates one soil profile by its ID.

Soil profiles are a collection of soil horizons that describe the soil at a specific location.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_profile import SoilProfile
from sensormap_client.models.soil_profile_update import SoilProfileUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    soil_profile_update = sensormap_client.SoilProfileUpdate() # SoilProfileUpdate | 

    try:
        # Update one soil profile
        api_response = api_instance.update_one_soil_profile(id, soil_profile_update)
        print("The response of DefaultApi->update_one_soil_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_soil_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **soil_profile_update** | [**SoilProfileUpdate**](SoilProfileUpdate.md)|  | 

### Return type

[**SoilProfile**](SoilProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_soil_type**
> SoilType update_one_soil_type(id, soil_type_update)

Update one soil type

Updates one soil type by its ID.

A categorisation of soil that is associated to a soil profile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.soil_type import SoilType
from sensormap_client.models.soil_type_update import SoilTypeUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    soil_type_update = sensormap_client.SoilTypeUpdate() # SoilTypeUpdate | 

    try:
        # Update one soil type
        api_response = api_instance.update_one_soil_type(id, soil_type_update)
        print("The response of DefaultApi->update_one_soil_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_soil_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **soil_type_update** | [**SoilTypeUpdate**](SoilTypeUpdate.md)|  | 

### Return type

[**SoilType**](SoilType.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_one_transect**
> Transect update_one_transect(id, transect_update)

Update one transect

Updates one transect by its ID.

This resource manages several plots within an area along a transect line in order to handle a specific methodology in the project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import sensormap_client
from sensormap_client.models.transect import Transect
from sensormap_client.models.transect_update import TransectUpdate
from sensormap_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sensormap_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = sensormap_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sensormap_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sensormap_client.DefaultApi(api_client)
    id = 'id_example' # str | 
    transect_update = sensormap_client.TransectUpdate() # TransectUpdate | 

    try:
        # Update one transect
        api_response = api_instance.update_one_transect(id, transect_update)
        print("The response of DefaultApi->update_one_transect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_one_transect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **transect_update** | [**TransectUpdate**](TransectUpdate.md)|  | 

### Return type

[**Transect**](Transect.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource updated successfully |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

