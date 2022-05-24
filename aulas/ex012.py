# Escreva um algoritmo que receba o primeiro termo e a razão de uma PA.
# No final mostre os 10 primeiros termos dessa progressão.

print("PROGRESSÃO ARITMÉTICA")
numero = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
for i in range(1,6):
    print("a",i,"...",numero)
    numero = numero + razao

print("PROGRESSÃO GEOMÉTRICA")
numero = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
for i in range(1,6):
    print("a",i,"...",numero)
    numero = numero * razao
