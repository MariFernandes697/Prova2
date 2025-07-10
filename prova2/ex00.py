'''
#Soma simples

x, y = map(int, input().split())
soma = x + y
print(soma)

#Par ou impar

n = int(input())

if n % 2 == 0:
    print('Par')
else:
    print('Impar')

#Tabuada

#Objetivo : ler um número e imprimir a sua tabuada de 0 até 10

n = int(input())
i = 0

while i < 11:
    tabuada = n * i
    print(f'{n} x {i} = {tabuada} ')
    i += 1

'''
#Fatorial
'''
n = int(input())
resultado = 1

for i in range(1, n + 1):
    resultado *= i

print(resultado)
'''

'''O i representa cada item do loop, que começa em 1 e vai até o número inserido pelo usuário + 1, 
ou seja i assume o valor de cada número de 1 até n por vez e multiplica em relação ao resultado anterior'''

#Inverter números
'''
lista = []

for i in range(20):
    n = int(input())
    lista.append(n)

for i in range(20):
    print(f'N[{i}] = {lista[19 - i]}')'''

''' O i pode assumir tanto o papel de indice ou valor do vetor, depende de como é utilizado dentro do loop'''

#Vogais
'''
frase = input(' ').lower()
vogais = "aeiou"
qtd_vogais = 0

for letra in frase:
    if letra in vogais:
        qtd_vogais += 1
print(qtd_vogais)

'''
