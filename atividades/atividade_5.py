'''
Beecrowd 1012

Prof. Gregory ----- Aluno(a): Marianna Fernandes
04/04/2025

'''
#Calculando área de diferentes formas geométricas

a, b, c = map(float, input().split())

pi = 3.14159

area_triangulo_retangulo = a * c / 2
area_circulo_raio = pi * (c**2)
area_trapezio = (a+b) * c / 2
area_quadrado = b**2
area_retangulo = a * b

print(f'TRIANGULO: {area_triangulo_retangulo:.3f}')
print(f'CIRCULO: {area_circulo_raio:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')

