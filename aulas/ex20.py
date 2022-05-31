print("PROGRESSÃO ARITMÉTICA")
a1 = int(input("Digite o primeiro termo: "))
an = int(input("Digite a quantidade de termos: "))
r = int(input("Digite a razão: "))
for i in range(1,an+1):
    print("a",i,"...",a1)
    a1 = a1 + r
