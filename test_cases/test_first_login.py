import pytest
from selenium import webdriver
from pages.base_file import Basepage
from pages.login_page_verify import Login

@pytest.mark.usefixtures('setup')
class Test_login:


    def test_01_login_valid_user(self):
        self.base_page = Basepage(self.driver)
        self.login = Login(self.driver)
        self.login.click_on_login("piyush.alphabin@gmail.com", "admin123")
        assert self.base_page.get_title() == "Log in to Facebook", "Test Fail"


    def test_02_invalid_user_email_login(self):
        self.base_page = Basepage(self.driver)
        self.login = Login(self.driver)
        self.login.invalid_user_login("piyushhello@gmail.com", "admin")
        if self.base_page.get_text(self.login.error_msg_for_invalid_user) == "The password that you've entered is incorrect.\nForgotten password?":
            assert True
        else:

            self.base_page.take_screenshot("invalid_user")
            assert False


    def test_03_user_invalid_password(self):
        self.base_page = Basepage(self.driver)
        self.login = Login(self.driver)
        self.login.click_on_login("piyush@gmail.com", "passss")
        assert self.base_page.get_title() == "Log in to Facebook"

    def test_04_check_logo_is_visible(self):
        self.base_page = Basepage(self.driver)
        self.login = Login(self.driver)
        self.login.logo_visible()
        self.login.name_display()
        assert self.base_page.get_text(self.login.name_facebook) == "Log in to Facebook"

    def test_05_user_can_click_on_forget_password(self):
        self.base_page = Basepage(self.driver)
        self.login = Login(self.driver)
        self.base_page.do_click(self.login.forgot_password)
        assert self.base_page.get_title() == "Forgotten Password | Can't Log In | Facebook"














