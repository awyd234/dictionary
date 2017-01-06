# -*- coding: utf-8 -*-

import configparser
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
config_path = os.path.join(parent_dir, 'etc/config.ini')

config = configparser.ConfigParser(allow_no_value=True)
config.read(config_path)


def get_value(section, option, default=None):
    try:
        return format(config.get(section, option))
    except:
        return default
