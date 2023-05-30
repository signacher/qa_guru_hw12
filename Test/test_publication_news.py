import time

import allure

from Pages.login_page import LoginPage
from Pages.dash_page import DashPage

@allure.tag('Web-Publication')
@allure.label('owner', 'Telnov')
@allure.feature('Новость')
@allure.story('Публикация и удаление новости в ленте')
def test_publication_news():
    login = LoginPage()
    login.login_user()

    publication = DashPage()
    publication.publication_news()




