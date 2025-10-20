💻 bootcamp_python-aula01
Este repositório contém os exercícios práticos desenvolvidos durante a Aula 01 do Bootcamp de Python. Os exercícios focam nos conceitos básicos de entrada de dados (input()), manipulação de strings, conversão de tipos (casting) e operações aritméticas simples.

🚀 Funcionalidades e Desafios
Os códigos presentes nesta aula exploram as seguintes tarefas:

1. Contador de Caracteres no Nome
Um programa que solicita o nome do usuário e, em seguida, informa a quantidade total de caracteres (letras e espaços) que o nome digitado possui.

Conceitos:

Função input() para receber dados do usuário.

Função len() para contar o número de caracteres de uma string.

Conversão explícita de tipos (str()) para concatenação na função print().

Código de Exemplo:

Python

# input("Digite seu nome: ")
# print("Seu nome tem " + str(len(input("Digite seu nome novamente para contar os caracteres: "))) + " caracteres.")
2. Calculadora de Soma Simples (Forma Direta)
Programa que pede dois valores numéricos ao usuário e imprime a soma desses valores de forma direta.

Conceitos:

Aninhamento de funções (int(input())).

Conversão de string para int (casting) para permitir a operação de soma.

Código de Exemplo:

Python

# print(int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))
3. Calculadora de Soma Simples (Com Variáveis)
Programa que utiliza variáveis para armazenar os valores digitados pelo usuário antes de realizar e exibir a soma.

Conceitos:

Atribuição de valores a variáveis (num1, num2).

Melhoria na legibilidade do código.

Código de Exemplo:

Python

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print("A soma dos dois números é: " + str(num1 + num2))
4. Gerador de Mensagem de Boas-Vindas com Cálculo de Bônus
Um programa mais completo que solicita nome, salário e bônus, e retorna uma mensagem personalizada com um cálculo financeiro.

Conceitos:

Uso de float() para trabalhar com números decimais (salário e bônus).

F-strings (f"Texto {}") para formatação de saída moderna.

Formatação de valores monetários (:.2f).

Cálculo customizado: Bônus Final = 1000 + (Salário * Bônus Base)

Código Completo:

Python

nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário mensal: "))
bonus = float(input("Digite o valor do bônus recebido: "))

print(f"Olá, {nome}! o seu bônus recebido foi R$ {(1000 + salario * bonus):.2f}.")
🛠️ Como Executar
Para rodar qualquer um dos exemplos de código, você deve ter o Python instalado em sua máquina.

Clone o repositório (ou copie o código que deseja testar).

Salve o código em um arquivo .py (ex: aula01.py).

Execute pelo seu terminal (na pasta onde salvou o arquivo):

Bash

python aula01.py