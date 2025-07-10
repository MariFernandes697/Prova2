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
