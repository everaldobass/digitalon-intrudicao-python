# União de conjuntos
conj1 = {1,2,3,4,5}
conj2 = {5,6,7,8,9,10}

conjunt_ouniao = conj1.union(conj2)
print("União: {}".format(conjunt_ouniao))

# Conjunto interseccao
conjunto_interseccao = conj1.intersection(conj2)
print("Intersecção: {}".format(conjunto_interseccao))

# Conjunto diferença
conjunto_diferenca = conj1.difference(conj2)
print("\nDiferença entre 1 e 2: {}".format(conjunto_diferenca))

conjunto_diferenca = conj2.difference(conj1)
print("Diferença entre 2 e 1: {}".format(conjunto_diferenca))

# Diferênça Simétrica - Traz apenas oque é diferente
conjunto_simetrica = conj1.symmetric_difference(conj2)
print("Diferença Simétrica: {}".format(conjunto_simetrica))

