# 12 - Instalando e utilizando pacotes em Python e realizar requisição com requests
import requests

def retorna_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    print(response.status_code)
# Tipo texto
    print(response.text)
# Formato de dicionario
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

if __name__ == '__main__':
    retorna_cep('01001000')
