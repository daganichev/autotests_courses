from atf.ui import *
from controls import *


class ContactsPage(Region):
    messages = ControlsListView(By.CSS_SELECTOR, '[data-qa="list"].Hint-ListWrapper_list', 'Список сообщений')
    tabs_dialogs = Sbis3ControlTabs(By.CSS_SELECTOR, '[data-name="dialogs"]', 'Вкладка "Диалоги"')

    move = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MoveDialog__scroll', 'Диалог перемещения')
    chats_folders = ControlsListView(By.CSS_SELECTOR, '.msg-dialogs-folder', 'Папки сообщений')
    close_tag = ControlsButton(By.CSS_SELECTOR, '.icon-Close', 'Кнопка удаления папки/тэга на сообщении')

    tabs_chats = Sbis3ControlTabs(By.CSS_SELECTOR, '[data-name="by_people"]', 'Вкладка Чаты')
    message_in_chats = ControlsListView(By.CSS_SELECTOR, '[data-qa="list"].msg-CorrespondenceDetail__view',
                                                         'Список сообщений в чатах')

    tags_choice = Sbis3ControlsListView(By.CSS_SELECTOR, '.controls-ListView__item_default-topPadding_l', 'Выбор тега')
    tags_folders = ControlsListView(By.CSS_SELECTOR, '.msg-tag-list', 'Папки тэгов')

    def check_load(self):
        self.messages.check_load()
