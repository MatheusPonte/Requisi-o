import os
import sys


def get_resource_path(relative_path):
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")
   return os.path.join(base_path, relative_path)

IMG = {
    'cookie': get_resource_path('img/cookie.png'),
    'Abrir_Requisicao': get_resource_path('img/Abrir_Requisicao.png'),
    'Requisicao': get_resource_path('img/Requisicao.png'),
    'Honorario': get_resource_path('img/Honorario.png'),
    'Adicionar': get_resource_path('img/Adicionar.png'),
    'Pasta': get_resource_path('img/Pasta.png'),
    'Adverso': get_resource_path('img/Adverso.png'),
    'TipoHonorario': get_resource_path('img/TipoHonorario.png'),
    'ValorEspecie': get_resource_path('img/ValorEspecie.png'),
    'Parcela': get_resource_path('img/Parcela.png'),
    'DataVencimento': get_resource_path('img/DataVencimento.png'),
    'Nota': get_resource_path('img/Nota.png'),
    'Salvar': get_resource_path('img/Salvar.png'),
    'atencao': get_resource_path('img/atencao.png'),
    'ok': get_resource_path('img/ok.png'),
    'HR': get_resource_path('img/HR.png'),
    'dadosgerais': get_resource_path('img/dadosgerais.png'),
}

POSITION = {
    'cookie': (1767, 972),
    'clique': (851, 409),
    'clique2': (660,399),
    'cliqueadv': (830, 417)
}
