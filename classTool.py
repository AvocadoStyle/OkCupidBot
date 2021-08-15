import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class OkCupidSelenium:
    def __init__(self, user_name, password, PATH):
        self._user_name = user_name
        self._password = password
        self._PATH = PATH
        self._okCupidPATH = "https://www.okcupid.com"

    def getDriver(self):
        driver = webdriver.Chrome(self._PATH)
        driver.get(self._okCupidPATH)
        time.sleep(3)
        return driver

    def login(self, driver):
        search = driver.find_element_by_class_name("splashdtf-header-signin-splashButton")
        search.click()
        time.sleep(2)
        search = driver.find_element_by_name("username")
        time.sleep(2)
        search.send_keys(self._user_name)
        search = driver.find_element_by_name("password")
        time.sleep(2)
        search.send_keys(self._password)
        time.sleep(2)
        search = driver.find_element_by_class_name("login-actions-button")
        search.click()
        time.sleep(10)

    def like(self, driver):
        search = driver.find_element_by_class_name("likes-pill-button-inner")
        search.click()
        time.sleep(5)

    def dislike(self, driver):
        search = driver.find_element_by_class_name("pass-pill-button-inner")
        search.click()
        time.sleep(5)

    def message(self, driver, contain, people):
        while(people > 0):
            cnt = 0
            print("people are => {}".format(people))

            # press on the "Likes" in the menu
            try:
                search = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id=\"nav_ratings\"]"))
                )
                search.click()
            finally:pass

            # in the "Likes" press "you like"
            try:
                search2 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id=\"userRows-app\"]/section/div/div/span[3]/a"))
                )
                search2.click()
            finally:pass

            # press on the first profile
            try:
                search3 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id=\"userRows-app\"]/div/main/div/div/div/div[2]/div[1]/div[1]/div"))
                )
                search3.click()
            finally: pass

            # inside the profile press "message" button
            try:
                search4 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[1]/main/div[1]/div[3]/div/div/div[3]/span/div/button[2]")))
                search4.click()
            finally:pass

            # inside the message box
            try:
                search5 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/textarea")))
                search5.send_keys(contain)
            # if their message box is full or other disturb, it pass the profile+exit from the profile
            except:
                search5 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div[2]/div/div[1]/div/button[2]")))
                search5.click()
                # exit the profile + refresh and continue to the next profile (while loop again)
                try:
                    search5 = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(
                            (By.XPATH, "/html/body/div[1]/main/div[1]/div[3]/div/div/div[3]/span/div/button[1]")))
                    search5.click()
                    driver.refresh()
                    time.sleep(5)
                    continue
                finally:
                    pass

            # press send button after insert the message inside the message box
            try:
                search6 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[3]/button")))
                search6.click()
            except:
                print("we're fucked up.")
            # exit from the message box
            try:
                search6 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/main/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[1]/button")))
                search6.click()
            finally:pass
            time.sleep(5)
            # refresh the list
            driver.refresh()
            time.sleep(5)
            people -= 1

    def location(self, driver):
        search_location = driver.find_element_by_class_name("cardsummary-location")
        return search_location.text
    def close(self, driver):
        driver.quit()