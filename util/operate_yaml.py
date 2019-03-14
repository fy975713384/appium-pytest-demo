import os
import yaml
from setting import Setting as ST


class OperateYAML:
    def __init__(self, yaml_path: str = None):
        if yaml_path:
            self._yml = yaml_path
        else:
            self._yml = os.path.abspath(f'{ST.ROOT_PATH}/conf/ElementData.yml')

    def _read_yml(self):
        with open(self._yml) as f:
            data = yaml.load(f)
            return data

    def get_data(self, k1: str, k2: str) -> tuple:
        data = self._read_yml()
        ele_data = str(data[k1][k2])
        if '=' in ele_data:
            tag, exp = ele_data.split('=')
            tag = str(tag).strip()
            exp = str(exp).strip()
            return tag, exp
        else:
            raise RuntimeError('元素格式错误')
