'''
Beecrowd 1179

Prof. Gregory ----- Aluno(a): Marianna Fernandes
05/07/2025
'''
#Preenchimento de vetor 4

pares = []
impares = []

for i in range(15):
    numero = int(input())
    if numero % 2 == 0:
        pares.append(numero)
        '''Len é uma função que retorna o número de itens em um objeto'''
        if len(pares) == 5:
            for i in range(5):
                print(f'par[{i}] = {pares[i]}')
            pares.clear()
    else:
        impares.append(numero)
        if len(impares) == 5:
            for i in range(5):
                print(f'impar[{i}] = {impares[i]}')
            impares.clear()

#Para imprir o resto dos números que sobraram na lista
for i in range(len(pares)):
    print(f'par[{i}] = {pares[i]}')

for i in range(len(impares)):
    print(f'impar[{i}] = {impares[i]}')