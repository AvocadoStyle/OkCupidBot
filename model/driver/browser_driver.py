from selenium import webdriver
import time

from selenium.webdriver import Keys

from model.Utilities.operation_utils import sleep_decorator
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.driver = None
        self.url_path_hanlder = UrlPath(url)

    def setupDriver(self, user_cached_data=None):
        """
        Setup the chrome driver.
        :param user_cached_data: If there is user credentials cache data will direct to the folder which its resides.
        """
        options = webdriver.ChromeOptions()
        if user_cached_data:
            options.add_argument(fr"user-data-dir={user_cached_data}")
        # driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=options)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        driver.set_window_size(1900, 1024)  # TODO: fix the magic numbers.
        driver.get(self.url_path_hanlder.url)
        time.sleep(3)
        self.driver = driver

    @sleep_decorator(prefix_duration=2, postfix_duration=2)
    def driver_refresh(self):
        """
        Refreshes the driver/browser, Will raise an exception if there is any.
        """
        try:
            self.driver.refresh()
            print(f"[debug] driver refreshed")
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