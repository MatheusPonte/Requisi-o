import pyautogui as pya
from selenium.webdriver.common.by import By
import time
from function.click_and_fill import click_and_fill
from function.webdriver import WebDriverManager
from function.logger import log

def logar(site, login, senh):
    driver_manager = WebDriverManager()
    browser = driver_manager.get_driver()
    browser.get(site)
    time.sleep(7)
    click_and_fill('cookie','caminho do cookie encontrado','caminho do cookie não encontrado')
    browser.find_element(By.ID, "LOGINprojuris/LoginVO_*_login").click()
    log.success('Login colocado')
    pya.write(login, interval=0.1)
    time.sleep(2)
    browser.find_element(By.ID, "SENHAprojuris/LoginVO_*_login").click()
    pya.write(senh, interval=0.1)
    log.success('Senha colocada')
    time.sleep(1)
    browser.find_element(By.ID, "ext-gen22").click()
    log.success('Logando!')
    time.sleep(10)



