numeros = [0]
while True:
    num = int(input("Entre com um número: "))
    if num != 0:
        numeros.append(num)
        numeros.sort()
        tamanho = len(numeros)
        print("Lista atualizada")
        for i in range (0, tamanho):
            print(numeros[i])
    else:
        break
print("Programa encerrado")
