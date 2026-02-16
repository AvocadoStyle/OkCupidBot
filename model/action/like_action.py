import time

from selenium.common import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from model.Utilities.operation_utils import sleep_decorator
from model.action.browser_action import BrowserAction
from model.action.operation_action import OperationAction
from model.driver.browser_driver import BrowserDriver


class Like(OperationAction):
    def __init__(self, browser_driver: BrowserDriver, browser_action: BrowserAction):
        super().__init__(browser_driver=browser_driver, browser_action=browser_action)

    def close_widget_superlike_suggest(self):
        try:
            # self.browser_driver.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/button[2]").click()
            element = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/div/button[2]"))
            )
            element.click()
        except NoSuchElementException as e:
            print(f"There are not open pop-widgets,"
                  f"Will not close any widget, Expected behavior, Expected behavior!")
        except TimeoutException as e:
            print("There isn't pop-out widgets, Expected behavior!")
        except Exception as e:
            print("bad thing happend")
            self.browser_driver.driver_refresh()

    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def like(self):
        try:
            self.browser_driver.driver_refresh()
            self.browser_action.goto_discover_swipe_section()
            # LIKE button
            search = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "dt-action-buttons-button"))
            )[1]
            search.click()
            self.close_widget_superlike_suggest()
        except IndexError as e:
            """
            Nothing to like or dislike anymore
            """
            self.browser_driver.driver_refresh()
            self.browser_action.goto_discover_swipe_section()
        except ElementClickInterceptedException as e:
            """
            Can't click the Button, There are many reasons:
            - Webpage scrolled down beyond the objects that clicked
            - We're not in the right page
            """
            self.browser_driver.driver_refresh()
            self.browser_action.goto_discover_swipe_section()
        except Exception as e:
            raise Exception(f"Couldn't like, Check If you have the option to like") from e

    @sleep_decorator(prefix_duration=1, postfix_duration=1)
    def dislike(self):
        try:
            self.browser_driver.driver_refresh()
            self.browser_action.goto_discover_swipe_section()
            # PASS button
            search = WebDriverWait(self.browser_driver.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "dt-action-buttons-button"))
            )[0]
            search.click()
            time.sleep(5)
        except IndexError as e:
            """
            If there is nothing to like or dislike anymore
            """
            pass
        except ElementClickInterceptedException as e:
            """
            Can't click the Button, There are many reasons:
            - Webpage scrolled down beyond the objects that clicked
            - We're not in the right page
            """
            self.browser_driver.driver_refresh()
            self.browser_action.goto_discover_swipe_section()
        except Exception as e:
            raise Exception(f"Couldn't dislike, Check If you have the option to dislike") from e

    def like_quantity(self, quantity):
        print(f"----------------------- start like: quantity={quantity} -----------------------")
        for count in range(quantity):

            self.like()
            print(f"like count={count+1}")

