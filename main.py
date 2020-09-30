from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

class Bot:

    def __init__(self):
        print('started. waiting for command...')

    
    def start_driver(self):
        print('starting chrome webdriver...')
        # options
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")

        # current user agent - Windows
        # list: https://www.whatismybrowser.com/guides/the-latest-user-agent/
        option.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36")

        # option.add_argument("start-maximized")

        # Pass the argument 1 to allow and 2 to block
        prefs = {"profile.default_content_setting_values.geolocation": 2,
                 "profile.default_content_setting_values.notifications": 1}
        option.add_experimental_option("prefs", prefs)

        # find correct version of chromedriver and install it
        self.driver = webdriver.Chrome(chrome_options = option, executable_path = ChromeDriverManager().install())

        self.driver.get("https://web.whatsapp.com/")
        
b = Bot()
