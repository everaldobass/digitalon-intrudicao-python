# 03 - Como criar um código em Python que funcione de acordo com a relação das variáveis
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

print("\n Condicionais com IF: ")
# IF
if a > b:
    print("Maior valor: {}".format(a))


print("\n Condicionais com ELSE: ")
# ELSE
if a > b:
    print("O Maior valor: {}".format(a))
else:
    print("O Maior valor: {}".format(b))

print("\n Condicionais com ELIF: ")
# ELIF
if a > b and a > c:
    print("O Maior valor: {}".format(a))
elif b > a and b > c:
    print("O Maior valor: {}".format(b))
else:
    print("O Maior valor: {}".format(c))



