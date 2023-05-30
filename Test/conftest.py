import pytest
from selene.support.shared import browser
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    browser.config.driver_options = options

    browser.config.base_url = 'https://test.app.pryaniky.com'
    browser.config.timeout = 30
    yield

    browser.quit()
