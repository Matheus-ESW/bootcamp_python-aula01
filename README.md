# 🐍 Projeto: bootcamp_python-aula01

Este projeto contém exercícios introdutórios em Python desenvolvidos durante a aula 01 do Bootcamp. Os exemplos abordam entrada de dados, manipulação de strings, operações matemáticas e formatação de saída.

---

## 📘 Exercícios

### 1️⃣ Contar caracteres do nome

Solicita ao usuário que digite seu nome duas vezes e exibe o número de caracteres da segunda entrada.

```python
input("Digite seu nome: ")
print("Seu nome tem " + str(len(input("Digite seu nome novamente para contar os caracteres: "))) + " caracteres.")
```

### 2️⃣ Soma de dois valores (versão direta)
Solicita dois números e exibe a soma diretamente.

```python
print(int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: ")))
```

### 3️⃣ Soma de dois valores (versão com variáveis)
Solicita dois números, armazena em variáveis e exibe a soma formatada.

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("A soma dos dois números é: " + str(num1 + num2))
```

### 4️⃣ Saudações com salário e bônus
Solicita nome, salário e bônus, e exibe uma mensagem personalizada com o valor calculado.

```python
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