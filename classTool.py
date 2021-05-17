import time
from selenium import webdriver

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

    def location(self, driver):
        search_location = driver.find_element_by_class_name("cardsummary-location")
        return search_location.text
    def close(self, driver):
        driver.quit()