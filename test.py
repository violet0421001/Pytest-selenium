
import pytest

from conftest import driver
from PageObject.BaiduPage import BaiduPage
def test_example(driver, url):
    page = BaiduPage(driver)
    page.open('https://www.baidu.com')
    page.search_input("selenium")
    page.search_button()
    assert (page.get_title(),"selenium_百度搜索")




