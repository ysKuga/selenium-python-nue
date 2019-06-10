import re
from enum import Enum, auto
from selenium.webdriver.remote import webdriver
from . import chrome, firefox


class DriverTypes(Enum):
    chrome = auto()
    firefox = auto()


def factory(driver_type=None) -> webdriver:
    if driver_type is not None:
        if driver_type is DriverTypes.firefox or re.search('firefox', driver_type, re.IGNORECASE):
            return firefox.factory()
        elif driver_type is DriverTypes.chrome or re.search('chrome', driver_type, re.IGNORECASE):
            return chrome.factory()

    return chrome.factory()
