import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier.utils import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """read yaml file and returns
    
    Args:
        path_to_yaml: path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
        
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_loadd(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directories: list, verbose=True):  
    """Create a list of directories

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"create directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved with json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")
        
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data

    Args:
        path (Path): _description_
        data (dict): _description_
    """

    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file is loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """_summary_

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    
    Returns:
        Any: object stored in the file
    
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: object stored in the file
    
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024.0)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdate = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdate)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())






