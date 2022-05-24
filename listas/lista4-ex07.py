# 7. Escreva um algoritmo que leia 2 notas de um aluno e calcule a
# média final deste aluno, considerando que a média é ponderada, ou seja,
# o peso das notas são 3 e 7. 

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

media = (n1 * 0.3) + ( n2 * 0.7)

print("A média ponderada é: ",media)
