import sys
import logging
import curses
import toml

from pathlib import Path

try:
    config_file = Path().home() / Path(".config/moniton/config.toml")
    config = toml.load(config_file)
except toml.decoder.TomlDecodeError as err:
    logging.error('Toml decode error: {}'.format(err))
    sys.exit(1)
except IsADirectoryError:
    logging.error("The config file '{}' is a directory".format(config_file))
    sys.exit(1)
except FileNotFoundError:
    logging.error("The config file '{}' does not exist".format(config_file))
    sys.exit(1)


class Color:

    def __init__(self):
        curses.start_color()

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.green_on_black = curses.color_pair(1)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        self.red_on_black = curses.color_pair(2)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        self.yellow_on_black = curses.color_pair(3)

        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.cyan_on_black = curses.color_pair(4)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.white_on_black = curses.color_pair(5)

class Config:

    def __init__(self, cls=False, dictionary={}):
        def _traverse(key, element):
            if isinstance(element, dict):
                return key, Config(dictionary=element)
            else:
                return key, element

        if cls:
            cls_name = cls.__class__.__name__
            if cls_name in config:
                job_config = config[cls_name]
                dictionary = job_config

        objd = dict(_traverse(k, v) for k, v in dictionary.items())
        self.__dict__.update(objd)

    def __repr__(self):
        return "{}".format(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def items(self):
        return self.__dict__.items()
