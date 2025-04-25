import time

from Task.buscar_pasta import buscar_pasta
from Task.cadastro import cadastrar
from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.logger import log


def etapa_processo(df):
    time.sleep(2)
    buscar_pasta(df["Nº"][0])
    for index, row in df.iterrows():
        log.info('cadastro do procon iniciado!')
        cadastrar(row)
        log.info('Cadastro completo: ' + row['PARTES'])