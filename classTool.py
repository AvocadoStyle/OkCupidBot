import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        # search = driver.find_element_by_xpath("/html/body/div[1]/main/nav/div/span[1]/a[4]/div/span")
        # print("0")
        # search = driver.find_element_by_xpath("//*[@id=\"nav_ratings\"]")
        # search.click()
        # print("1")
        while(people > 0):
            cnt = 0
            print("people are => {}".format(people))
            search = driver.find_element_by_xpath("//*[@id=\"nav_ratings\"]")
            search.click()
            try:
                search2 = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id=\"userRows-app\"]/section/div/div/span[3]/a"))
                )
                search2.click()
                print("here")
                time.sleep(7)
                search3 = driver.find_element_by_xpath(
                    "//*[@id=\"userRows-app\"]/div/main/div/div/div/div[2]/div[1]/div[1]/div")
                search3.click()
                time.sleep(4)
                print("will check it now!")
                search4 = driver.find_elements_by_class_name("profile-pill-buttons")
                for s in search4:
                    if(cnt == 0):
                        cnt += 1
                    else:
                        k = s.find_element_by_xpath(
                            "/html/body/div[1]/main/div[1]/div[2]/div/div/div[3]/span/div/button[2]")
                        k.click()
                        time.sleep(4)

                m = driver.find_element_by_xpath(
                    "/html/body/div[1]/main/div[1]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/textarea")
                m.send_keys(contain)
                m = driver.find_element_by_xpath(
                    "//*[@id=\"main_content\"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[3]/button")
                m.click()
                time.sleep(4)
                m = driver.find_element_by_xpath(
                    "//*[@id=\"main_content\"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[1]/button/span")
                m.click()
                driver.refresh()
                time.sleep(4)
                people -= 1

            finally: pass
            # print("2")
            # #search2 = driver.find_element_by_xpath("//*[@id=\"userRows-app\"]/section/div/div/span[3]/a")
            # time.sleep(3)
            # search3 = driver.find_element_by_xpath("//*[@id=\"userRows-app\"]/div/main/div/div/div/div[2]/div[1]/div[1]/div")
            # search3.click()
            # print("3")
            # time.sleep(3)


            # search = driver.find_element_by_class_name("pass-pill-button-inner")
            # search.click()
            # time.sleep(5)


    def location(self, driver):
        search_location = driver.find_element_by_class_name("cardsummary-location")
        return search_location.text
    def close(self, driver):
        driver.quit()