import os
import logging
from pathlib import Path

# Configure logging to display timestamps and messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    "src/{project_name}/__init__.py",
    "src/{project_name}/components/__init__.py",
    "src/{project_name}/utils/__init__.py",
    "src/{project_name}/config/__init__.py",
    "src/{project_name}/config/configuration.py",
    "src/{project_name}/pipeline/__init__.py",
    "src/{project_name}/entity/__init__.py",
    "src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Optional: Replace {project_name} with an actual project name
project_name = "cnnClassifier"
list_of_files = [filepath.replace("{project_name}", project_name) for filepath in list_of_files]

# Loop over each file path in the list and create directories and files as needed
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object for easier handling
    filedir, filename = os.path.split(filepath)  # Separate directory and file name

    # Create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Just open and close to create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")