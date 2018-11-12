import sys
import os
import time
from modules.driver import factory as driver_factory
from modules.element import factory as element_factory

driver = driver_factory()

driver.get('https://google.co.jp/')

element = element_factory(driver)
element.find('//input[@id="lst-ib"]').send_keys('にょろ')

time.sleep(5)

driver.quit()
