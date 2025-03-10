# coding: utf-8

"""
    soil-api

    API for managing SOIL lab data

    The version of the OpenAPI document: 2.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sensormap_client.models.sensor_data import SensorData

class TestSensorData(unittest.TestCase):
    """SensorData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SensorData:
        """Test SensorData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SensorData`
        """
        model = SensorData()
        if include_optional:
            return SensorData(
                error_flat = 56,
                instrument_seq = 56,
                sensor_id = '',
                shake = 56,
                soil_moisture_count = 56,
                temperature_1 = 1.337,
                temperature_2 = 1.337,
                temperature_3 = 1.337,
                temperature_average = 1.337,
                time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SensorData(
                error_flat = 56,
                instrument_seq = 56,
                sensor_id = '',
                shake = 56,
                soil_moisture_count = 56,
                temperature_1 = 1.337,
                temperature_2 = 1.337,
                temperature_3 = 1.337,
                temperature_average = 1.337,
                time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testSensorData(self):
        """Test SensorData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
