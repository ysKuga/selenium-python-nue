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

    bin_path = os.path.abspath('bin/chromedriver.exe')

    if os.path.exists(bin_path):
        # bin/ 配下にドライバーがあればそちらを使用する
        print('downloaded Chrome Driver: [%s]' % bin_path)
        return bin_path

    elif os.path.exists(chromedriver_binary.chromedriver_filename):
        # デフォルトを Chrome に
        print('Chrome Driver: [%s]' %
              chromedriver_binary.chromedriver_filename
              )
        return chromedriver_binary.chromedriver_filename

    # 引っかからない場合にダウンロードのパスを表示してみる
    print(
        'Download driver from [https://sites.google.com/a/chromium.org/chromedriver/downloads]'
    )
    sys.exit()


def factory() -> webdriver:
    """
    Chrome 用の webdriver が返る
    """
    return selenium.webdriver.Chrome(
        executable_path=get_executable_path()
    )
