import time

import pyautogui

from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.read_dataframe import copiar


def buscar_pasta(value):
    time.sleep(2)
    searchimage('Requisicao', 'Requisicao encontrado!', 'Requisicao não encontrado')
    time.sleep(4)
    searchimage('Abrir_Requisicao', 'Abrir_Requisicao Encontrado!', 'Abrir_Requisicao não encontrado!')
    copiar(value)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    searchimage('Honorario', 'Honorario encontrado!', 'Honorario não encontrado')
    time.sleep(2)
    searchimage('Adicionar', 'Adicionar Encontrado!', 'Adicionar não encontrado!')
