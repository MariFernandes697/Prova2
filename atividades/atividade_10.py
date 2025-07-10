'''
Beecrowd 1038

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''
#Lanche
a, b = map(float, input().split())

if (a == 1):
    produto = "Cachorro Quente"
    preco = 4.00
elif (a == 2):
    produto = "X-Salada"
    preco = 4.50
elif (a == 3):
    produto = "X-Bacon"
    preco = 5.00
elif (a == 4):
    produto = "Torrada simples"
    preco = 2.00
elif (a == 5):
    produto = "Refrigerante"
    preco = 1.50
else:
    exit()

total = b * preco
print(f'Total: R$ {total:.2f}')