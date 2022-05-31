# Estrutura de dados - Listas
numeros = [0,1,2,3,4,5,6]
num = int(input("Digite um número entre 0 e 6: "))

for i in range(0,7):
    if numeros[i] == num:
        numeros[i] = 7

for i in range(0,7):
    print(numeros[i])
