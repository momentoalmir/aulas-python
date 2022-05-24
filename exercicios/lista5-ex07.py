# 7. Escreva um algoritmo que receba dois números e exiba para o usuário todos os valores
# intermediários a eles, veja exemplo:
# Primeiro número: 5 
# Segundo número: 15 
# Resultado: 6 7 8 9 10 11 12 13 14

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
while num1 < num2:
    print(num1)
    num1 += 1
print("Programa encerrado")