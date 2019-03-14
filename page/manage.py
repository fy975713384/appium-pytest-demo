from page.base_page import BasePage


class ManagePage(BasePage):
    def __init__(self):
        super(ManagePage, self).__init__()
        self.sec = 'manage'
        self.test_group = 'test_group'

    def add_group(self):
        pass

    def delete_group(self):
        pass

    def add_stock_in_group(self):
        pass

    def delete_stock_in_group(self):
        pass

