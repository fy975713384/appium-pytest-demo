from page.base_page import BasePage
from page.search import SearchPage


class HomePage(BasePage):

    def __init__(self):
        super(BasePage, self).__init__()
        self.sec = 'home'
        self._tab_portfolio = self.find('tab_portfolio')
        self.loaded()

    def loaded(self):
        locations = ['foo1', 'foo2']
        while locations[-1] != locations[-2]:
            ele = self._tab_portfolio
            locations.append(ele)

    def to_search(self):
        self._tab_portfolio.click()
        return SearchPage()
