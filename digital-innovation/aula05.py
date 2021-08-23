# 05 - Como organizar os dados em uma lista ou tupla e realizar operações com elas

lista = [1,3,5,7]
#print(lista)
animal = ['cachorro', 'gato', 'cavalo', 'elefante']

print(animal)
# Acessando elementos de uma lista
print(animal)

# Percorrendo uma lista com um FOR
soma = 0
for x in lista:
    print(x)
    soma += x
    print(soma)
print("\n Algumas operações com lista")

# Somar elementos de uma lista
print("Somar: ",sum(lista))

# Maior valor de uma lista
print("Maior valor: ", max(lista))

# Menor valor de uma lista
print("Menor valor: ", min(lista))

# String também funcional
print("Menor valor: ", min(animal))

# Verificar se tem um elemento na lista
if 'lobo' in animal:
    print("\n Existe um animal: ")
else:
    print("Não existe animal na lista: ")

# Incluir novos registro na lista
