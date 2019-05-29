import sys
import os
import time
import selenium
from selenium.webdriver.remote import webdriver
import chromedriver_binary


def get_executable_path() -> str:
    """
    selenium.webdriver.Chrome 用の executable path を返す
    """
    if not os.path.exists(chromedriver_binary.chromedriver_filename):
        print('https://sites.google.com/a/chromium.org/chromedriver/downloads')
        sys.exit()
    else:
        # デフォルトを Chrome に
        print('ChromeDriver: [%s]' % chromedriver_binary.chromedriver_filename)
        return chromedriver_binary.chromedriver_filename


def factory() -> webdriver:
    """
    Chrome 用の webdriver が返る
    """
    return selenium.webdriver.Chrome(
        executable_path=get_executable_path()
    )
