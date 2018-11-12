import sys
import os
import time
import selenium
from selenium.webdriver.remote import webdriver
import chromedriver_binary

if not os.path.exists(chromedriver_binary.chromedriver_filename):
    print('https://sites.google.com/a/chromium.org/chromedriver/downloads')
    sys.exit()
else:
    print('ChromeDriver: [%s]' % chromedriver_binary.chromedriver_filename)


def factory() -> webdriver:
    return selenium.webdriver.Chrome(
        executable_path=chromedriver_binary.chromedriver_filename
    )
