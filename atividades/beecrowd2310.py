'''
Beecrowd 2310

Prof. Gregory ----- Aluno(a): Marianna Fernandes
05/07/2025
'''

#Voleibol

N = int(input())

saques = 0
bloqueio = 0
ataque = 0

acertos_saques = 0
acertos_bloqueio = 0
acertos_ataque = 0

for i in range(N):
    nome_jogador = input()
    s,b, a = map(int, input().split())
    s1, b1, a1 = map(int, input().split())

    saques += s
    bloqueio += b
    ataque += a

    acertos_saques += s1
    acertos_bloqueio += b1
    acertos_ataque += a1

percentual_s = (acertos_saques / saques) * 100
percentual_b = (acertos_bloqueio / bloqueio) * 100
percentual_a = (acertos_ataque / ataque) * 100

print(f'Pontos de Saque: {percentual_s:.2f} %')
print(f'Pontos de Bloqueio: {percentual_b:.2f} %')
print(f'Pontos de Ataque: {percentual_a:.2f} %')