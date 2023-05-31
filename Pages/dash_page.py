import allure
from selene.support.shared import browser
from selene import have, query, be


class DashPage:
    def publication_news(self):
        with allure.step('Открываем форму отправки новости'):
            browser.element('#news').click()
        with allure.step('Вызываем редактор в поле ввода текста новости'):
            browser.element('.DraftEditorMui5').click()
        with allure.step('Вводим в поле ввода текст новости'):
            browser.element('//div[@class="notranslate public-DraftEditor-content" and @role="combobox"]').type('Новость тест').press_tab()
        with allure.step('Нажимаем кнопку Опубликовать'):
            browser.all('.MuiButton-sizeLarge').element_by(have.text("ОПУБЛИКОВАТЬ")).click()

        with allure.step('Проверяем появление новости в ленте по тексту новости'):
            browser.element('.CommonmarkRender-Paragraph').should(have.text('Новость тест'))
        with allure.step('Вызываем контекстное меню'):
            browser.element('.ContextMenu-Toggle').click()
        with allure.step('В меню выбираем Удалить'):
            browser.all('.ContextMenu-Item').element_by(have.text('Удалить')).click()
        with allure.step('Нажимаем Подтвердить удаление'):
            browser.all('.Confirm-Button').element_by(have.text('Подтвердить')).click()
            browser.element('.CommonmarkRender-Paragraph').should(be.present)


    def should_delete_news(self):
        with allure.step('Проверяем отсутствие новости в ленте по тексту новости'):
            news = browser.element('.CommonmarkRender-Paragraph').should(be.present).get(query.text)
            print('Текст последней публикации в ленте: ',news)
            assert news != 'Новость тест',f'Новость не удалена!!!Текст новости {news}'
