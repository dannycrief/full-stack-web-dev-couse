import json
import math
import os


class Config:
    EVN_VAR_NAME = "CONFIG_PATH"

    def __init__(self, config_path):
        self.path = config_path
        self._data = {}

    @classmethod
    def load_from_env(cls):
        config_path = os.environ[cls.EVN_VAR_NAME]
        return cls(config_path)

    def read(self):
        with open(self.path) as fd:
            self._data = json.load(fd)

    def __getitem__(self, item):
        return self._data[item]

    @property
    def db_connectino_uri(self):
        section = self._data["database"]
        return "postgresql://{user}:{password}@{host}:{port}/{name}".format(**section)

    @staticmethod
    def list_static(static_path):
        ret = []
        for path in os.listdir(static_path):
            _, ext = os.path.splitext(path)
            if ext in [".js", ".html", ".png"]:
                ret.append(path)
        return ret


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.1415 * self.radius ** 2

    @area.setter
    def area(self, value):
        self.radius = math.sqrt(value / 3.1415)


if __name__ == '__main__':
    cfg = Config("file.json")
    cfg.read()
    print(cfg["server"]["host"])
    print(cfg["server"]["port"])
    print(cfg.db_connectino_uri)
    cfg = Config.load_from_env()
    print(cfg["server"]["port"])
    print()
    c1 = Circle(4)
    print(c1.area)
    c1.area = 48
    print(c1.area)
    print(c1.radius)
