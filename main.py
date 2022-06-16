from os import path
from shutil import copy
from lumberjack import logger

class Two():
    """
    """

    def __init__(self):
        """
        """

        pass

    def copy_file(self, file_name, directory_name):
        """
        """
    
        print("Copying file...")
        logger.info("Copying file...")
        source = file_name
        destination = directory_name
        if path.isfile(file_name):
            copy(source, destination)
            print(f"{file_name} has been copied.")
            logger.info(f"{file_name} has been copied.")
    
        else:
            print(f"{file_name} is already there.")
            logger.info(f"{file_name} is already there.")

    def run(self):
        """
        """

        pass
