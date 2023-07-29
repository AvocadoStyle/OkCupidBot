from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException


class BrowserAction:
    def __init__(self, browser_driver):
        self.browser_driver = browser_driver

    def goto_discover_swipe_section(self):
        try:
            search = WebDriverWait(self.browser_driver.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/nav/div/span[1]/a[4]"))
            )
            search.click()
        except TimeoutException as e:
            print("not found the element")
            self.browser_driver.driver_refresh()
            self.browser_driver.driver_close_widgets_escape()
            self.goto_discover_swipe_section()
        except Exception as e:
            raise Exception(f"unfamiliar exception {e}")

    def goto_you_like_section(self):
        pass