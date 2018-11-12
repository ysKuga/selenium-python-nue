import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote import webdriver, webelement


class Element:

    wait_limit = 30

    def __init__(self, driver: webdriver):
        self.driver = driver

    def by(self) -> By:
        return By

    def selector(self, selector) -> tuple:
        if isinstance(selector, str):
            if re.match(r'^//', selector):
                return (By.XPATH, selector)
            if re.match(r'^[.#]\w', selector):
                return (By.CSS_SELECTOR, selector)
        else:
            return selector

    def wait(self, selector):
        driver = self.driver
        # https://qiita.com/motoki1990/items/a59a09c5966ce52128be#webdriverwait
        WebDriverWait(driver, self.wait_limit).until(
            expected_conditions.element_to_be_clickable(
                self.selector(selector))
        )

    def find(self, selector, wait: bool = True) -> webelement:
        driver = self.driver
        if wait:
            self.wait(selector)

        selector_tuple = self.selector(selector)
        return driver.find_element(selector_tuple[0], selector_tuple[1])


def factory(driver: webdriver):
    return Element(driver)
