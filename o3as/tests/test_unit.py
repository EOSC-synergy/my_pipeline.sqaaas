# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2019 Karlsruhe Institute of Technology - Steinbuch Centre for Computing
# This code is distributed under the MIT License
# Please, see the LICENSE file
#
"""
Created on Sat June 30 23:47:51 2020
@author: vykozlov
"""
import numpy as np
import os
import pandas as pd
import pkg_resources
import xarray as xr
import unittest
from o3as import api as o3api
from o3as import config as cfg
from o3as import plots as o3plots
from o3as import plothelpers as phlp

class TestPackageMethods(unittest.TestCase):

    def setUp(self):
        module = __name__.split('.', 1)
        pkg = pkg_resources.get_distribution(module[0])

        # Check package meta info
        self.meta = {
            'name' : 'o3as',
            'version' : None,
            'summary' : 'O3AS service to analyse ozone projections',
            'home-page' : 'https://git.scc.kit.edu/synergy.o3as/o3as',
            'author' : 'KIT-IMK, KIT-SCC',
            'author-email' : 'tobias.kerzenmacher@kit.edu, borja.sanchis@kit.edu, valentin.kozlov@kit.edu',
            'license' : 'GNU LGPLv3'
        }



        # Create artificial data and store it
        delta_years = 2
        self.start_date = (np.datetime64('today', 'M') - 
                           np.timedelta64(12*delta_years, 'M'))
        self.end_date = (self.start_date + 
                         np.timedelta64(12*delta_years - 1, 'M'))
        self.o3ds = xr.Dataset(
            {"t": (("level", "lat", "time"), np.ones((10, 19, 24))),
             "tco3_zm": (("level", "lat", "time"), np.ones((10, 19, 24))),
            },
            coords={
                    "level": [z for z in range(0, 1000, 100)],
                    "lat": [x for x in range(-90, 100, 10)],
                    "time": [ self.start_date + np.timedelta64(x, 'M') 
                              for x in range(0, 12*delta_years, 1)]
                   }
        )

        end_year = np.datetime64('today', 'Y').astype(int) + 1970
        begin_year = end_year - delta_years

        data_base_path = "tmp/data"
        #os.environ["O3AS_DATA_BASEPATH"] = self.data_base_path
        cfg.O3AS_DATA_BASEPATH = data_base_path
        model = "o3as-test"
        ptype = 'tco3_zm'
        test_dir = os.path.join(data_base_path, model) 
        test_path  = os.path.join(test_dir, ptype + "_skim_" + 
                                            str(end_year) + ".nc")
        os.makedirs(test_dir, exist_ok=True)
        self.o3ds.to_netcdf(test_path)
        #self.o3ds.close()

        self.kwargs = {
            'type': ptype,
            'models': [model],
            'begin_year': begin_year,
            'end_year': end_year,
            'lat_min': -10,
            'lat_max': 10
        }

        print(self.kwargs)

        # initialize how to process data
        if ptype == 'tco3_zm':
            self.data = o3plots.ProcessForTCO3(**self.kwargs)
        elif ptype == 'vmro3_zm':
            self.data = o3plots.ProcessForVMRO3(**self.kwargs)
        elif ptype == 'tco3_return':
            self.data = o3plots.ProcessForTCO3Return(**self.kwargs)
            
        # initialize the plot title and filename
        self.plot_title = (self.kwargs['type'] + ' (inputs: ' +
                           str(self.kwargs['begin_year']) + ',' +
                           str(self.kwargs['end_year']) + ',' +
                           str(self.kwargs['lat_min']) + ',' +
                           str(self.kwargs['lat_max']) + ')' )

        self.plot_filename = (self.kwargs['type'] + '_' + 
                              str(self.kwargs['begin_year']) + '_' +
                              str(self.kwargs['end_year']) + '_' +
                              str(self.kwargs['lat_min']) + '_' +
                              str(self.kwargs['lat_max']))

    def test_metadata_type(self):
        """
        Test that o3meta is dict
        """
        o3meta = o3api.get_metadata()
        self.assertTrue(type(o3meta) is dict)


    def test_metadata_values(self):
        """
        Test that metadata contains right values (subset)
        """
        o3meta = o3api.get_metadata()
        self.assertEqual(self.meta['name'].replace('-','_'),
                         o3meta['name'].replace('-','_'))
        self.assertEqual(self.meta['summary'].replace('-','_'),
                         o3meta['summary'].replace('-','_'))
        self.assertEqual(self.meta['home-page'].lower().replace(' ',''),
                         o3meta['home-page'].lower().replace(' ',''))
        self.assertEqual(self.meta['author'].lower().replace(' ',''),
                         o3meta['author'].lower().replace(' ',''))
        self.assertEqual(self.meta['author-email'].lower().replace(' ',''), 
                         o3meta['author-email'].lower().replace(' ',''))
        self.assertEqual(self.meta['license'].lower(),
                         o3meta['license'].lower())

    def test_list_models_type(self):
        """
        Test that self.meta is dict
        """
        o3list = o3api.list_models()
        self.assertTrue(type(o3list) is dict)

    def test_get_model_info_type(self):
        """
        Test that model_info is dict
        """
        o3kwargs = {
            'model': self.kwargs['models'][0],
            'type': self.kwargs['type']
        }
        o3model_info = o3api.get_model_info(**o3kwargs)
        print(F"O3 model: {o3model_info}")
        self.assertTrue(type(o3model_info) is dict)

    def test_get_dataslice_type(self):
        """
        Test that the returned dataset type is correct, xarray.Dataset
        """
        model = self.kwargs['models'][0]
        ds = self.data.get_dataslice(model)
        self.assertTrue(type(ds) is xr.Dataset)


    def test_get_data_processed_type(self):
        """
        Test that the returned dataset type is correct, xarray.Dataset
        """
        model = self.kwargs['models'][0]
        ds = self.data.get_plot_data(model)
        self.assertTrue(type(ds) is xr.Dataset)


    def test_get_dataset_values(self):
        """
        Test that returned dataset values are the same as generated.
        """
        model = self.kwargs['models'][0]
        ds = self.data.get_plot_data(model)
        self.assertEqual(ds, self.o3ds)


    def test_get_date_range(self):
        """
        Test correctness of returned min/max dates
        """
        date_min, date_max = phlp.get_date_range(self.o3ds)
        self.assertEqual(date_min, self.start_date)
        self.assertEqual(date_max, self.end_date)


    def test_get_periodicity(self):
        """
        Test correctness of returned periodicity
        """
        time_axis = pd.DatetimeIndex(self.o3ds.coords['time'].values)
        period = phlp.get_periodicity(time_axis)
        self.assertEqual(period, 12)
        
    def test_get_plot_title(self):
        """
        Test setting of the plot title
        """
        o3plot_title = phlp.set_plot_title(**self.kwargs)
        self.assertEqual(self.plot_title, o3plot_title)

    def test_get_plot_filename(self):
        """
        Test setting of the plot filename
        """
        o3plot_filename = phlp.set_filename(**self.kwargs)
        self.assertEqual(self.plot_filename, o3plot_filename)

if __name__ == '__main__':
    unittest.main()
