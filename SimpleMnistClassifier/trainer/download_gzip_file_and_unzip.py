import os
import gzip
import shutil

from six.moves import urllib
from tensorflow.python.platform import gfile


def download_gzip_file_and_unzip(filename, destination_directory, url):
    # Removing extension from file
    if filename[-3:] == ".gz":
        unzipped_filename = filename[:-3]
    else:
        unzipped_filename = filename
    # Check if destination directory exists, if not create it
    if not gfile.Exists(destination_directory):
        gfile.MakeDirs(destination_directory)
    # Get absolute file paths from operating system
    file_path = os.path.join(destination_directory, filename)
    unzipped_file_path = os.path.join(destination_directory, unzipped_filename)
    # Checking if the data set file already exists
    if not gfile.Exists(unzipped_file_path):
        # Go to url and request to download data set
        urllib.request.urlretrieve(url, file_path)
        # Check that our unzipped file doesnt have the same name as out zipped file
        if not filename == unzipped_filename:
            with gzip.open(file_path, 'rb') as f_in:
                with open(unzipped_file_path, 'wb') as f_out:
                    # Unzipping file and dumping contents into new file
                    shutil.copyfileobj(f_in, f_out)
        with gfile.GFile(file_path) as f:
            # getting size of data set
            size = f.size()
        print('Succesfully downloaded and unzipped ', filename, size, 'bytes.')
    return unzipped_file_path
