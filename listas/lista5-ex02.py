# 2. Escreva um algoritmo que receba 10 valores digitados pelo usuário 
# e no final exiba o maior número.

cont = 1
numero = 0
maior = 0

while cont <= 10:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    cont += 1

print("O maior número digitado foi:", maior)