import yaml
import os
from common import exceptions as exp


def parse_from_yaml_file_str(file_path_str):
    if not isinstance(file_path_str, str):
        raise exp.FileNameMustBeString()
    if not os.path.exists(file_path_str):
        raise exp.FileNotExists(file_name=file_path_str)
    with open(file_path_str, 'r+') as f:
        content = f.read()
    return yaml.safe_load(content)


def mkdir_from_str(dest):
    if os.path.exists(dest):
        raise exp.DirectoryExists(directory_name=dest)
    os.makedirs(dest, mode=0o777)


def dir_already_existed(dest):
    return os.path.exists(dest)
