from enum import Enum
from selenium.webdriver.remote import webdriver
from . import chrome, firefox


class DriverTypes(Enum):
    chrome = 1
    firefox = 2


def factory(driver_type: DriverTypes) -> webdriver:
    if driver_type is DriverTypes.firefox:
        return firefox.factory()
    elif driver_type is DriverTypes.chrome:
        return chrome.factory()

    return chrome.factory()
