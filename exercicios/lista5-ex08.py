# 8. Escreva um algoritmo que receba um nome e três notas e exiba uma mensagem
# diferente para cada um dos casos a seguir:
# A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”; 
# B) Se a média for menor que 7 e maior que 5, exiba a mensagem
#    “Você ficou com média (media) e está de recuperação; 
# C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”.

nome = str(input("Digite seu nome: "))
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))

media  = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 10:
    print("Parabéns", nome, "! Você foi aprovado")
elif media >= 5 and media < 7:
    print("Você ficou com média", media, " e está de recuperação")
elif media >= 0 and media < 5:
    print(nome, "você está reprovado")
else:
    print("Média inválida")
