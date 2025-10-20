🐍 boot_py_aula01.py
Exercícios introdutórios em Python — Bootcamp Cloud: Aula 01

Este arquivo contém exercícios práticos introdutórios em Python, com o objetivo de reforçar conceitos básicos de entrada de dados (input), manipulação de strings, operações matemáticas e formatação de saída (print).

🧩 Estrutura do Script
1️⃣ Contagem de caracteres em um nome

Solicita que o usuário digite seu nome e exibe o número de caracteres digitados.

input("Digite seu nome: ")
print("Seu nome tem " + str(len(input("Digite seu nome novamente para contar os caracteres: "))) + " caracteres.")


Conceitos aplicados:

Função input() para leitura de dados

Função len() para contar caracteres

Conversão de tipos (str())

2️⃣ Soma de dois valores (versão simples)

O usuário digita dois números e o programa retorna a soma imediatamente, sem armazenar em variáveis.

print(int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))


Conceitos aplicados:

Leitura de múltiplos valores

Conversão para inteiro (int())

Operação aritmética de soma

3️⃣ Soma de dois valores (versão estruturada)

Versão mais organizada, utilizando variáveis nomeadas para armazenar os números antes da soma.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("A soma dos dois números é: " + str(num1 + num2))


Conceitos aplicados:

Declaração de variáveis

Operação matemática e concatenação de strings

4️⃣ Cálculo de bônus sobre o salário

Programa principal: solicita o nome, salário mensal e bônus do usuário, e exibe uma mensagem personalizada com o valor total do bônus calculado.

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus = float(input("Digite o valor do bônus recebido: "))

print(f"Olá, {nome}! o seu bônus recebido foi R$ {(1000 + salario * bonus):.2f}.")


Conceitos aplicados:

Tipos numéricos (float)

Operações matemáticas com variáveis

Formatação de strings com f-string

Arredondamento de casas decimais (:.2f)

🎯 Objetivo de Aprendizado

Praticar a interação com o usuário via terminal

Manipular e converter tipos de dados (str, int, float)

Entender o funcionamento básico de entrada e saída em Python

Aplicar lógica simples para resolver problemas práticos

💡 Dica de execução

Para rodar o script no terminal:

python boot_py_aula01.py


Ou, se estiver em um ambiente virtual:

poetry run python boot_py_aula01.py