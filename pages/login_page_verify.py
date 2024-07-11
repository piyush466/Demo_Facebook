from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_file import Basepage


class Login(Basepage):

    username = (By.NAME, "email")
    password = (By.NAME, "pass")
    submit = (By.NAME, "login")
    error_msg_for_invalid_user = (By.CSS_SELECTOR, "[class='_9ay7']")
    logo = (By.CSS_SELECTOR, "[class='_97vu img']")
    name_facebook = (By.CSS_SELECTOR, "[class='_9axz']")
    forgot_password = (By.CSS_SELECTOR, "[class='_97w4']")

    def click_on_login(self, email, password):
        self.send_keys(self.username, email)
        self.send_keys(self.password, password)
        self.do_click(self.submit)

    def invalid_user_login(self, email, password):
        self.send_keys(self.username, email)
        self.send_keys(self.password, password)
        self.do_click(self.submit)
        print(self.get_text(self.error_msg_for_invalid_user))

    def logo_visible(self):
        self.is_display(self.logo)

    def name_display(self):
        self.is_display(self.name_facebook)

