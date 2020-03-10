# Script to recurse through all subdirectories
from pandas.io.json import json_normalize
import flatten_json
import xmltodict
import argparse
import zipfile
import shutil
import pandas
import tqdm
import json
import os
import re

''' ------------------------------ CONSTANTS ------------------------------ '''
JSON_WORKBOOKS_ARRAY_OPENER    = '{"jsonified-workbooks":['
JSON_WORKBOOKS_ARRAY_CLOSER    = ']}'
JSON_WORKBOOKS_ARRAY_DELIMITER = ','
STARTING_DIRECTORY             = '/'
EXTRACT_NAME                   = 'extracted_workbook'
SECURITY_WARNING               = r"""
SECURITY WARNING

This program relies on creating a temporary directory to extract Tableau
archives. Be sure that only appropriate users have access to tmp directories.
On DOS systems, the default tmp directory is located at "C:\Windows\Temp for
a system", and for an individual, the tmp directory is located at
"C:\Users\<username>\AppData\Local\Temp".

The default tmp directory in a nix system is located at /tmp

To prevent inappropriate access, local tmp directories are used. You may want to
customize the tmp location used dependent on your policy or need.
"""

'''
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--tmpdir', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
args = parser.parse_args()
'''

''' -------------------------- RUNTIME CONSTANTS -------------------------- '''
FOLDER_PATH = 'Users' + os.sep + os.getenv('username') + os.sep + 'Documents' + os.sep + 'Desktop' + os.sep + 'demo_folder'
DISK_PATH   = "C:" + os.sep

STARTING_DIRECTORY = os.path.join(os.sep, DISK_PATH, FOLDER_PATH)
OUTPUT_DIRECTORY   = os.path.join(os.sep, DISK_PATH, FOLDER_PATH)
TMP_DIRECTORY      = os.path.join(os.sep, DISK_PATH, FOLDER_PATH)

REMOVE_IMAGE_RAW_BITS = True   # This needs to come from some sort of command line argument
REMOVE_CUSTOM_SQL     = False  # This needs to come from some sort of command line argument

def unzip(zip_archive, destination):
    print('suggested destination: ' + destination)
    with zipfile.ZipFile(zip_archive, "r") as zip_archive:
        zip_archive.extractall(destination)


# we don't want to merge python dictionaries, we want to add each dictionary to
# a larger dictionary
def get_all_workbooks(starting_directory, unzip_tmp_directory):
    print('current dir: ' + starting_directory)
    tableau_workbooks_xml = []

    for item in os.listdir(starting_directory):
        if item.endswith('.twb'):                               # straightforward xml extraction
            tableau_workbooks_xml.append(
                get_workbook_xml(starting_directory + '\\' + item)
            )
        elif item.endswith('.twbx'):                            # extract archive, extract xml
            extract_destination  = unzip_tmp_directory + '/' + EXTRACT_NAME
            archive_directory    = unzip(starting_directory + '\\' + item, extract_destination)
            archive_workbook_xml = get_all_workbooks(extract_destination, unzip_tmp_directory)
            if type(archive_workbook_xml) is list:
                for xml_string in archive_workbook_xml:
                    if type(xml_string) is not str:
                        print('Unexpected type!')
                    else:
                        tableau_workbooks_xml.append(xml_string)
            elif type(archive_workbook_xml) is str:
                tableau_workbooks_xml.extend(archive_workbook_xml)
            else:
                print('Unexpected type! Error appending XML data to tableau_workbooks_xml')
                exit()
            # Remove your unzipped archive
            shutil.rmtree(extract_destination)
        elif os.path.isdir(starting_directory + '\\' + item):                               # recurse over subdirectory
            tableau_workbooks_xml.extend(get_all_workbooks(starting_directory + '\\' + item, unzip_tmp_directory))

    return tableau_workbooks_xml


def get_workbook_xml(path):
    xml_contents = ''
    print('Path = ' + path)
    with open(path, "r") as file_stream:
        xml_contents = file_stream.read()

    return xml_contents


def list_of_xml_to_list(xml_list):
    json_list = []
    print('XML_LIST type: ' + str(type(xml_list)))
    for xml in xml_list:
        if type(xml) is list:
            for xml_string in xml:
                json_list.append(xmltodict.parse(xml_string))

        print('XML type: ' + str(type(xml)))
        print('XML type: ' + str(xml))
        json_list.append(xmltodict.parse(xml))

    return json_list


# Given the state of a flag, start cleaning process
def cleanse(json_summary):
    json_summary = json_summary  # not sure if this needs to be declared locally, this might be removable

    # Remove the raw image content, not information about the images
    if REMOVE_IMAGE_RAW_BITS:
        # workbook.thumbnails.thumbnail[].#text
        try:
            for element in json_summary['workbook']['thumbnails']['thumbnail']:
                # If this is not an element, it will be interpreted as a string which will crash the metho d and program
                if type(element) is not str:
                    del element['#text']
            try:
                # Case where there is only one image in the workbook, not multiple
                del json_summary['workbook']['thumbnails']['thumbnail']['#text']
            except KeyError as key_error:
                pass
            except TypeError as type_error:
                # happens when slicing a list, depends on what's in the attribute
                pass
        except KeyError as key_error:
            pass

        # workbook.external.shapes.shape[].#text
        try:
            for element in json_summary['workbook']['external']['shapes']['shape']:
                # If this is not an element, it will be interpreted as a string which will crash the metho d and program
                if type(element) is not str:
                    del element['#text']
            try:
                # Case where there is only one image in the workbook, not multiple
                del json_summary['workbook']['external']['shapes']['shape']['#text']
            except KeyError as key_error:
                pass
            except TypeError as type_error:
                # happens when slicing a list, depends on what's in the attribute
                pass
        except KeyError as key_error:
            pass

    # Remove the raw SQL information, not the individual formulas that are used throughout the report
    if REMOVE_CUSTOM_SQL:
        # connection.metadata-records.metadata-record[].attributes.attribute[].#text
        try:
            for data_source in json_summary['workbook']['datasources']['datasource']:
                # If this is not an element, it will be interpreted as a string which will crash the method and program
                for metadata_record in data_source['connection']['metadata-records']['metadata-record']:
                    for attribute in metadata_record['attributes']['attribute']:
                        if type(attribute) is not str:
                            del attribute['#text']
        except KeyError as key_error:
            print('Recovered from key error when attempting to remove custom sql.')
            print(key_error)

    return json_summary


def get_windows_username():
    os.getlogin()


def get_nix_username():
    os.popen('whoami').read()


def make_tmp_directory(tmp_directory_location):
    if os.path.exists(tmp_directory_location):
        # don't make dir
        pass
    else:
        pass


def clear_tmp_directory():
    pass

def get_workbook_name():
    # return $(FILE_NAME or PATH?)
    pass

def detect_custom_sql():
    # if datasources.datasource[].connection.@class == ("sqlproxy" or "postgres")
    # however, still not indicative of custom SQL; are the XML queries you removed indicative?
    pass

def main():
    os.system('cls')

    input('Defaulting to starting directory: ' + STARTING_DIRECTORY)
    input('Defaulting to output directory: '   + OUTPUT_DIRECTORY)
    input('Defaulting to tmp directory: '      + TMP_DIRECTORY)
    input('Remove image raw bits (.#text): ' + str(REMOVE_IMAGE_RAW_BITS))
    input('Remove custom SQL: ' + str(REMOVE_CUSTOM_SQL))

    workbook_xml_list = get_all_workbooks(STARTING_DIRECTORY, TMP_DIRECTORY)
    output_file_path  = OUTPUT_DIRECTORY + os.sep + 'json_output.json'
    json_list         = list_of_xml_to_list(workbook_xml_list)

    try:  # file I/O writing output and removing a trailing character
        # Write output
        with open(output_file_path, 'w') as output_file:
            output_file.write(JSON_WORKBOOKS_ARRAY_OPENER)
        with open(output_file_path, 'a') as output_file:
            for json_summary in json_list:
                string = json.dumps(cleanse(json_summary))
                output_file.write(string + JSON_WORKBOOKS_ARRAY_DELIMITER)
        # remove trailing '},' that was generated at the end of the loop
        with open(output_file_path, 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()
        with open(output_file_path, 'a') as output_file:
            output_file.write(JSON_WORKBOOKS_ARRAY_CLOSER)
    except IOError as e:
        print('Failed to open or write JSON output.' + str(e))

if __name__ == "__main__":
    main()
