    # 09 - Gere, copie, mova, escreva e leia informações de arquivos externo
def escrever_arquivo(texto):
    arquivo = open("notas.txt","w") # Pode passar o caminho do arquivos
    arquivo.write("Notas de um Aluno\n")
    arquivo.close()

    # Escrever uma segunda linha
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,"a")
    arquivo.write("texto")
    arquivo.close()

    # Lendo um arquivo de texto
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


# Método para chamar os arquivos
if __name__ == '__main__':
    #escrever_arquivo("Primeira Linha. \n")
    aluno = '\nEveraldo, 10,10,8,8'
    atualizar_arquivo("notas.txt", aluno)
    #ler_arquivo("teste.txt")