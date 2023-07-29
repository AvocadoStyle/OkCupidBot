from selenium import webdriver
import time

from selenium.webdriver import Keys

from model.Utilities.operation_utils import sleep_decorator


class BrowserDriver:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.driver = None
        self.url_path_hanlder = UrlPath(url)

    def setupDriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\edenr\AppData\Local\Google\Chrome\User Data\Profile 1")
        driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        driver.set_window_size(1900, 1024)
        driver.get(self.url_path_hanlder.url)
        time.sleep(3)
        self.driver = driver

    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def driver_refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            raise Exception(f"Couldn't refresh the page, Check the WebDriver") from e

    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def driver_close_widgets_escape(self):
        try:
            webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        except Exception as e:
            pass

    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def driver_close(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise Exception(f"Couldn't close the driver, The Driver maybe still working") from e


class UrlPath:
    def __init__(self, url):
        self.url = url