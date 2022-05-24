import random

print("---------------------------------")
print("       JOGO DE ADIVINHAÇÃO       ")
print("---------------------------------")

segredo = random.randrange(1,11)
acertou = False
tentativas = 3

for i in range(1, 4):
    print("Você possui",tentativas,"tentativas de 3\n")
    numero = int(input("Digite um número entre 1 e 10: "))
    #print(segredo)

    if(numero < 1 or numero > 10):
        print("** Você deve tentar um número entre 1 e 10 **\n")
        continue

    if numero == segredo:
        acertou = True

    if (acertou):
        print("---------------------------------")
        print("   VOCÊ ACERTOU!!! PARABÉNS!!!   ")
        print("---------------------------------")
        break
    else:
        print("Você errou! Tente novamente\n")
        tentativas -= 1

print("Fim de Jogo")