import flet as ft
from Task.processo import etapa_processo
from end import endpoints
import os
from Task.login import logar
from function.read_dataframe import ler_arquivo
import pandas as pd
from function.logger import log
from function.config import load_environment

load_environment()
url = endpoints['TRI']

import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    base_path = Path(sys._MEIPASS)
else:
    base_path = Path(__file__).parent

img_path = base_path / "img"
function_path = base_path / "function"
src_path = base_path / "src"
task_path = base_path / "Task"


def main(page: ft.Page):
    page.title = "Automação da Eduardinha"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    log.info('Automação iniciada')

    df = None
    username_input = ft.TextField(label="Usuário", width=300, color=ft.colors.BLACK)
    password_input = ft.TextField(label="Senha", password=True, width=300, color=ft.colors.BLACK)

    def importar(e):
        nonlocal df
        try:
            file_path = ler_arquivo()
            df = pd.read_excel(file_path, dtype=str)
            log.success('Planilha Importada: ' + file_path)
            page.add(ft.Text("Importação concluída com sucesso!", size=20, color=ft.colors.GREEN))
        except Exception as ex:
            log.warning('Erro ao importar planilha')
            page.add(ft.Text("Erro na importação", size=20, color=ft.colors.RED))

    def iniciar_automacao(e):
        nonlocal df
        usern = username_input.value.strip()
        passw = password_input.value.strip()

        if not usern or not passw:
            log.warning("Usuário ou senha não preenchidos!")
            page.add(ft.Text("Por favor, insira usuário e senha!", size=20, color=ft.colors.RED))
            return

        if df is None:
            log.info('Nenhuma Planilha foi importada!')
            page.add(ft.Text('Nenhuma Planilha foi importada!', size=20, color=ft.colors.RED))
            return

        try:
            logar(url, usern, passw)
            etapa_processo(df)
            page.add(ft.Text(log.success('Automação iniciada!'), size=20, color=ft.colors.GREEN))
        except Exception as ex:
            page.add(ft.Text(log.critical('Erro na automação'), size=20, color=ft.colors.RED))

    def sair(e):
        log.info("Automação fechada")
        os._exit(0)

    background = ft.Container(
        image_src=str(img_path / "fundo.jpeg"),
        image_fit=ft.ImageFit.COVER,
        expand=True,
        content=ft.Row(
            [
                ft.Container(
                    bgcolor=ft.colors.with_opacity(0, ft.colors.BLACK),
                    border_radius=20,
                    padding=30,

                    content=ft.Column(
            [
                        ft.Text("Bem-vindo à Automação da Eduardinha", size=30, weight="bold",
                                font_family="Arial Black", color=ft.colors.BLACK),
                        username_input,
                        password_input,
                        ft.ElevatedButton("Carregar Planilha", on_click=importar),
                        ft.ElevatedButton("Iniciar Automação", on_click=iniciar_automacao),
                        ft.ElevatedButton("Sair", on_click=sair),
                    ],

                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    page.add(background)


ft.app(target=main)
