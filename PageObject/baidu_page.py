
from poium import Page, Element


class BaiduPage(Page):
    search_input = Element(id_="kw")
    search_button = Element(id_="su")

    def get_title(self):
        return self.driver.title  # 使用 webdriver 获取页