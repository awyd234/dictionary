# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser(allow_no_value=True)
config.read('../etc/config.ini')


def get_value(section, option, default=None):
    try:
        return format(config.get(section, option))
    except:
        return default
