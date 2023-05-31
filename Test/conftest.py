import pytest
from selene.support.shared import browser
from selenium import webdriver
from util import attach

# def pytest_addoption(parser):
#     parser.addoption(
#         '--envr',
#         help='Среда, в которой будут запускатся тесты',
#         choises=[dev, stag, prod],
#         default= dev
#     )

@pytest.fixture(scope="function",autouse = True )
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.browser_version = "100.0"
    # Headless

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless=new')
    options.set_capability(
        'selenoid:options',
         {
            "enableVNC": True,
            "enableVideo": True
        }
    )
    browser.config.driver_options = options
    browser.config.driver_remote_url = (
        "https://user1:1234@selenoid.autotests.cloud/wd/hub"
    )
    # envr_value = request.config.getoption('--envr')
    # if envr_value==dev:
    #     envr = '-dev.v5-pre'
    # elif envr_value=='stage':
    #     envr = '-rc.v5-stage'
    # elif envr_value == 'prod':
    #     envr = '.app'
    browser.config.base_url = f'https://test.v5.pryaniky.com'

    browser.config.timeout = 30

    yield browser

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add__screenshot(browser)
    attach.add_video(browser)
    browser.quit()
