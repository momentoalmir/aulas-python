# 8. Escreva um algoritmo para ler dois números e apresente
# a multiplicação deles apenas se o resultado for maior ou igual a 50. 

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
mult = numero1 * numero2

if mult >= 50:
    print("A multiplicação dos números é: ",mult)

print("Programa encerrado")
