    # 09 - Gere, copie, mova, escreva e leia informações de arquivos externo
def escrever_arquivo(texto):
    arquivo = open("teste.txt","w") # Pode passar o caminho do arquivos
    arquivo.write("Gerando arquivos em Python\n")
    arquivo.close()

    # Escrever uma segunda linha
def atualizar_arquivo(texto):
    arquivo = open("teste.txt","a")
    arquivo.write("Escrevendo uma outra linha\n")
    arquivo.close()

    # Lendo um arquivo de texto
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


# Método para chamar os arquivos
if __name__ == '__main__':
    #escrever_arquivo("Primeira Linha. \n")
    #atualizar_arquivo("Segunda linha\n")
    ler_arquivo("teste.txt")