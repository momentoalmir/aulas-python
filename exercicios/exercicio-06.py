# Escreva um programa que receba o preço de dois produtos. Calcule um desconto de
#  8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago.

produto1 = float(input("Digite o valor do produto 1: "))
produto2 = float(input("Digite o valor do produto 2: "))
valor1 = produto1 - (produto1 * 0.08)
valor2 = produto2 - (produto2 * 0.11)
total = valor1 + valor2

print("O valor final a ser pago é", total)