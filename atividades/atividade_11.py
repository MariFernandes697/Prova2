'''
Beecrowd 1041

Prof. Gregory ----- Aluno(a): Marianna Fernandes
06/04/2025
'''
#Coordenadas de um ponto

x, y = map(float, input().split())

if (x == 0 and y == 0):
    print("Origem")
elif (x== 0 and y!=0):
    print("Eixo Y")
elif (x!= 0 and y==0):
    print("Eixo X")
elif(x>0 and y>0):
    print("Q1")
elif(x>0 and y<0):
    print("Q4")
elif(x<0 and y>0):
    print("Q2")
elif(x<0 and y<0):
    print("Q3")
else:
    exit()


#Identifica os pontos informados compara os com os pontos de origem e determina o quadrante correto.