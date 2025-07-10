'''
Beecrowd 1180

Prof. Gregory ----- Aluno(a): Marianna Fernandes
02/07/2025
'''
#Menor e Posição

N = int(input())
x = list(map(int, input().split()))

menor_valor = min(x)
posicao = x.index(menor_valor)

print(f'Menor valor: {menor_valor}\nPosicao: {posicao}')