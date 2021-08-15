import classTool
from classTool import OkCupidSelenium
from dict import *

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    user_name = T["user_name"]
    password = T["password"]
    # ok = OkCupidSelenium(user_name, password, PATH)
    contain = "*משחק אותה שלא מתלהב בכלל* מה קורה?"
    people = 300
    while(True):
        ok = OkCupidSelenium(user_name, password, PATH)
        driver = ok.getDriver()
        ok.login(driver)
        ######################################################################
        # method 1: like dislike method
        # while(check_counter):
        #     location = ok.location(driver)
        #     print(location)
        #     for s in saved_locations:
        #         if(location == s):
        #             like_counter += 1
        #             print("like: {} people\n".format(like_counter))
        #             ok.like(driver)
        #             continue
        #     ok.dislike(driver)
        #     dislike_counter += 1
        #     check_counter -= 1
        # print("the like counter is: {}\n".format(like_counter))
        # print("the dislike counter is: {}\n".format(dislike_counter))
        ####################################################################

        ok.message(driver, contain, people)
        classTool.time.sleep(100)
        ok.close(driver)




