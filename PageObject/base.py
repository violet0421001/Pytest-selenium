from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def by_id(self,id):
        return self.driver.find_element(By.ID, id)

    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    #  class  定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    #  XPath  定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    #  CSS  定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    #  获取 title
    def get_title(self):
        return self.driver.title

    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    #  执行 JavaScript 脚本
    def js(self, script):
        self.driver.execute_script(script)

