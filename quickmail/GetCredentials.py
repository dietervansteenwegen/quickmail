from configparser import ConfigParser
from typing import Dict, Tuple


def getCredentials():
    parser = ConfigParser()
    parser.read('./quickmail/credentials')
    rtnDict = {}
    for sect in parser.sections():
        for key, value in parser.items(sect):
            rtnDict[key] = value

    return rtnDict


def checkMissing(credentials: Dict, required: Tuple):
    return [req for req in required if len(credentials[req]) < 1]
