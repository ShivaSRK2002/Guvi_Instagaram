import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class InstagramAutomation:
    def __init__(self, profile_url):
        self.profile_url = profile_url
        self.driver = None
        self.init_driver()

    def init_driver(self):
        # Initialize the Chrome WebDriver with options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def open_profile(self):
        # Open the Instagram profile URL and maximize the browser window
        self.driver.get(self.profile_url)
        self.driver.maximize_window()

    def get_follow_counts(self):
        try:
            following = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span"))
            )
            followers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button/span"))
            )
            # Print the number of following and followers
            print("The total number of following is:", following.text)
            print("The total number of followers is:", followers.text)
        except (TimeoutException, NoSuchElementException):
            print("Could not find the followers or following count.")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    # URL of the Instagram profile to scrape
    profile_url = "https://www.instagram.com/guviofficial/"
    # Create an instance of the InstagramAutomation class
    instagram_bot = InstagramAutomation(profile_url)
    # Open the Instagram profile
    instagram_bot.open_profile()
    # Retrieve and print the follow counts
    instagram_bot.get_follow_counts()
