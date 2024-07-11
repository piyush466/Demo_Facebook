import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--env", default="prod")

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")

    if env == "prod":
        url = ("https://www.facebook.com/login.php/")
    elif env == "QA":
        url = ("https://www.Amazon.in")
    else:
        url = ("https://www.facebook.com/login.php/")


    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.quit()
