import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.user.credentials import User
from model.driver.browser_driver import BrowserDriver
from model.action.like_action import Like


class OkCupidSelenium:
    def __init__(self, user_name, password, driver_path, url):
        self.browser_driver = BrowserDriver(driver_path, url)
        self.user_credentials = User(user_name, password)
        self.like_action = None
        self.initialize_objects()

    def initialize_objects(self):
        """
        The main initializer of all the handlers
        """
        # Setup the driver object
        self.browser_driver.setupDriver()
        self.like_action = Like(self.browser_driver)
        print("hey")




















    def login(self, driver):
        search = driver.find_element_by_class_name("c0J0grIjyKY6YuiL9OO7")
        search.click()
        time.sleep(2)
        search = driver.find_element_by_name("username")
        time.sleep(2)
        search.send_keys(self.user_credentials.user_name)
        search = driver.find_element_by_name("password")
        time.sleep(2)
        search.send_keys(self.user_credentials.password)
        time.sleep(2)
        search = driver.find_element_by_class_name("login-actions-button")
        search.click()
        time.sleep(10)

    def message(self, driver, contain, people):
        people_main = people
        disturb = 0
        cnt_row = 1
        cnt_col = 1
        while people > 0:
            print(f"---- Starting once again ----")
            print(f"Sent message to people={people}")
            print(f"Send message goal={people_main}")
            print(f"disurbed times={disturb}")
            # first of all we'll refresh
            self.driver_refresh(driver)
            # press on the "Likes" in the menu
            try:
                search = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id=\"nav_ratings\"]"))
                )
                search.click()
            except Exception as e:
                disturb = self.disturbed(disturb)
                self.driver_refresh(driver)
                continue
            # in the "Likes" press "you like"
            try:
                self.driver_refresh(driver)
                search2 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/section/div/nav/div/span[3]/a"))
                )
                search2.click()
                time.sleep(1)
                self.driver_refresh(driver)
                time.sleep(4)
            except Exception as e:
                disturb = self.disturbed(disturb)
                self.driver_refresh(driver)
                time.sleep(2)
                continue
            # press on the first profile
            try:
                self.driver_refresh(driver)
                time.sleep(3)
                search3 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[@id=\"userRows-app\"]/div/main/div/div/div/div[2]/div[{cnt_row}]/div[{cnt_col}]/div"))
                )
                search3.click()
                time.sleep(2)
                self.driver_refresh(driver)
                time.sleep(2)
            except Exception as e:
                disturb = self.disturbed(disturb)
                print("Cannot press on the first profile! In the 'You Like' section")
                self.driver_refresh(driver)
                time.sleep(2)
                continue
            print("debug2")
            time.sleep(3)
            # inside the profile press "message" button
            try:
                time.sleep(1)
                search4 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[2]/div")))
                search4.click()
                time.sleep(1)
            except Exception as e:
                disturb = self.disturbed(disturb)
                print("Trying to press on the 'message' box but it fails!")
                self.driver_refresh(driver)
                continue
            # inside the message box send items
            try:
                time.sleep(1)
                search5 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/textarea")))
                time.sleep(1)
                search5.send_keys(contain)
                time.sleep(2)
            # if their message box is full or already sent msg  other disturb, it pass the profile+exit from the profile
            except Exception as e:
                try:
                    time.sleep(1)
                    disturb = self.disturbed(disturb)
                    search5 = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/button/i")))
                    time.sleep(2)
                    search5.click()
                    time.sleep(2)
                # it will try to send a message with a different message box
                except Exception as e:
                    try:
                        search5 = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located(
                                (By.XPATH,
                                 "/html/body/div[1]/main/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/textarea")))
                        time.sleep(2)
                        search5.send_keys(contain)
                        search5.send_keys(Keys.RETURN)
                        time.sleep(2)
                    except Exception as e:
                        self.driver_refresh(driver)
                        continue
                    # will exit now
                    try:
                        search5 = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located(
                                (By.XPATH,
                                 "/html/body/div[1]/main/div/div[1]/div[2]/div/div[1]/div/button[2]")))
                        search5.click()
                        people -= 1
                        self.driver_refresh(driver)
                        continue
                    except Exception as e:
                        self.driver_refresh(driver)
                        continue

                # exit the profile + refresh and continue to the next profile (while loop again)
                try:
                    # time.sleep(1)
                    # search5 = WebDriverWait(driver, 20).until(
                    #     EC.presence_of_element_located(
                    #         (By.XPATH, "/html/body/div[1]/main/div/div[3]/div[1]/div/div/div[3]/div/button[1]/div")))
                    # search5.click()
                    # time.sleep(2)
                    driver.refresh()
                    # time.sleep(5)
                    continue
                finally:
                    pass
            print("debug4")
            # press send button after insert the message inside the message box
            try:
                search6 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[3]/button")))
                search6.click()
            except Exception as e:
                print("we're fucked up.")
            # exit from the message box
            try:
                time.sleep(2)
                search6 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/button/i")))
                search6.click()
            except Exception as e:
                disturb = self.disturbed(disturb)
                print("Can't get out from the message box, Will continue to the next")
                continue
            time.sleep(5)
            # refresh the list
            driver.refresh()
            time.sleep(5)
            people -= 1

    def location(self, driver):
        search_location = driver.find_element_by_class_name("cardsummary-location")
        return search_location.text