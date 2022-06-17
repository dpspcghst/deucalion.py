from sys import exit
from file_manager import FileManager as fm

class CommandCenter():
    """
    """

    def __init__(self):
        """
        """

        self.commands = [
                "copy file", "create directory", "create file",
                "delete directory", "delete file", "exit",
                "fin", "open file", "rename directory",
                "rename file"
            ]
        self.fm = fm()

    def command_center(self):
        """
        """

        command = input("> ").lower().strip()

        if command == "copy file":
            self.fm.copy_file()
        
        elif command == "create directory":
            self.fm.create_directory()
        
        elif command == "create file":
            self.fm.create_file()

        elif command == "delete directory":
            self.fm.delete_directory()

        elif command == "delete file":
            self.fm.delete_file()

        elif command == "exit" or command == "fin":
            exit()

        elif command == "find file":
            self.fm.find_file()

        elif command == "open file":
            self.fm.open_file()

        elif command == "rename directory":
            self.fm.rename_directory()

        elif command == "rename file":
            self.fm.rename_file()

        elif command not in self.commands:
            print("Please give an accepted command: ")
            print(self.commands)

        else:
            pass
