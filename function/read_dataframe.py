from logging import exception
import pandas as pd
import pyperclip
from tkinter import filedialog
from function.logger import log


def ler_arquivo():
    return filedialog.askopenfilename(title="Selecione o arquivo BASE DE DEVEDORES",filetypes=[("Arquivos Excel", "*.xlsx *.xls")])


def copiar(valor: str, date: bool = False, time: bool = False):
    try:
        if date and not time:
            valor = pd.to_datetime(valor, format='%d/%m/%Y', errors='coerce')
            if pd.notnull(valor) and valor.year > 1900:  # Ignorar anos inválidos
                valor = valor.strftime('%d/%m/%Y')  # ✅ Formata corretamente
            else:
                log.error('Data inválida')
                return None

        if time and not date:
            valor = pd.to_datetime(valor, format='%H:%M:%S', errors='coerce')
            if pd.notnull(valor):
                valor = valor.strftime('%H:%M:%S')  # ✅ Formata corretamente
            else:
                log.error('Hora inválida')
                return None

        if pd.notnull(valor):
            valor_final = str(valor)
            pyperclip.copy(valor_final)
            log.success(f'Valor Copiado: {valor_final}')
            return valor_final
        else:
            log.error('Erro ao processar o valor.')
            return None

    except Exception as e:
        log.error(f'Erro: {e}')
        return None

def copiar2(valor):
    try:
        if isinstance(valor, pd.Timestamp):
            valor = valor.strftime('%d/%m/%Y')

        elif isinstance(valor, str):
            valor = pd.to_datetime(valor, errors='coerce')
            if pd.notnull(valor):
                valor = valor.strftime('%d/%m/%Y')

        if pd.notnull(valor):
            pyperclip.copy(valor)
            log.success('Valor Copiado!')
            return valor
        else:
            log.warning('Valor é nulo, nada copiado.')
            return None

    except Exception as e:
        log.error(f"Erro ao copiar valor: {e}")
        return None