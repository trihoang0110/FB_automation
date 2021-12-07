from selenium import webdriver
from Automate import constant as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import os
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)


class Facebook(webdriver.Chrome):
    def __init__(self, driverpath='C:\\seleniumDriver', teardown=False, options=chrome_options):
        self.driver_path = driverpath
        self.chrome_options = options
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super().__init__(chrome_options=self.chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def access_site(self):
        self.get(const.base_url)

    def login(self, email=None, password=None):
        username = self.find_element(By.ID, 'email')
        username.send_keys(email)
        pw = self.find_element(By.ID, 'pass')
        pw.send_keys(password)
        login_button = self.find_element(locate_with(By.TAG_NAME, "button").below(pw))
        login_button.click()

    def choose_page(self, page):
        search_page = self.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_page.click()
        search_page.send_keys(f'{page}')
        target_page = self.find_element(By.XPATH, "//li[@id='dir_nav_sts:237635394456373']/div")
        target_page.click()













