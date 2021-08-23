# If / Else
a = int(input("Entre com primeiro bimestre: "))
if a > 10:
    a = int(input("Digitou errado primeiro bimestre: "))

b = int(input("Entre com segundo bimestre: "))
if b > 10:
    b = int(input("Digitou errado Segundo bimestre: "))

c = int(input("Entre com terceiro bimestre: "))
if c > 10:
    c = int(input("Digitou errado terceiro bimestre: "))

d = int(input("Entre com quarto bimestre: "))
if d > 10:
    d = int(input("Digitou errado quarto bimestre: "))

# Calculando a média
media = (a + b + c + d)/4
if a <= 10 and b  <= 10 and c <= 10:
    print(" Resultado da média: {}".format(media))
else:
    print(" informado errado: {}".format(media))


