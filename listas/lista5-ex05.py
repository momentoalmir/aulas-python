# 5. Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou,
# por exemplo, o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120

cont = 1
fat = 1

numero = int(input("Digite um número para calcular o seu fatorial: ") )
while cont <= numero:
    fat *= cont
    cont += 1
print("o fatorial de ", numero, " é ", fat)