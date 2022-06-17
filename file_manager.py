import os
from lumberjack import logger

class FileManager():
    """
    """

    def __init__(self):
        """
        """

        pass

    def copy_file(self):
        """
        """

        file_name = input("file name -> ")
        directory_name = input("directory name -> ")
    
        print("Copying file...")
        logger.info("Copying file...")

        if path.isfile(file_name):
            copy(file_name, directory_name)
            print(f"{file_name} has been copied.")
            logger.info(f"{file_name} has been copied.")
    
        else:
            print(f"{file_name} is already there.")
            logger.info(f"{file_name} is already there.")

    def create_directory(self):
        """
        """

        directory_name = input("directory name -> ")
        parent_directory = os.getcwd()
        directory_path = os.path.join(parent_directory, directory_name)

        os.mkdir(directory_path)

    def create_file(self):
        """
        """

        file_name = input("file name -> ")
        content = input("content -> ")

        print("Creating file...")
        logger.info("Creating file...")

        if not os.path.exists(file_name):
            file = open(file_name, "w")
            file.write(content)
            file.close()
            print(f"{file_name} has been created.")
            logger.info(f"{file_name} has been created.")
    
        else:
            print(f"{file_name} already exists.")
            logger.info(f"{file_name} already exists.")
    
    def delete_directory(self):
        """
        """

        directory_name = input("directory name -> ")

        os.rmdir(directory_name)
    
    def delete_file(self):
        """
        """

        file_name = input("file name -> ")
    
        print("Deleting file...")
        logger.info("Deleting file...")

        if os.path.isfile(file_name):
            os.remove(file_name)
            print(f"{file_name} has been deleted.")
            logger.info(f"{file_name} has been deleted.")
    
        else:
            print(f"{file_name} does not exists.")
            logger.info(f"{file_name} does not exists.")
