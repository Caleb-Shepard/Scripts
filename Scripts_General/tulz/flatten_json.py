from flatten_json import flatten
import json
import os

# TODO implement a coherent way to handle folder path, both input and output
DISK_PATH        = "C:" + os.sep
FOLDER_PATH      = 'Users' + os.sep + os.getenv('username') + os.sep + 'Documents' + os.sep + 'Desktop' + os.sep + 'demo_folder'
INPUT_DIRECTORY  = os.path.join(os.sep, DISK_PATH, FOLDER_PATH)
OUTPUT_DIRECTORY = os.path.join(os.sep, DISK_PATH, FOLDER_PATH)
STRIP_NEWLINES_FROM_VALUES = True


def strip_newlines(string: str) -> str:
    if '\n' in string:
        string = string.replace('\n', '')
    if '\r' in string:
        string = string.replace('\r', '')

    return string


def flatten_dictionary(dictionary: dict) -> str:
    flattened_data = flatten(dictionary)
    flattened_dictionary = ''
    for key, value in flattened_data.items():
        # Remove newlines from possible values
        if STRIP_NEWLINES_FROM_VALUES:
            if type(value) is str:
                if '\n' in value:
                    value = value.replace('\n', ' ')
                if '\r' in value:
                    value = value.replace('\r', '')

        flattened_dictionary += '"' + str(key) + '": "' + str(value) + '"\n'

    return flattened_dictionary


def main():
    # Load dictionary as input file
    with open(INPUT_DIRECTORY + os.sep + 'json_output.json') as json_file:
        json_data = json.load(json_file)
    # Flatten input
    flattened_dictionary = flatten_dictionary(json_data)
    # Export output as flattened file
    with open(OUTPUT_DIRECTORY + os.sep + 'flattened_dictionary.txt', 'w') as flat_keys:
        flat_keys.write(flattened_dictionary)

if __name__ == '__main__':
    print('Flatten JSON!')
    main()
