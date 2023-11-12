# ------------------------------------------------------------------------------
# Name:        water_stn_converter.py
#
# Purpose:
#    Converts the provided JSON file to CSV or KML.
#    For the CSV, the output columns will be:
#      {Station_Number}, {Station_Name}, {Longitude}, {Latitude}, LINK
#
#    where LINK is
#    https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}
#
#    Header for CSV will be:
#      StationNumber, StationName, Longitude, Latitude, WaterOfficeLink
#
#    For the KML, the <Placemark> element will have the following sub-elements:
#              <name>{Station_Name}</name>
#              <description>
#                 link
#              </description>
#              <Point>
#                <coordinates>{Longitude},{Latitude},0</coordinates>
#              </Point>
#
#   Items enclosed by { } are the keys in the dictionary associated with
#   each feature (a key:value dictionary of values).
#
# Author:      Brigitte and Mousmi
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import json
import os
import csv
import zipfile

in_json_filename = 'data/water_stn.json'
out_csv_filename = 'json_borne.csv'
out_kml_filename = 'data/json_borne.kml'
out_kmz_filename = 'data/json_borne.kmz'

def load_json_file_to_dict():
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # Use with to open in_json_filename and use that file object as an
    # argument to json.load.  This will return a Python dict with nested
    # lists and dictionaries
    
    script_folder = os.path.dirname(os.path.abspath(__file__))
    
    json_filename = os.path.join(script_folder, in_json_filename)
    
    with open(json_filename) as json_file:
        return json.load(json_file)

def json_to_csv():
    """Converts a JSON file created using the water_stn_downloader module
    to CSV"""

    # Call load_json_file_to_dict()
    json_dict = load_json_file_to_dict()

    # Use with to open out_csv_filename
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_borne_csv = os.path.join(script_folder, out_csv_filename)

    with open(json_borne_csv, 'w', newline= '') as js:
        writer = csv.writer(js)

        # Write the header to the CSV file
        header = ['StationNumber', 'StationName', 'Longitude', 'Latitude', 'WaterOfficeLink']
        writer.writerow(header)

        # Loop through all the features and write the results to the CSV file
        features = json_dict['features']

        for feature in features:

            #Get the values of the key value pairs for the attributes dictionnary within the feature dictionnary
            attributes = feature['attributes']

            #Replace the {Station_Number} in the wateroffice link with the actual station number
            wateroffice_link = 'https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}'
            fixed_link = wateroffice_link.replace('{Station_Number}', attributes['Station_Number'])

            #Write out the row
            row = [attributes['Station_Number'],attributes['Station_Name'],attributes['Longitude'],attributes['Latitude'], fixed_link]
            writer.writerow(row)

def get_wateroffice_link(station_number):
    """Given a station_number, return the English wateroffice link"""
    wateroffice_link = 'https://wateroffice.ec.gc.ca/report/real_time_e.html?stn={Station_Number}'
    fixed_link = wateroffice_link.replace('{Station_Number}', station_number)
    return fixed_link


def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude  """
    attributes = feature['attributes']
    row = [attributes['Station_Number'],attributes['Station_Name'],attributes['Longitude'],attributes['Latitude']]
    return row

def get_kml_header():
    """Return the xml header including the Document start tag
    """
    return '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>'

def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    """
    return f"  <Placemark>\n    <name>{name}</name>\n    <description>\n    {wateroffice_link}\n    </description>\n    <Point>\n        <coordinates>{longitude},{latitude},0</coordinates>\n    </Point>\n  </Placemark>"

def get_kml_footer():
    """Return the document and kml end tags
    """
    return "</Document>\n</kml>"


def json_to_kml():
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_borne_kml = os.path.join(script_folder, out_kml_filename)
    with open(json_borne_kml, 'w') as json_kml:

    #Write kml header
        json_kml.write(get_kml_header() + '\n')

        json_dict = load_json_file_to_dict()
        features = json_dict['features']
        for f in features:
            row = get_values_from_feature(f)
            station_number = row[0]
            name = row[1]
            longitude = row[2]
            latitude = row[3]
            wateroffice_link = get_wateroffice_link(station_number)
            json_kml.write(get_placemark(name, longitude, latitude, wateroffice_link))
        
    #Write kml footer
        json_kml.write(get_kml_footer())


def json_to_kmz():
    json_to_kml()
    script_folder = os.path.dirname(os.path.abspath(__file__))
    json_borne_kml = os.path.join(script_folder, out_kml_filename)
    json_borne_kmz = os.path.join(script_folder, out_kmz_filename)
    with zipfile.ZipFile(json_borne_kmz,'w', zipfile.ZIP_DEFLATED) as Kmz_zip:
        Kmz_zip.write(json_borne_kml)
        Kmz_zip.close()
