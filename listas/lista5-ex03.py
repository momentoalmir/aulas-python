# 3. Escreva um algoritmo que leia o ano de nascimento de dez pessoas
# e no final mostre quantas pessoas são maiores de idade.

maiorDeIdade = 0

for pessoa in range(10):
    ano = int(input("Digite o ano de nascimento: "))
    idade = 2022 - ano
    if idade >= 18:
        maiorDeIdade += 1

print("Pessoas com 18 anos ou mais:", maiorDeIdade)
