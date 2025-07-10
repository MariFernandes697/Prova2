'''
Beecrowd 1177

Prof. Gregory ----- Aluno(a): Marianna Fernandes
01/07/2025
'''
#Preencher vetor

T = int(input())

sequencia = 0

for i in range(1000):
    print(f'N[{i}] = {sequencia}')
    sequencia += 1

    if sequencia == T:
        sequencia = 0
    
'''
Recebe um valor, esse valor será até onde seguirá a sequência de números, 
depois tem um contador que irá contar as posições do vetor e zerar as mesmas
assim que o valor for igual o da entrada
'''

