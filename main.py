import logging
from command_center import CommandCenter as cc

# sets up err.log for file handling
handler = logging.FileHandler(
    encoding="utf-8",
    filename="deucalion_err.log",
    mode="w"
)

# determines how the log will be formatted
handler.setFormatter(logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s"))

logger = logging.getLogger("file manager")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

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
