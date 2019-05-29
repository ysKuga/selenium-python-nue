import sys
import os
import time
from modules.driver import factory as driver_factory
from modules.element import factory as element_factory

driver = driver_factory()

driver.get('https://google.co.jp/')

element = element_factory(driver)
element.find('//input[@title="検索"]').send_keys('にょろ')

time.sleep(5)

driver.quit()
