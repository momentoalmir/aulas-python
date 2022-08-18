import random
#importa uma biblioteca para gerar números aleatórios

print("---------------------------------")
print("       JOGO DE ADIVINHAÇÃO       ")
print("---------------------------------")

segredo = random.randrange(1,11)
#print(segredo) # Número sorteado

acertou = False
tentativas = 3

for i in range(1, 4):
    print("Você possui",tentativas,"tentativas de 3\n")
    numero = int(input("Digite um número entre 1 e 10: "))
        
    if numero == segredo:
        acertou = True

    if acertou:
        print("---------------------------------")
        print("   VOCÊ ACERTOU!!! PARABÉNS!!!   ")
        print("---------------------------------")
        break
    else:
        print("Você errou! Tente novamente\n")
        tentativas -= 1

print("Fim de Jogo - O número sorteado foi", segredo)
