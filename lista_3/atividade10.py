#Atividade 1
print('Atividade 1\n')
def subtrair(a,b):
    resultado = a - b
    return resultado
print('Resultado da operação:', subtrair(13, 3))
print('Resultado da operação:', subtrair(22, 7))
print('Resultado da operação:', subtrair(15, 9))

#Atividade 2
print('\nAtividade 2\n')

def calcular(n1,n2, op):
    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 - n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    return resultado

print('Resultado da soma:',calcular(15, 5, '+'))
print('Resultado da subtração:',calcular(15, 5, '-'))
print('Resultado da multiplicação:',calcular(15, 5, '*'))
print('Resultado da divisão:',calcular(15, 5, '/'))

