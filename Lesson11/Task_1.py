# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = 'https://sbis.ru/'
browser = webdriver.Chrome()

try:
    browser.get(sbis_site)
    sleep(3)
    assert browser.current_url == sbis_site, 'Открыт не тот сайт'

    contacts_tab = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link[href="/contacts"]')
    assert contacts_tab.text == "Контакты", 'Кнопка Контакты не найдена'
    assert contacts_tab.is_displayed(),  'Кнопка контакты не отображается'
    contacts_tab.click()
    sleep(3)

    tensor_banner = browser.find_element(By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor'
                                                          '[href="https://tensor.ru/"]')
    assert tensor_banner.is_displayed(), 'Баннер Тензор не отображается'
    tensor_banner.click()
    sleep(3)

    browser.switch_to.window(browser.window_handles[-1])

    block_power_in_people = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content '
                                                                  '.tensor_ru-Index__card-title')
    assert block_power_in_people.text == 'Сила в людях', 'Блок "Сила в людях отсутствует"'

    detailed_link_in_block = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
    browser.execute_script("arguments[0].scrollIntoView();", detailed_link_in_block)
    assert detailed_link_in_block.text == 'Подробнее', 'Текст кнопки Подробнее не соответствует эталонному'
    assert detailed_link_in_block.is_displayed(), 'Кнопка подробнее не отображается'
    detailed_link_in_block.click()
    sleep(3)

    assert browser.current_url == 'https://tensor.ru/about', 'Неверно открыт сайт tensor.ru/about'

finally:
    browser.quit()
