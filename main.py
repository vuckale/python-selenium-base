from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import local_storage
import os
import itertools
path = os.getcwd()
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

        self.driver.get("https://google.com/")


    def get_storage(self):
        '''get the local storage from current session'''
        global path

        # get the local storage
        storage = local_storage.LocalStorage(self.driver)

        with open('/local_storage', 'w') as f:
            print(storage.items(), file=f)

        with open(path+'/local_storage', 'w') as f:
            for key, value in storage.items().items():
                print(key + '\n' + value, file=f)


    def load_storage_param(self, file):
        '''load the data from @param file into local storage (must be parsed)'''
        print("loading storage...")

        # get the local storage
        storage = local_storage.LocalStorage(self.driver)

        with open(file) as f:
            lines = [line.rstrip() for line in f]

        local_storage_dict = dict(itertools.zip_longest(*[iter(lines)] * 2, fillvalue=""))

        for key, value in local_storage_dict.items():
            storage[key] = value

        if len(local_storage_dict) > 0:
            self.driver.refresh()

        self.init_dir()


    def get_cookies(self):
	pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))


    def load_cookies(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            print(cookies)
            self.driver.add_cookie(cookie)

b = Bot()

