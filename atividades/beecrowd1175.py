'''
Beecrowd 117

Prof. Gregory ----- Aluno(a): Marianna Fernandes
03/07/2025
'''

lista = []
for _ in range(20):
    n = int(input())
    lista.append(n)

for i in range(20):
    print(f'N[{i}] = {lista[19 - i]}')

'''
Faz um laço de repetição que percorre uma lista de 20 valores, pede para o usuário inserir os valores e isere eles na lista
depois a variavel i percorre cada um dos vetores e assume a posição do vetor e imprime, 
e então acessamos o valor do vetor pela lista a partir da ultima posição, no caso posição 19
19 - i : significa que a posição 19 - a posição inicial do vetor: 0, ou seja, inicia pelo valor do próprio vetor 19.

'''