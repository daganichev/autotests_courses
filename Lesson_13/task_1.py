# Переместить запись в другую папку и проверить перемещение
# (убедиться в: наличии в папке и увеличении счётчика).
# И вернуть обратно.

from atf import *
from atf.ui import *
from pages.auth import AuthPage
from pages.contacts import ContactsPage


class TestMoveMessageToAnotherFolder(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'), 'SITE_CONTACTS')
        cls.page = ContactsPage(cls.driver)


    def test_move_message_to_another_folder(self):
        folder_name = 'Папка для автотестов'
        message = 'Сообщение для автотестов'

        log('Переходим на вкладку диалоги')
        self.page.tabs_dialogs.click()

        log('Перемещаем сообщение в папку через доп. меню')
        self.page.messages.item(contains_text=message).select_menu_actions('Переместить')
        self.page.move.row(contains_text=folder_name).click()

        log('Проверяем что сообщение в папке, проверяем что сообщение в папке')
        self.page.messages.item(contains_text=message).should_be(ContainsText(folder_name))
        self.page.chats_folders.item(contains_text=folder_name).should_be(ExactText(folder_name+'\n1\n1'))

        log('Убираем сообщение из папки, проверяем что сообщение пропало из папки')
        self.page.close_tag.click()
        self.page.messages.item(contains_text=message).should_not_be(ContainsText(folder_name))
        self.page.chats_folders.item(contains_text=folder_name).should_not_be(ExactText('\n1\n1'))

