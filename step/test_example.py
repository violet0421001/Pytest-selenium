import pytest
from conftest import driver
from PageObject.baidu_page import BaiduPage

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
@pytest.mark.parametrize(
     "params",
    [("selenium", "selenium_百度搜索"),
     ("pytest", "pytest_百度搜索")],
    ids=["case1", "case2"]
)
def test_example(driver,params):
    send, title = params
    page = BaiduPage(driver)
    page.open('https://www.baidu.com')
    page.search_input.send_keys(send)
    page.search_button.click()
    title = page.get_title()
    assert (title,title)




