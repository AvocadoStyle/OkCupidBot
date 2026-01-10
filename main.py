from controller.classTool import OkCupidSelenium
import os
from dotenv import load_dotenv
import time

T = {
    "user_name": os.getenv("USER_NAME"),
    "password": os.getenv("PASSWORD"),
}

if __name__ == "__main__":
    like_counter = 0
    dislike_counter = 0
    check_counter = 1000
    # represents locations
    saved_locations = ["`Akko", "Qiryat Yam", "Haifa", "Qiryat Motzkin", "Qiryat Bialik", "`Afula", "Yoqne`am",
                       "Or `Aqiva", "Tiberias", "Shelomi", "Karmi’el", "Ma`alot", "Hadar HaKarmel"]
    driver_path = "chromedriver.exe"
    okcupid_url = "https://www.okcupid.com"
    user_name = T["user_name"]
    password = T["password"]
    # ok = OkCupidSelenium(user_name, password, PATH)
    contain = "*משחק אותה שלא מתלהב בכלל* מה קורה?"
    # contain = "*משחק אותה שלא מתלהב* מה קורה?"
    # contain = "את ממש מוכרת לי"
    people = 50000
    # gets the cache data path of the user, And if there isn't it will retrieve `None`, And it's valid behavior.
    # such as the path: Chrome\User Data\Profile 1
    usr_cached_data = T.get('user_cache_data')
    ok = OkCupidSelenium(
        user_name=user_name, password=password, driver_path=driver_path, url=okcupid_url,
        user_cached_data=usr_cached_data)
    people_max_qty_to_msg = 40
    while True:
        message_again = ok.message_action.message(msg_to_send=contain)
        # if not message_again:
        #     ok.like_action.like_quantity(quantity=10)
        time.sleep(2)
