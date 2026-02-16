import os
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver import Keys
import time

from model.Utilities.operation_utils import sleep_decorator

BOT_PROFILE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "chrome_bot_profile"))


class BrowserDriver:
    def __init__(self, driver_path, url, auto_install_driver=True):
        self.driver_path = driver_path
        self.auto_install_driver = auto_install_driver
        self.driver = None
        self.url_path_hanlder = UrlPath(url)

    def setupDriver(self):
        """
        Setup the chrome driver using undetected-chromedriver to bypass Cloudflare.
        Uses a dedicated bot profile at chrome_bot_profile/.
        First run: log in manually in the browser, then press Enter in the terminal.
        Next runs: already logged in via saved cookies.
        """
        options = uc.ChromeOptions()
        driver_executable_path = None if self.auto_install_driver else os.path.abspath(self.driver_path)
        driver = uc.Chrome(
            driver_executable_path=driver_executable_path,
            options=options,
            user_data_dir=BOT_PROFILE_DIR,
            version_main=144,
        )
        time.sleep(3)
        driver.set_window_size(1900, 1024)
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
