import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import helpers


@pytest.fixture(params=['firefox', 'chrome'])  
def driver(request):
    if request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = Service(firefox_driver)
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = helpers.create_test_user()
    yield user
    helpers.del_test_user(user["json"]["accessToken"])
