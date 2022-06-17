from command_center import CommandCenter as cc

class Deucalion():
    """
    """

    def __init__(self):
        """
        """

        self.cc = cc()
    
    def run(self):
        """
        """

        while True:
            self.cc.command_center()

if __name__ == "__main__":
    deuca = Deucalion()
    deuca.run()
