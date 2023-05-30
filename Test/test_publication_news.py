from selene.support.shared import browser
import allure
from Pages.login_page import LoginPage
from Pages.dash_page import DashPage
from util import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('Публикация и удаление новости в ленте')
def test_publication_news():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options = options)
    browser.config.driver = driver

    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news()

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add__screenshot(browser)
    attach.add_video(browser)


