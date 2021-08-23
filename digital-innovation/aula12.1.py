# 12 - Instalando e utilizando pacotes em Python e realizar requisição com requests
import requests

def retorna_pokemon(pokemon):
    # Adicionar a API do pokemon
    response = requests.get("https://pokemon.com.br/ws/{}/json/".format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


if __name__ == '__main__':
    dados_pokemon = retorna_pokemon(['sprites']['front_shiny'])