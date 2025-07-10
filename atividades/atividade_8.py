'''
Beecrowd 1019

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''
import math
n = int(input(""))

conversor_horas = n//3600 #para descobrir as horas
n = n % 3600 #resto da divisão inteira para as horas
minutos = n//60 # para descobrir os minutos
n = n % 60 # resto da divisão inteira para os minutos
print(f'{conversor_horas}:{minutos}:{n}')
