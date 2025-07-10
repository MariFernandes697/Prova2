'''
Beecrowd 1070

Prof. Gregory ----- Aluno(a): Marianna Fernandes
24/04/2025
'''
'''
💡 Beecrowd 1070 - Seis Números Ímpares
📝 Enunciado:
Leia um valor inteiro X. Em seguida, mostre os 6 valores ímpares consecutivos a partir de X, inclusive X se ele for ímpar.
'''

x = int(input(''))
contador = 0

while contador < 6:
    if x % 2 != 0 :
        print(x)
        contador += 1

    x = x + 1

'''
Comece a partir do número informado.

Verifique se ele é ímpar. Se for, conte ele. Se for par, comecará do próximo número.

Continue até encontrar 6 números ímpares.
'''