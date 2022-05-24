# 3. Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas 
# pessoas são maiores de idade.

cont = 1
maiorDeIdade = 0

while cont <= 3:
    ano = int(input("Digite o ano de nascimento: "))
    idade = 2021 - ano
    if idade >= 18:
        maiorDeIdade += 1
    cont +=1

print("Pessoas com 18 anos ou mais:", maiorDeIdade)