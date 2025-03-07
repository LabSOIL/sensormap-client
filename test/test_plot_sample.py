# coding: utf-8

"""
    soil-api

    API for managing SOIL lab data

    The version of the OpenAPI document: 2.1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sensormap_client.models.plot_sample import PlotSample

class TestPlotSample(unittest.TestCase):
    """PlotSample unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlotSample:
        """Test PlotSample
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlotSample`
        """
        model = PlotSample()
        if include_optional:
            return PlotSample(
                al_ug_per_g = 1.337,
                archea_per_g = 1.337,
                bacteria_per_g = 1.337,
                c = 1.337,
                ca_ug_per_g = 1.337,
                cl_ug_per_g = 1.337,
                clay_percent = 1.337,
                cn = 1.337,
                created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                fe_ug_per_g = 1.337,
                fungi_per_g = 1.337,
                id = '',
                k_ug_per_g = 1.337,
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                loi = 1.337,
                lower_depth_cm = 1.337,
                methanogens_per_g = 1.337,
                methanotrophs_per_g = 1.337,
                mfc = 1.337,
                mg_ug_per_g = 1.337,
                mn_ug_per_g = 1.337,
                n = 1.337,
                na_ug_per_g = 1.337,
                name = '',
                p_ug_per_g = 1.337,
                ph = 1.337,
                plot = sensormap_client.models.plot.Plot(
                    area = sensormap_client.models.area.Area(
                        description = '', 
                        geom = null, 
                        id = '', 
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        plots = [
                            sensormap_client.models.plot.Plot(
                                area_id = '', 
                                aspect = '', 
                                coord_srid = 56, 
                                coord_x = 1.337, 
                                coord_y = 1.337, 
                                coord_z = 1.337, 
                                created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                gradient = 'flat', 
                                id = '', 
                                image = '', 
                                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                lithology = '', 
                                name = '', 
                                nearest_sensor_profiles = [
                                    sensormap_client.models.closest_sensor_profile.ClosestSensorProfile(
                                        distance = 1.337, 
                                        elevation_difference = 1.337, 
                                        id = '', 
                                        name = '', )
                                    ], 
                                samples = [
                                    sensormap_client.models.plot_sample.PlotSample(
                                        al_ug_per_g = 1.337, 
                                        archea_per_g = 1.337, 
                                        bacteria_per_g = 1.337, 
                                        c = 1.337, 
                                        ca_ug_per_g = 1.337, 
                                        cl_ug_per_g = 1.337, 
                                        clay_percent = 1.337, 
                                        cn = 1.337, 
                                        created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                        fe_ug_per_g = 1.337, 
                                        fungi_per_g = 1.337, 
                                        id = '', 
                                        k_ug_per_g = 1.337, 
                                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        loi = 1.337, 
                                        lower_depth_cm = 1.337, 
                                        methanogens_per_g = 1.337, 
                                        methanotrophs_per_g = 1.337, 
                                        mfc = 1.337, 
                                        mg_ug_per_g = 1.337, 
                                        mn_ug_per_g = 1.337, 
                                        n = 1.337, 
                                        na_ug_per_g = 1.337, 
                                        name = '', 
                                        p_ug_per_g = 1.337, 
                                        ph = 1.337, 
                                        plot_id = '', 
                                        replicate = 56, 
                                        rh = 1.337, 
                                        s_ug_per_g = 1.337, 
                                        sample_weight = 1.337, 
                                        sand_percent = 1.337, 
                                        si_ug_per_g = 1.337, 
                                        silt_percent = 1.337, 
                                        subsample_replica_weight = 1.337, 
                                        subsample_weight = 1.337, 
                                        upper_depth_cm = 1.337, )
                                    ], 
                                topography = '', 
                                transects = [
                                    sensormap_client.models.transect.Transect(
                                        area_id = '', 
                                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        description = '', 
                                        id = '', 
                                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        name = '', 
                                        nodes = [
                                            sensormap_client.models.transect_node.TransectNode(
                                                order = 56, 
                                                plot_id = '', )
                                            ], )
                                    ], 
                                vegetation_type = '', 
                                weather = '', )
                            ], 
                        project = sensormap_client.models.project.Project(
                            color = '', 
                            description = '', 
                            id = '', 
                            last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            name = '', ), 
                        project_id = '', 
                        sensor_profiles = [
                            sensormap_client.models.sensor_profile.SensorProfile(
                                area_id = '', 
                                assignments = [
                                    sensormap_client.models.sensor_profile_assignment.SensorProfileAssignment(
                                        data = [
                                            sensormap_client.models.sensor_data.SensorData(
                                                error_flat = 56, 
                                                instrument_seq = 56, 
                                                sensor_id = '', 
                                                shake = 56, 
                                                soil_moisture_count = 56, 
                                                temperature_1 = 1.337, 
                                                temperature_2 = 1.337, 
                                                temperature_3 = 1.337, 
                                                temperature_average = 1.337, 
                                                time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                            ], 
                                        date_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        date_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        id = '', 
                                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        sensor = sensormap_client.models.sensor.Sensor(
                                            assignments = [
                                                sensormap_client.models.sensor_profile_assignment.SensorProfileAssignment(
                                                    date_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    date_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    id = '', 
                                                    last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    sensor_id = '', 
                                                    sensor_profile = sensormap_client.models.sensor_profile.SensorProfile(
                                                        area_id = '', 
                                                        assignments = , 
                                                        coord_srid = 56, 
                                                        coord_x = 1.337, 
                                                        coord_y = 1.337, 
                                                        coord_z = 1.337, 
                                                        description = '', 
                                                        id = '', 
                                                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        name = '', ), 
                                                    sensorprofile_id = '', )
                                                ], 
                                            comment = '', 
                                            data = [
                                                sensormap_client.models.sensor_data.SensorData(
                                                    error_flat = 56, 
                                                    instrument_seq = 56, 
                                                    sensor_id = '', 
                                                    shake = 56, 
                                                    soil_moisture_count = 56, 
                                                    temperature_1 = 1.337, 
                                                    temperature_2 = 1.337, 
                                                    temperature_3 = 1.337, 
                                                    temperature_average = 1.337, 
                                                    time_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                ], 
                                            data_base64 = '', 
                                            data_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            data_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            description = '', 
                                            id = '', 
                                            last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            manufacturer = '', 
                                            name = '', 
                                            serial_number = '', ), 
                                        sensor_id = '', 
                                        sensor_profile = , 
                                        sensorprofile_id = '', )
                                    ], 
                                coord_srid = 56, 
                                coord_x = 1.337, 
                                coord_y = 1.337, 
                                coord_z = 1.337, 
                                description = '', 
                                id = '', 
                                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', )
                            ], 
                        soil_profiles = [
                            sensormap_client.models.soil_profile.SoilProfile(
                                area_id = '', 
                                aspect = '', 
                                coord_srid = 56, 
                                coord_x = 1.337, 
                                coord_y = 1.337, 
                                coord_z = 1.337, 
                                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description_horizon = null, 
                                gradient = '', 
                                id = '', 
                                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                lythology_surficial_deposit = '', 
                                name = '', 
                                parent_material = 1.337, 
                                photo = '', 
                                soil_diagram = '', 
                                soil_type_id = '', 
                                topography = '', 
                                vegetation_type = '', 
                                weather = '', )
                            ], 
                        transects = [
                            sensormap_client.models.transect.Transect(
                                area_id = '', 
                                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                description = '', 
                                id = '', 
                                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                name = '', 
                                nodes = [
                                    sensormap_client.models.transect_node.TransectNode(
                                        order = 56, 
                                        plot_id = '', )
                                    ], )
                            ], ), 
                    area_id = '', 
                    aspect = '', 
                    coord_srid = 56, 
                    coord_x = 1.337, 
                    coord_y = 1.337, 
                    coord_z = 1.337, 
                    created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    gradient = 'flat', 
                    id = '', 
                    image = '', 
                    last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lithology = '', 
                    name = '', 
                    nearest_sensor_profiles = [
                        sensormap_client.models.closest_sensor_profile.ClosestSensorProfile(
                            distance = 1.337, 
                            elevation_difference = 1.337, 
                            id = '', 
                            name = '', )
                        ], 
                    samples = [
                        sensormap_client.models.plot_sample.PlotSample(
                            al_ug_per_g = 1.337, 
                            archea_per_g = 1.337, 
                            bacteria_per_g = 1.337, 
                            c = 1.337, 
                            ca_ug_per_g = 1.337, 
                            cl_ug_per_g = 1.337, 
                            clay_percent = 1.337, 
                            cn = 1.337, 
                            created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            fe_ug_per_g = 1.337, 
                            fungi_per_g = 1.337, 
                            id = '', 
                            k_ug_per_g = 1.337, 
                            last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            loi = 1.337, 
                            lower_depth_cm = 1.337, 
                            methanogens_per_g = 1.337, 
                            methanotrophs_per_g = 1.337, 
                            mfc = 1.337, 
                            mg_ug_per_g = 1.337, 
                            mn_ug_per_g = 1.337, 
                            n = 1.337, 
                            na_ug_per_g = 1.337, 
                            name = '', 
                            p_ug_per_g = 1.337, 
                            ph = 1.337, 
                            plot_id = '', 
                            replicate = 56, 
                            rh = 1.337, 
                            s_ug_per_g = 1.337, 
                            sample_weight = 1.337, 
                            sand_percent = 1.337, 
                            si_ug_per_g = 1.337, 
                            silt_percent = 1.337, 
                            subsample_replica_weight = 1.337, 
                            subsample_weight = 1.337, 
                            upper_depth_cm = 1.337, )
                        ], 
                    topography = '', 
                    transects = , 
                    vegetation_type = '', 
                    weather = '', ),
                plot_id = '',
                replicate = 56,
                rh = 1.337,
                s_ug_per_g = 1.337,
                sample_weight = 1.337,
                sand_percent = 1.337,
                si_ug_per_g = 1.337,
                silt_percent = 1.337,
                subsample_replica_weight = 1.337,
                subsample_weight = 1.337,
                upper_depth_cm = 1.337
            )
        else:
            return PlotSample(
                id = '',
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                lower_depth_cm = 1.337,
                name = '',
                plot_id = '',
                replicate = 56,
                upper_depth_cm = 1.337,
        )
        """

    def testPlotSample(self):
        """Test PlotSample"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
