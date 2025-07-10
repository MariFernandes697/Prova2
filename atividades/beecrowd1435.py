'''
Beecrowd 1435

Prof. Gregory ----- Aluno(a): Marianna Fernandes
05/07/2025
'''
#Matriz Quadrada

while True:
    N = int(input())
    if N == 0:
        break

    matriz = [[0 for _ in range(N)] for _ in range(N)]

    for camada in range((N + 1 ) // 2):
        valor = camada + 1 
        for i in range(camada, N - camada):
            for j in range(camada, N - camada):
             matriz[i][j] = valor

    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()