'''
Beecrowd 1557

Prof. Gregory ----- Aluno(a): Marianna Fernandes
05/07/2025
'''
#Matriz Quadrada 2
#Matriz Quadrada 2

while True:
    N = int(input())
    if N == 0:
        break
    matriz = []
    for i in range(N):
        linha = []
        for j in range(N):
            valor = 2 ** (i + j)
            linha.append(valor)
        matriz.append(linha)
    maior_m = matriz[N-1][N-1]
    comprimento = len(str(maior_m))

    for linha in matriz:
        linha_f = ""
        for num in linha:
            linha_f += f"{num:>{comprimento}} "
        print(linha_f.strip())
    print()
