from controller.classTool import OkCupidSelenium
from dict import *
import time

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    driver_path = "chromedriver.exe"
    okcupid_url = "https://www.okcupid.com"
    user_name = T["user_name"]
    password = T["password"]
    # ok = OkCupidSelenium(user_name, password, PATH)
    # contain = "*משחק אותה שלא מתלהב בכלל* מה קורה?"
    contain = "אז מה את עושה בחיים חוץ מלדגמן?"
    people = 50000
    ok = OkCupidSelenium(user_name, password, driver_path, okcupid_url)
    while True:
        ok.like_action.like()
        time.sleep(10)
        # ok.login(driver)
        # input("type when you're ready")
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

        # ok.message(driver, contain, people)
        # classTool.time.sleep(100)
        # ok.close(driver)




