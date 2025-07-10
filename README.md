# Prova2

Exercícios básicos

#Tabuada

#Objetivo : ler um número e imprimir a sua tabuada de 0 até 10

n = int(input())
i = 0

while i < 11:
    tabuada = n * i
    print(f'{n} x {i} = {tabuada} ')
    i += 1

'''
#Fatorial
'''
n = int(input())
resultado = 1

for i in range(1, n + 1):
    resultado *= i

print(resultado)
'''

'''O i representa cada item do loop, que começa em 1 e vai até o número inserido pelo usuário + 1, 
ou seja i assume o valor de cada número de 1 até n por vez e multiplica em relação ao resultado anterior'''

#Inverter números
'''
lista = []

for i in range(20):
    n = int(input())
    lista.append(n)

for i in range(20):
    print(f'N[{i}] = {lista[19 - i]}')'''

''' O i pode assumir tanto o papel de indice ou valor do vetor, depende de como é utilizado dentro do loop'''

#Vogais
'''
frase = input(' ').lower()
vogais = "aeiou"
qtd_vogais = 0

for letra in frase:
    if letra in vogais:
        qtd_vogais += 1
print(qtd_vogais)

'''

🌀 while em Python – A Estrutura Mais Teimosa da Família
🧠 O que é o while?
O while é um laço de repetição que continua rodando enquanto a condição for verdadeira.
 Ou seja: ele não sabe quando parar, então você precisa dizer isso pra ele! 😅

💡 Estrutura básica:
python
CopiarEditar
while condição:
    # bloco de código que será repetido

✨ Enquanto a condição for verdadeira, o Python vai continuar repetindo o bloco.

🔁 Exemplo simples:
python
CopiarEditar
i = 0
while i < 5:
    print(f"Valor de i: {i}")
    i += 1  # Isso é ESSENCIAL, senão o loop nunca para!

📤 Saída:
less
CopiarEditar
Valor de i: 0
Valor de i: 1
Valor de i: 2
Valor de i: 3
Valor de i: 4


⚠️ Atenção, Mari:
Se você esquecer de alterar a variável de controle (i += 1), o loop vira um loop infinito.
 Python vai rodar até o fim dos tempos... ou até você apertar Ctrl+C em desespero kkkk 😵

🆚 for vs while
Característica
for
while
Quando usar?
Quando você sabe quantas vezes repetir
Quando você não sabe ao certo
Controle automático
Sim, com range()
Não, você mesma controla
Risco de loop eterno
Baixo
Alto, se esquecer o contador
Exemplo clássico
Tabuada, vetores
Menu interativo, login, testes


✨ Exemplo de senha com while:
python
CopiarEditar
senha = ""
while senha != "1234":
    senha = input("Digite a senha: ")
print("Acesso liberado!")

🔐 Enquanto o usuário errar a senha, o loop continua!

📌 RESUMÃO PRA SUA COLINHA:
python
CopiarEditar
# ESTRUTURA DO WHILE:
variável = valor_inicial
while condição:
    # bloco de código
    variável += algo  # ou alteração de controle

# DICA: use while quando você NÃO souber o número exato de repetições




🔠 len() – O que é essa belezinha?
len() é uma função built-in do Python (ou seja, vem pronta da casa), e serve pra contar quantos itens existem em uma coleção.

📚 Significado:
len vem de "length", que significa comprimento, ou seja, o tamanho de algo!

📦 Métodos de list (listas)
Método
O que faz
append(x)
Adiciona o elemento x no final da lista
insert(i, x)
Insere x na posição i (empurra o resto pra frente)
extend(lista2)
Adiciona todos os elementos de outra lista (concatena listas)
pop()
Remove e retorna o último item da lista
pop(i)
Remove e retorna o item na posição i
remove(x)
Remove a primeira ocorrência de x na lista
clear()
Remove todos os itens da lista (esvazia)
index(x)
Retorna o índice da primeira ocorrência de x
count(x)
Retorna quantas vezes o elemento x aparece na lista
sort()
Ordena a lista em ordem crescente (muda a lista original)
reverse()
Inverte a ordem dos elementos da lista
copy()
Retorna uma cópia rasa da lista


Exercícios intermediários

#Matrizes e vetores
'''
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

'''
'''
obs: Na utilização de matrizes não basta apenas fazer o código com a lógica de construção dela e tentar imprimir com um print
Temos que criar um outro loop para imprimir a mesma. Utlizando da função len que irá contar quantos item tem na lista e determinar o comprimento da matriz'''
'''
for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end=" ")
    print()

'''
#Desafio do ChatGPT - Soma dos elementos da Diagonal principal da matriz
'''
matriz = [] #Cria a matriz vazia
soma = 0

for i in range(3): #Constrói as linhas e colunas da matriz
    linha = []
    for j in range(3):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):  #Imprime a matriz
    for j in range(len(matriz)):
        print(matriz[i][j], end=" ")
    print()


for i in range(3): #Faz o somatório da diagonal principal, ou seja, quando o indice da linha for igual ao indice da coluna.
    for j in range(3):
        if i == j:
            soma += matriz[i][j]
print(soma)
'''
#Soma da diagonal secundária
'''
matriz = []
soma_secundaria = 0

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input())
        linha.append(n)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end=" ")
    print()


for i in range(3):
    for j in range(3):
        if j == len(matriz) - 1 - i: #soma invertida ( tamanho da matriz - 1 - indice da matriz)
            soma_secundaria += matriz[i][j]
print(soma_secundaria)

'''
#Matriz quadrada - (linhas == colunas)

#acima da diagonal principal == são os vetores em que a coluna será maior que a linha ( if j > i)
#acima da diagonal secundária ( if j < 11 - i)
#abaixo da diagonal principal (j > i)
#abaixo da diagonal secundaria ( j > 11 - i)

operacao = input()

matriz = []

for i in range(3):
    lista = []
    for j in range(3):
        n = float(input())
        lista.append(n)
    matriz.append(lista)

soma = 0
media_qtd = 0

for i in range(3):
    for j in range(3):
        if j > i:
            soma += matriz[i][j]
            media_qtd += 1

if operacao == 'soma':
    print(f'{soma:.1f}')
elif operacao == 'media':
    print(f'{soma/media_qtd:.1f}')
else:
    pass




Parte que não consegui estudar toda:

🧮 3. Matriz 1190 – Área Direita

Essa é mais desafiadora!

📌 Objetivo: Soma/média dos elementos na “área direita” da matriz 12x12
Visualmente, é essa região:

Só os elementos do lado direito da matriz, com um formato de funil

🎯 Lógica: pega a parte da matriz onde j > i E j > 11 - i

(ou usa índice fixo com ranges decrescentes e crescentes)

Tem um padrão:

linha = 0
coluna_inicio = 12 - 1  # Começa do fim e vai diminuindo
for i in range(1, 6):
    for j in range(12 - i, 12):  # parte direita
        soma += matriz[i][j]
        cont += 1

Depois:

for i in range(6, 11):
    for j in range(i + 1, 12):  # espelha o de cima
        soma += matriz[i][j]
        cont += 1


---

🧩 Outras áreas importantes:

➕ Acima da diagonal secundária:

Diagonal secundária: matriz[i][11 - i]

Para pegar acima, a condição é:

if j < 11 - i

➕ Abaixo da diagonal secundária:

if j > 11 - i


---

🌀 Fibonacci (beecrowd 1151)

📌 Objetivo: imprimir os n primeiros termos da sequência Fibonacci:

a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b


---

📦 Preenchimento de Vetor I (beecrowd 1177)

📌 Objetivo: preencher um vetor de tamanho 1000 com valores de 0 até t-1 repetidamente

t = int(input())
vetor = []

for i in range(1000):
    vetor.append(i % t)
    print(f"N[{i}] = {vetor[i]}")


—

##funções ou subrotinas:


🎯 O que são Sub-rotinas?
Em bom Pythonês:
Sub-rotinas são blocos de código separados que executam tarefas específicas e podem ser chamados sempre que precisar.
Elas também são conhecidas como funções!

💡 Serve pra organizar, reutilizar e modularizar seu código.

🧠 Estrutura de uma sub-rotina (função) em Python:
python
Copiar
Editar
def nome_da_funcao(parametros):
    # bloco de código
    return resultado
🔁 Exemplo básico:
python
Copiar
Editar
def saudacao():
    print("Olá, Mari! Bem-vinda ao mundo das sub-rotinas!")

saudacao()
📤 Saída:

css
Copiar
Editar
Olá, Mari! Bem-vinda ao mundo das sub-rotinas!
⚙️ Com parâmetros:
python
Copiar
Editar
def soma(a, b):
    return a + b

resultado = soma(3, 7)
print(resultado)
📤 Saída:

Copiar
Editar
10
✂️ Exemplo com matriz:
Digamos que você quer calcular a média dos valores de uma matriz. Você pode fazer:

python
Copiar
Editar
def media_matriz(matriz):
    soma = 0
    qtd = 0
    for linha in matriz:
        for valor in linha:
            soma += valor
            qtd += 1
    return soma / qtd
Chamando depois:

python
Copiar
Editar
matriz = [[1, 2], [3, 4]]
print(media_matriz(matriz))  # Saída: 2.5

#sintaxe

def nome_funcao(parâmetros):
    # faz alguma coisa
    return valor

# Chamada:
resultado = nome_funcao(valores)

