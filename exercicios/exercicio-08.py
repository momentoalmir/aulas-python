# Escreva um algoritmo que receba 7 valores digitados pelo usuário 
# e no final exiba o maior número.

cont = 1
numero = 0
maior = 0

while cont <= 7:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    cont += 1

print("O maior número digitado foi:", maior)