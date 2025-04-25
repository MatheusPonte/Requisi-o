import time
from time import sleep

import pyautogui
import pyperclip
import keyboard as key
from function.logger import log

from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage, search_image_time
from function.read_dataframe import copiar, copiar2


def cadastrar(row):
    time.sleep(5)
    copiar(row["PASTA"])
    searchimage('Pasta', 'Pasta Encontrado!', 'Pasta não encontrado!')
    pyautogui.write('1')
    pyautogui.press("backspace", presses=13)
    time.sleep(2)
    click_and_fill('clique2', 'clique2 encontrado', 'clique2 nao encontrado')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('Adverso', 'Adverso Encontrado!', 'Adverso não encontrado!')
    time.sleep(1)
    click_and_fill('clique2', 'clique2 encontrado', 'clique2 nao encontrado')
    searchimage('Adverso', 'Adverso Encontrado!', 'Adverso não encontrado!')
    time.sleep(1)
    copiar(row["PARTES"])
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    click_and_fill('cliqueadv', 'cliqueadv encontrado', 'cliqueadv não encontrada')
    time.sleep(1)
    searchimage('TipoHonorario', 'TipoHonorario Encontrado!', 'TipoHonorario não encontrado!')
    copiar(row["ATO"])
    time.sleep(4)
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(10)
    searchimage('Parcela', 'Parcela Encontrado!', 'Parcela não encontrado!')
    time.sleep(1)
    pyautogui.write('1')
    time.sleep(1)
    searchimage('ValorEspecie', 'ValorEspecie specie Encontrado!', 'ValorEspecie specie não encontrado!')
    time.sleep(1)
    valor = "{:.2f}".format(float(row["VALOR"])).replace('.', ',')
    key.write(valor)
    #copiar(valor)
    #key.write(valor)
    #pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    searchimage('DataVencimento', 'DataVencimento specie Encontrado!', 'DataVencimento specie não encontrado!')
    copiar2(row["DATA"])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    searchimage('Nota', 'Nota specie Encontrado!', 'Nota specie não encontrado!')
    copiar(row["OBS"])
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    searchimage('Salvar', 'Salvar specie Encontrado!', 'Salvar specie não encontrado!')
    if search_image_time('atencao', 'bloco de atenção encontrado', 'não achado bloco de atenção'):
        searchimage('ok','ok clicado prosseguidno','ok não econtrado')
        sleep(2)
        searchimage('HR','HR clicado prosseguidno','HR não econtrado')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press("backspace")
        searchimage('dadosgerais','dadosgerais clicado prosseguidno','dadosgerais não econtrado')
    else:
        log.info('indo para o proximo cadastro')




