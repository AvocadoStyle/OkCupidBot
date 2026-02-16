"""Quick test to find what uc.Chrome configuration works."""
import undetected_chromedriver as uc
import time

print("=== Test 1: Basic uc.Chrome (no profile, auto driver) ===")
try:
    driver = uc.Chrome(version_main=144)
    print(f"SUCCESS - opened: {driver.title}")
    driver.get("https://www.okcupid.com")
    time.sleep(3)
    print(f"OkCupid title: {driver.title}")
    driver.quit()
    print("Test 1 PASSED")
except Exception as e:
    print(f"Test 1 FAILED: {e}")

input("Press Enter to run Test 2 (with profile)...")

print("\n=== Test 2: uc.Chrome with user profile ===")
try:
    options = uc.ChromeOptions()
    options.add_argument(r"--profile-directory=Default")
    driver = uc.Chrome(
        options=options,
        user_data_dir=r"C:\Users\eden.r\AppData\Local\Google\Chrome\User Data",
        version_main=144,
    )
    print(f"SUCCESS - opened: {driver.title}")
    driver.get("https://www.okcupid.com")
    time.sleep(3)
    print(f"OkCupid title: {driver.title}")
    driver.quit()
    print("Test 2 PASSED")
except Exception as e:
    print(f"Test 2 FAILED: {e}")
