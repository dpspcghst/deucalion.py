import logging
from os import getcwd, mkdir, path

log_path = path.join(getcwd(), "logs/deucalion.log")
if not path.isdir("logs"):
    print("Logging directory not found.")
    print("Creating logging directory...")
    log_directory_path = path.join(getcwd(), "logs")
    mkdir(log_directory_path)
    file = open(log_path, "x")
    file.close()

elif not path.exists(log_path):
    file = open(log_path, "x")
    file.close()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_path)

logger = logging.getLogger()
