# 12 - Instalando e utilizando pacotes em Python e realizar requisição com requests
import requests

def retorna_pagina(url):
    # Retona a página de um site
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_pagina('https://web.digitalinnovation.one/')
    print(response)