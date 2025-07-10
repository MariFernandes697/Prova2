'''
Beecrowd 1013

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''
#Descobrindo o maior número 
a, b, c = map(int, input().split())
maior_entre_ab = (a + b + abs (a-b))//2
#abs retorna o valor absoluto de um número
maior_com_c = (maior_entre_ab + c + abs(maior_entre_ab - c))//2

print(f'{maior_com_c} eh o maior')