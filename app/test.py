import sys
import os
import time
from modules.driver import factory as driver_factory

driver = driver_factory()

driver.get('https://google.co.jp/')

time.sleep(5)

driver.quit()
