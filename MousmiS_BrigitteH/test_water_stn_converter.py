# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        test_water_stn_converter.py
#
# Purpose:     Tests for functions in water_stn_converter.py
#
# Author:      David Viljoen
#
# Created:     09/11/2021
#-------------------------------------------------------------------------------

import json
import os
import csv
import water_stn_converter as wsc


def test_load_json_file_to_dict():
    # Use http://jsonviewer.stack.hu/ to select a value for expected
    expected = 'esriGeometryPoint'
    wsc.in_json_filename = 'data/water_stn.json'
    data = wsc.load_json_file_to_dict()
    # Use a combination of indexes and keys to access some value from the dictionary
    actual = data['geometryType']
    assert actual == expected


def test_get_values_from_feature():
    """Returns row # 4 in the json file returning correct StationNumber, StationName, Longitude, Latitude"""
    expected = '01AQ002,Magaguadavic River at Elmcroft,-66.80667,45.27333'
    feature = 4
    json_dict = wsc.load_json_file_to_dict()
    features = json_dict['features']
    actual = ','.join(wsc.get_values_from_feature(features[feature]))
    assert actual == expected

def test_json_to_csv():
    """Returns row #2 in the csv file returning correct StationNumber, StationName, Longitude, Latitude, WaterOfficeLink """
    expected = '01AD003,St. Francis River at outlet of Glasier Lake,-68.95694,47.20661,https://wateroffice.ec.gc.ca/report/real_time_e.html?stn=01AD003'
    json_borne = wsc.json_to_csv()
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_csv = os.path.join(script_folder,'json_borne.csv')
    with open(json_csv) as i:
            reader = csv.reader(i)
            header = next(reader)
            row_1 = next(reader)
            row_2 = next(reader)
            actual = ','.join(row_2)
    assert actual == expected

def test_get_placemark():
    """Returns row#2 in the json file as a KML Placemark element including start and end tags"""
    name = "St. Francis River at outlet of Glasier Lake"
    longitude = -68.95694
    latitude = 47.20661
    station_number = '01AD003'
    wateroffice_link = wsc.get_wateroffice_link(station_number)
    actual = wsc.get_placemark(name,longitude,latitude,wateroffice_link)
    expected = "  <Placemark>\n    <name>St. Francis River at outlet of Glasier Lake</name>\n    <description>\n    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn=01AD003\n    </description>\n    <Point>\n        <coordinates>-68.95694,47.20661,0</coordinates>\n    </Point>\n  </Placemark>"
    assert expected == actual

def test_export_to_kml():
    """Returns the first line of the kml file and opens kml file in Google Earth"""
    out_kml_filename = 'data/json_borne.kml'
    expected = '<?xml version="1.0" encoding="UTF-8"?>'
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_borne_kml = os.path.join(script_folder, out_kml_filename)
    with open(json_borne_kml) as json_kml:
        actual = json_kml.readline()
        os.startfile(json_borne_kml)
    expected == actual

def test_export_to_kmz():
    out_kml_filename = 'data/json_borne.kml'
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_borne_kml = os.path.join(script_folder, out_kml_filename)
    wsc.json_to_kmz()
    kml_size = os.path.getsize(wsc.out_kml_filename)
    kmz_size = os.path.getsize(wsc.out_kml_filename.replace('.kml', '.kmz'))
    assert kmz_size < kml_size
    assert kmz_size > 10000
    json_borne_kmz = os.path.join(script_folder, out_kml_filename.replace('.kml', '.kmz'))
    with open(json_borne_kmz) as json_kmz:
         os.startfile(json_borne_kmz)






