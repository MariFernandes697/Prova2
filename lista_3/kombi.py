#Definição de função para calcular o fatorial de Anne

def fat(n):
    f = 1
    for x in range(2, n + 1):
        f = f * x
        return f

def kombi(n,p):
    c = fat(n)/ (fat(p) * fat(n - p))
    return c

print(kombi(3,2))