import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name="CNN classifier"
list_of_files = [
    ".github/workflows/.gitkeep",
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
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for i in list_of_files:
    i=Path(i)
    folder,fl=os.path.split(i)
    if(folder!=""):
        os.makedirs(folder,exist_ok=True)
        logging.info(f"created dir {folder}")
    if os.path.exists(folder):
        with open(fl,"w"):
            logging.info(f"file created in {folder} {fl}")
    else:
        logging.info(f"file already exist{fl}")