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
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import json

in_json_filename = 'data/water_stn.json'
out_csv_filename = ''
out_kml_filename = ''

def json_to_csv():
    """Converts a JSON file created using the water_stn_downloader module
    to CSV"""

    # Call load_json_file_to_dict()
    #

    # Use with to open out_csv_filename
    #

        # Write the header to the CSV file
        #


        # Loop through all the features and write the results to the CSV file
        #


def json_to_kml():
    """Converts a JSON file created using the water_stn_downloader module
    to KML"""


def load_json_file_to_dict():
    """Use json.load(file_object) to convert the contents of in_json_filename
    to a Python dictionary.  Return the resulting dictionary.
    """
    # Use with to open in_json_filename and use that file object as an
    # argument to json.load.  This will return a Python dict with nested
    # lists and dictionaries


def get_values_from_feature(feature):
    """Given a dictionary of feature attributes, return the following:
        Station_Number, Station_name, Longitude, Latitude  """


def get_wateroffice_link(station_number):
    """Given a station_number, return the English wateroffice link"""


def get_kml_header():
    """Return the xml header including the Document start tag
    """


def get_kml_footer():
    """Return the document and kml end tags
    """


def get_placemark(name, longitude, latitude, wateroffice_link):
    """Return the KML Placemark element including start and end tags
    """

