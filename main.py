import os
from shutil import copy
from sys import exit

from file_manager import FileManager as fm

class Two():
    """
    """

    def __init__(self):
        """
        """

        self.fm = fm()
    
    def run(self):
        """
        """

        while True:
            command = input("> ").lower().strip()

            if command == "copy file":
                self.fm.copy_file()
            
            if command == "create directory":
                self.fm.create_directory()
            
            if command == "create file":
                self.fm.create_file()

            if command == "delete directory":
                self.fm.delete_directory()

            if command == "delete file":
                self.fm.delete_file()

            if command == "exit" or command == "fin":
                exit()


two = Two()
two.run()
