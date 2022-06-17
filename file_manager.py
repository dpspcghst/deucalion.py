import os
from shutil import copy, rmtree
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

        if os.path.isfile(file_name):
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

        if not os.path.exists(directory_name):
            os.mkdir(directory_path)
            print(f"{directory_name} has been created.")
            logger.info(f"{directory_name} has been created.")

        elif os.path.exists(directory_path):
            print(f"{directory_name} already exists.")
            logger.info(f"{directory_name} already exists.")

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

        if os.path.exists(directory_name):
            try:
                os.rmdir(directory_name)
                print(f"{directory_name} has been deleted.")
                logger.info(f"{directory_name} has been deleted.")
            except OSError:
                print(f"{directory_name} is not empty.")
                logger.info(f"{directory_name} is not empty.")
                print(f"{directory_name} was not deleted.")
                logger.info(f"{directory_name} was not deleted.")

        elif not os.path.exists(directory_name):
            print(f"{directory_name} does not exists.")
            logger.info(f"{directory_name} does not exists.")
    
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

    def find_file(self):

        pass

    def open_file(self):
        """
        """

        file_name = input("file name -> ")
    
        print("Opening file...")
        logger.info("Opening file...")

        if os.path.exists(file_name):
            print(f"_________{file_name}_________")
            file = open(file_name, "r")
            print(file.read())
            logger.info(file.read())

        elif not os.path.exists(file_name):
            print(f"{file_name} does not exist.")
            logger.info(f"{file_name} does not exist.")

    def rename_directory(self):
        """
        """

        old_directory_name = input("old directory name -> ")
        new_directory_name = input("new directory name -> ")
    
        print("Renaming directory...")
        logger.info("Renaming directory...")

        if os.path.exists(old_directory_name):
            os.rename(old_directory_name, new_directory_name)
            print("This directory has been renamed.")
            logger.info("This directory has been renamed.")
    
        elif not os.path.exists(old_directory_name):
            print(f"{old_directory_name} cannot be found.")
            logger.info(f"{old_directory_name} cannot be found.")
    
        elif os.path.exists(new_directory_name):
            print(f"{new_directory_name} already exists.")
            logger.info(f"{new_directory_name} already exists.")

    def rename_file(self):
        """
        """

        old_file_name = input("old file name -> ")
        new_file_name = input("new file name -> ")
    
        print("Renaming file...")
        logger.info("Renaming file...")
        if os.path.exists(old_file_name):
            os.rename(old_file_name, new_file_name)
            print("This file has been renamed.")
            logger.info("This file has been renamed.")
    
        elif not os.path.exists(old_file_name):
            print(f"{old_file_name} cannot be found.")
            logger.info(f"{old_file_name} cannot be found.")
    
        elif os.path.exists(new_file_name):
            print(f"{old_file_name} already exists.")
            logger.info(f"{old_file_name} already exists.")
