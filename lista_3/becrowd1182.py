
'''
Beecrowd 1182

Prof. Gregory ----- Aluno(a): Marianna Fernandes
12/06/2025
'''
#Exibir a soma ou média de determinada linha de uma matriz

c = int(input())
operacao = input()

matriz =[]

for _ in range(12):
   coluna = []
   for _ in range(12):
      num =  float(input(''))
      coluna.append(num) 
   matriz.append(coluna)

soma = 0

for l in range(12):
   soma += matriz[l][c]

if operacao == 'S':
   print(f'{soma:.1f}')
else:
   media = soma/12
   print(f'{media:.1f}')