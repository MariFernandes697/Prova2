'''
Beecrowd 117

Prof. Gregory ----- Aluno(a): Marianna Fernandes
03/07/2025
'''

T = int(input())

sequencia_fibonacci = [0, 1]
for i in range(2,61):
  sequencia_fibonacci.append(sequencia_fibonacci[i - 1]+ sequencia_fibonacci[i-2])

for _ in range(T):
  n = int(input())
  print(f'Fib({n}) = {sequencia_fibonacci[n]}')


'''
Ler um valor, esse valor será a quantidade de repetição do loop, depois criamos uma lista, que já terá as posições iniciais de 0 1 
Logo após percorremos um loop que irá incerir números de acordo com a lógica da sequencia de fibonacci,  logo após imprimir a sequência.
'''