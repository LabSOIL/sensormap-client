# coding: utf-8

"""
    soil-api

    API for managing SOIL lab data

    The version of the OpenAPI document: 2.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sensormap_client.models.instrument_experiment_channel_create import InstrumentExperimentChannelCreate

class TestInstrumentExperimentChannelCreate(unittest.TestCase):
    """InstrumentExperimentChannelCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstrumentExperimentChannelCreate:
        """Test InstrumentExperimentChannelCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstrumentExperimentChannelCreate`
        """
        model = InstrumentExperimentChannelCreate()
        if include_optional:
            return InstrumentExperimentChannelCreate(
                baseline_chosen_points = None,
                baseline_spline = None,
                baseline_values = None,
                channel_name = '',
                experiment_id = '',
                integral_chosen_pairs = None,
                integral_results = None,
                raw_values = None,
                time_values = None
            )
        else:
            return InstrumentExperimentChannelCreate(
                channel_name = '',
                experiment_id = '',
        )
        """

    def testInstrumentExperimentChannelCreate(self):
        """Test InstrumentExperimentChannelCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
