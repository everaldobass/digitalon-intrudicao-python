# Remoção de duplicidade de listas utilizando conjuntos

# Conjunto Subset - Todos os elementos que tem em B tem em A
conjA = {1,2,3}
conjB = {1,2,3,4,5}
conjunto_subset = conjB.issubset(conjA)
print("Subset {}".format(conjunto_subset))

# conjunto Superset - Todos os elementos que tem em A tem em B
conjunto_superset = conjB.issuperset(conjA)
print("Superset {}".format(conjunto_superset))

# Converter uma lista em conjunto
lista = ['cachorro', 'gato', 'gato', 'elefante', 'pato', 'pato']
print(lista)
# Lista em conjunto
lista_animais = set(lista)
print(lista_animais)

# Conjunto em lista
lista_animais = list(lista_animais)
print(lista_animais)



