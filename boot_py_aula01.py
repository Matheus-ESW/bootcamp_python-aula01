# 1 - Crie programa que o usuário digita o seu nome e retorna o número de caracteres

# input("Digite seu nome: ")
# print("Seu nome tem " + str(len(input("Digite seu nome novamente para contar os caracteres: "))) + " caracteres.")

# 2 - Criar um programa onde o usuário digite dois valores e apareça a soma

#print(int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))

# 3 - Criar um programa onde o usuário digite dois valores e apareça a soma

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print("A soma dos dois números é: " + str(num1 + num2))

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, 
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus = float(input("Digite o valor do bônus recebido: "))

print(f"Olá, {nome}! o seu bônus recebido foi R$ {(1000 + salario * bonus):.2f}.")