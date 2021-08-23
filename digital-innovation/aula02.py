# O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário

# Interação com o usuário
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

# Operadores Aritiméticos

soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b

print("\n soma : ", soma)
print("\n subtracao : ", subtracao)
print("\n divisao : ", divisao)
print("\n multiplicacao : ", soma)
print("\n Resto da divisão: ", resto)

# Identificar o tipo de uma varivel
print(type(soma))

# Converter um número
print("Converter : " + str(soma))

# Converter texto para número
x = "1"
res = int(x) + 1
print("Converter o valor de String em número: ", res)

# Concatenar
print("Concatenar o resultado: {}".format(res))



