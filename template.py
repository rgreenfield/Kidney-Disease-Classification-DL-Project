import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'


list_of_files = [
    ".github/wokrflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html",
    "Dockerfile",
    "setup.py",
    "scores.json",
    "app.py",
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filename, "w") as f:
            pass
            logging.info("Creating empty file: {filepath}")

    else:
        logging.info(f"File already exists: {filename}")
        

