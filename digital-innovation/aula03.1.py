# Condicionais
a = int(input("Entre com primeiro valor: "))
b = int(input("Entre com segundo valor: "))

restoa = a % 2
restob = b % 2

if restoa == 0 or not restob > 0:
    print("foi digitado um número e par: ")
else:
    print("Nenhum número par foi digitado: ")
