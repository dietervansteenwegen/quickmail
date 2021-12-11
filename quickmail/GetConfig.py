from configparser import ConfigParser
from typing import Dict, Tuple


def get_config():
    parser = ConfigParser()
    parser.read('./quickmail/credentials')
    rtnDict = {}
    for sect in parser.sections():
        for key, value in parser.items(sect):
            rtnDict[key] = value.strip("'")

    return rtnDict


def check_missing(cfg: Dict, required: Tuple):
    return [req for req in required if len(cfg.get(req, '')) < 1]


def create_blank():
    pass
