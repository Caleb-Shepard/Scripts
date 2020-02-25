import zipfile

def unzip(zip_archive, destination):
    with zipfile.ZipFile(zip_archive, "r") as zip_archive:
        zip_archive.extractall(destination)
