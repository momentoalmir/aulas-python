# Estrutura de dados - Listas
print("Lista de números")
numeros = [1, 4, 3, 6, 2, 5]
maior = 0
for i in range(0,6):
    print(numeros[i])
    if numeros[i] > maior:
        maior = numeros[i]
        pos = i
print("O maior número é",maior,
      "e ele está na posição",pos+1,"da lista")


