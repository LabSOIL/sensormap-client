# coding: utf-8

"""
    soil-api

    API for managing SOIL lab data

    The version of the OpenAPI document: 2.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sensormap_client.models.soil_type_update import SoilTypeUpdate

class TestSoilTypeUpdate(unittest.TestCase):
    """SoilTypeUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SoilTypeUpdate:
        """Test SoilTypeUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SoilTypeUpdate`
        """
        model = SoilTypeUpdate()
        if include_optional:
            return SoilTypeUpdate(
                description = '',
                image = '',
                name = ''
            )
        else:
            return SoilTypeUpdate(
        )
        """

    def testSoilTypeUpdate(self):
        """Test SoilTypeUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
