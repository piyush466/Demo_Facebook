import pytest
from selenium import webdriver


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login.php/")
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
