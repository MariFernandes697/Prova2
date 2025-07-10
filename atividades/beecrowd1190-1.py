# Lê a operação: 'S' para soma ou 'M' para média
op = input()

# Cria e preenche a matriz 12x12
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

soma = 0
quantidade = 0

# Parte superior da área direita (linhas de 1 a 5)
for i in range(1, 6):
    for j in range(12 - i, 12):  # colunas da direita vão diminuindo
        soma += matriz[i][j]
        quantidade += 1

# Parte inferior da área direita (linhas de 6 a 10)
for i in range(6, 11):
    for j in range(i + 1, 12):  # colunas da direita vão crescendo
        soma += matriz[i][j]
        quantidade += 1

# Imprime o resultado com uma casa decimal
if op.upper() == 'S':
    print(f"{soma:.1f}")
elif op.upper() == 'M':
    media = soma / quantidade
    print(f"{media:.1f}")
