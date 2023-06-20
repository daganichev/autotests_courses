# Пометить сообщение эталонным тегом.
# Убедиться, что тег появился на сообщении,
# а счётчик тегов увеличился.
# Снять тег и проверить.


from atf import *
from atf.ui import *
from pages.auth import AuthPage
from pages.contacts import ContactsPage


class TestMarkerMessageInTeg(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'), 'SITE_CONTACTS')
        cls.page = ContactsPage(cls.driver)

    def test_marker_message_in_teg(self):
        tag_name = 'Тег для автотеста'
        message = 'Сообщение для автотестов'
        self.page.tabs_dialogs.click()

        log('Вешаем тэг на нужное сообщение')
        self.page.messages.item(contains_text=message).select_menu_actions('Пометить')
        self.page.tags_choice.click()

        log('Проверяем тэг на сообщении, слева в папке тэга счетчик')
        self.page.messages.item(contains_text=message).should_be(ContainsText(tag_name))
        self.page.tags_folders.item(contains_text=tag_name).should_be(ContainsText(tag_name + '\n1\n|\n1'))

        log('Удаляем тег с задачи, проверяем что тэг отсутствует на сообщении')
        self.page.close_tag.click()
        self.page.chats_folders.item(contains_text=tag_name).should_not_be(ExactText('\n1\n|\n1'))
        self.page.messages.item(contains_text=message).should_not_be(ContainsText(tag_name))
