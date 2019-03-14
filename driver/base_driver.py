from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from setting import Setting as ST


class BaseDriver:
    driver: WebDriver = None

    @classmethod
    def get_driver(cls):
        return cls.driver

    @classmethod
    def init_driver(cls):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Phone",
            "automationName": "UiAutomator2",
            "app": f"{ST.ROOT_PATH}/app/com.xueqiu.android_11.17_203.apk",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "autoGrantPermissions": True,
            "unicodeKeyboard": True,
            "resetKeyboard": True,
        }

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(7)


if __name__ == '__main__':
    BaseDriver().init_driver()
