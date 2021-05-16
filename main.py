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

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    user_name = "name@domain.com"
    password = "password"
    ok = OkCupidSelenium(user_name, password, PATH)
    while(True):
        driver = ok.getDriver()
        ok.login(driver)
        while(check_counter):
            location = ok.location(driver)
            print(location)
            for s in saved_locations:
                if(location == s):
                    like_counter += 1
                    print("like: {} people\n".format(like_counter))
                    ok.like(driver)
                    continue
            ok.dislike(driver)
            dislike_counter += 1
            check_counter -= 1
        print("the like counter is: {}\n".format(like_counter))
        print("the dislike counter is: {}\n".format(dislike_counter))
        ok.close(driver)




