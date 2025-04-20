from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as condicao_experada
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import time
import random
import keyboard as kb

from selenium.webdriver.support.wait import WebDriverWait


class Automacao:
    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument("--lang=pt-BR")
        firefox_options.add_argument("--disable-notifications")
        firefox_options.add_argument("--maximize-window")
        self.driver = webdriver.Firefox(options=firefox_options)
        self.wait = WebDriverWait(
            self.driver, 10,
            poll_frequency = 1,
            ignored_exceptions = [
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
        ]
    )
        self.site ="https://www.instagram.com/"
        self.user = "usuario" #username a ser preenchido no login
        self.password = "password" #senha do usuario

    def iniciar(self):
        self.doLogin()
        self.pesquisarInstagram("nvidia")

    def doLogin(self):
        self.driver.get(self.site)
        self.driver.maximize_window()

        user_box = self.wait.until(
            condicao_experada.element_to_be_clickable(
                (By.XPATH, '//input[@name="username"]')
            )
        )
        user_box.click()
        time.sleep(1)
        user_box.send_keys(self.user)

        password_box = self.wait.until(
            condicao_experada.element_to_be_clickable(
                (By.XPATH, '//input[@name="password"]')
            )
        )
        password_box.click()
        time.sleep(1)
        password_box.send_keys(self.password)
        kb.press_and_release("enter")

    def pesquisarInstagram(self, instagram):
        time.sleep(3)
        search_box = self.wait.until(
            condicao_experada.element_to_be_clickable(
                (By.XPATH, '//*[local-name()="svg" and @aria-label="Search"]')
            )
        )
        time.sleep(2)
        search_box.click()
        time.sleep(2)
        search_box_on = self.wait.until(
            condicao_experada.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Search']")
            )
        )
        time.sleep(2)
        search_box_on.send_keys(instagram)
        time.sleep(2)
        search_box_on.send_keys(Keys.DOWN)
        time.sleep(1)
        kb.press_and_release("enter")



teste = Automacao()
teste.iniciar()

