'''
Beecrowd 1044

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''
#Múltiplos
a, b = map(float, input().split())

if( b % a == 0 or a % b == 0):
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")