import classTool
from classTool import OkCupidSelenium

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    user_name = "e@domain.com"
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




