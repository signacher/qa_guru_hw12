from selene.support.shared import browser
import allure
from Pages.login_page import LoginPage
from Pages.dash_page import DashPage
from util import attach


@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('Публикация и удаление новости в ленте')
def test_publication_news():
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news()

    attach.add_html(browser)
    attach.add_logs(browser)
    attach.add__screenshot(browser)


