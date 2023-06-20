# Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах

from atf import *
from atf.ui import *
from pages.auth import AuthPage
from pages.contacts import ContactsPage


class TestCheckDate(TestCaseUI):
    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'), 'SITE_CONTACTS')
        cls.page = ContactsPage(cls.driver)

    def test_check_date(self):
        date_message = '20 июн'
        author = 'Честный Алексей'
        message = 'Сообщение для автотестов'

        log('Переходим на вкладку диалоги')
        self.page.tabs_dialogs.click()

        log('Проверяем дату сообщения')
        self.page.messages.item(contains_text=message).should_be(ContainsText(date_message))

        log('Переходим на вкладку чаты')
        self.page.tabs_chats.click()
        self.page.message_in_chats.should_be(Visible)

        log('Проверяем автора и дату')
        self.page.message_in_chats.item(contains_text=message).should_be(ContainsText(author))
        self.page.message_in_chats.item(contains_text=message).should_be(ContainsText(date_message))

