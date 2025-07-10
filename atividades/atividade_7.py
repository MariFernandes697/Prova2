'''
Beecrowd 1018

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''

#DECOMPOSIÇÃO DE CÉDULAS

a = int(input(""))
print(a)

if(a>0 or a<1000000):
    notas_100 = a//100
    a = a % 100
    notas_50 = a//50
    a = a % 50
    notas_20 = a//20
    a = a % 20
    notas_10 = a//10
    a = a % 10
    notas_5 = a//5
    a = a % 5
    notas_2 = a//2
    a = a % 2
    notas_1 = a//1
    a = a % 1
    print(f'{notas_100} nota(s) de R$ 100,00')
    print(f'{notas_50} nota(s) de R$ 50,00')
    print(f'{notas_20} nota(s) de R$ 20,00')
    print(f'{notas_10} nota(s) de R$ 10,00')
    print(f'{notas_5} nota(s) de R$ 5,00')
    print(f'{notas_2} nota(s) de R$ 2,00')
    print(f'{notas_1} nota(s) de R$ 1,00')
else:
    exit()
