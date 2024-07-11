from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_file import Basepage


class Login(Basepage):

    username = (By.NAME, "email")
    password = (By.NAME, "pass")
    submit = (By.NAME, "login")
    error_msg_for_invalid_user = (By.CSS_SELECTOR, "[class='_9ay7']")

    def click_on_login(self, email, password):
        self.send_keys(self.username, email)
        self.send_keys(self.password, password)
        self.do_click(self.submit)

    def invalid_user_login(self, email, password):
        self.send_keys(self.username, email)
        self.send_keys(self.password, password)
        self.do_click(self.submit)
        print(self.get_text(self.error_msg_for_invalid_user))

