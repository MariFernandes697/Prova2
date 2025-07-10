#Pratica 0001 
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'''
for linha in matriz:
    for i in linha:
        print(i)
'''
'''
for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j])

'''
for i in range(len(matriz)):
        linha = " "
        for j in range(len(matriz[i])):
            linha += str(matriz[i][j])
            linha += " "
        print(linha)