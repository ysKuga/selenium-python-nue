import sys
import os
import time
from selenium import webdriver
import chromedriver_binary

if not os.path.exists(chromedriver_binary.chromedriver_filename):
    print('https://sites.google.com/a/chromium.org/chromedriver/downloads')
    sys.exit()
else:
    print('ChromeDriver: [%s]' % chromedriver_binary.chromedriver_filename)

driver = webdriver.Chrome(
    executable_path=chromedriver_binary.chromedriver_filename
)

driver.get('https://google.co.jp/')

time.sleep(5)

driver.quit()
