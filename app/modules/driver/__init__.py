from selenium.webdriver.remote import webdriver
from . import chrome


def factory() -> webdriver:
    return chrome.factory()
