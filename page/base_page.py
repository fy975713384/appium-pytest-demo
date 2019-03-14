from SeleniumLibrary.errors import ElementNotFound
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from lxml import etree
from util.operate_yaml import OperateYAML

from driver.base_driver import BaseDriver


class BasePage:
    def __init__(self):
        self.driver = BaseDriver.get_driver()
        self.sec = None

    def _get_element(self, value) -> tuple:
        return OperateYAML().get_data(self.sec, value)

    def find_element(self, value: str) -> WebElement:
        """ 通过从配置文件中读取的元素信息查找元素
        """
        ele_tuple = self._get_element(value)
        tag = str(ele_tuple[0]).lower()
        exp = str(ele_tuple[1]).lower()

        if tag == 'id':
            by = MobileBy.ID
        elif tag == 'ac_id':
            by = MobileBy.ACCESSIBILITY_ID
        else:
            by = MobileBy.XPATH
        try:
            return self.driver.find_element(by=by, value=exp)
        except ElementNotFound:
            self.exception_handler()
            return self.driver.find_element(by=by, value=exp)

    def find_by(self, by=MobileBy.ID, value=None) -> WebElement:
        """ 通过给定的元素信息查找元素
        """
        try:
            return self.driver.find_element(by, value)
        except ElementNotFound:
            self.exception_handler()
            return self.driver.find_element(by, value)

    def find(self, by=None, value: str = None, ) -> WebElement:
        if by is None:
            element = self.find_element(value)
        else:
            element = self.find_by(by, value)
        return element

    def exception_handler(self) -> None:
        """ 处理系统中的冗余弹窗
        """
        black_list = [
            BasePage.by_attr(text='好的'),
            BasePage.by_attr(text='下次再说')
        ]
        page_source = self.driver.page_source
        xml = etree.XML(str(page_source).encode('utf-8'))

        for w in black_list:
            if len(xml.xpath(w) > 0):
                self.driver.find_element_by_xpath(w).click()

    @classmethod
    def by_attr(cls, text=None, ele_id=None) -> str:
        text_selector = ''
        if text is not None:
            text_selector = f'@text="{text}"'
            if ele_id is not None:
                id_selector = f'contains(@resource-id, "{ele_id}")'
                return f'//*[{text_selector} and {id_selector}]'
        return f'//*[{text_selector}]'
