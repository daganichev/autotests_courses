# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from time import sleep


sbis_ru = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
login = 'ooomechtest'
password = 'ooomechtest123'
employee = 'Честный Алексей'
message_string = 'Сообщение для автотестирования'

try:
    driver.get(sbis_ru)
    sleep(1)

    line_login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    line_login.send_keys(login, Keys.ENTER)
    sleep(1)
    assert line_login.get_attribute('value') == login, 'Логин не соответствует эталонному'

    line_password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    line_password.send_keys(password, Keys.ENTER)
    assert line_password.get_attribute('value') == password, 'Пароль не соответствует эталонному'
    sleep(5)

    contacts = driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]')
    contacts.click()
    sleep(1)

    contacts_menu = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contacts_menu.click()
    sleep(4)

    plus = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus.click()
    sleep(1)

    search = driver.find_element(By.CSS_SELECTOR, '.controls-StackTemplate__top-area-content input')
    search.send_keys(employee)
    sleep(1)

    person = driver.find_element(By.CSS_SELECTOR, f'[data-qa="person-Information__fio"][title="{employee}"]')
    person.click()
    sleep(2)

    text = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    text.send_keys(message_string)
    sleep(1)

    send = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    send.click()
    sleep(4)

    message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert message.text == message_string, 'Сообщение отсутствует в реестре'

    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.perform()
    sleep(1)

    delete = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete.click()
    sleep(2)

    try:
        message = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item p')
        assert message.text != message_string, 'Не удалось удалить сообщение'
    except selenium.common.exceptions.NoSuchElementException:
        print('Сообщения в реестре отсутствуют')
finally:
    driver.quit()
