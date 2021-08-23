### 11 - Gerenciando e criando exceções customizadas com try, except, else e finally
lista = [1, 10]
#a = ""
arquivo = open('teste.txt', 'r')

try:
    divisao = 10/ 1
    numero = lista[1]
    x = a

except ZeroDivisionError:
    print(" Divisão por Zero não é possivel: ")

except ArithmeticError:
    print("Houve erro de operação aritimética")

except IndexError:
    print("Erro invalido da Lista")
    # BaseException a exerção principal
except BaseException as ex:
    print('Error desconhecido. Erro: {} '.format(ex))
else:
    print("Executa quando não ocorre erro: ")
finally:
    print("sempre executa")
    print("Fechando arquivo")
    arquivo.close()
