# converts a file at an address to a string
def file_to_string(file_location):
    with open(file_location) as file:
        file_as_string = file.read()
    return file_as_string
