import sys
import os
import time
import selenium
from selenium.webdriver.remote import webdriver


def get_executable_path() -> str:
    """
    selenium.webdriver.Firefox 用の executable path を返す
    """

    bin_path = os.path.abspath('bin/geckodriver.exe')

    if os.path.exists(bin_path):
        # bin/ 配下にドライバーがあればそちらを使用する
        print('downloaded Firefox Driver: [%s]' % bin_path)
        return bin_path

    # 引っかからない場合にダウンロードのパスを表示してみる
    print(
        'Download driver from [https://github.com/mozilla/geckodriver/releases]'
    )
    sys.exit()


def factory() -> webdriver:
    """
    Firefox 用の webdriver が返る
    """
    return selenium.webdriver.Firefox(
        executable_path=get_executable_path()
    )
