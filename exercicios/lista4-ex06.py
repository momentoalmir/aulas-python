# 6. Escreva um algoritmo para ler uma temperatura em graus Celsius
# e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão
# é F = (9 * C + 160) / 5, # sendo F a temperatura em Fahrenheit e
# C a temperatura em Celsius.

cel = int(input("Digite a temperatura em graus Celsius: "))
fah = (9 * cel + 160) / 5

print(cel,"graus Celsius em Fahrenheit é", fah)
