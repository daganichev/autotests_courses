from atf.ui import *


class AuthPage(Region):

    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'Логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'Пароль')

    def auth(self, login: str, password: str, site: str):
        self.browser.open(self.config.get(site))
        self.login.should_be(Displayed).type_in(login + Keys.ENTER)
        self.login.should_be(ExactText(login))
        self.password.type_in(password + Keys.ENTER)
