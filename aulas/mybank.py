# Algoritmo para Simulação de Empréstimo
# Aula de Lógica - Professor Júnior Gonçalves 

while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("    SIMULADOR DE EMPRÉSTIMO    ")
    print("-------------------------------")

    cliente = str(input("Você já é nosso cliente? s/n: "))

    # Definindo a taxa de juros dependendo do perfil do usuário
    if cliente == 'n':
        tarifa = 35
        score = int(input("Digite seu Serasa Score: "))
        if score < 300:
            juros = 0.2
        elif score < 500:
            juros = 0.15
        elif score < 800:
            juros = 0.1
        elif score < 1000:
            juros = 0.05
    else:
        # se for cliente será utilizado a menor taxa de juros do banco
        juros = 0.04
        tarifa = 0

    # solicitando informações sobre o empréstimo
    valor = float(input("Valor desejado para o empréstimo: "))
    parcelas = int(input("Quantidade de parcelas: "))
    seguro = str(input("Deseja incluir um seguro desemprego no seu empréstimo? s/n: "))

    # calculando os valores do empréstimo
    valor_parcial = valor + (valor * juros)
    total = tarifa + valor_parcial + (valor_parcial * 0.0038)
    if seguro == 's':
        total = total + (total * 0.035)
    valor_parcelas = total / parcelas

    print("-------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("-------------------------------")
    print("Quantidade de parcelas: ", parcelas)
    print("Valor das parcelas: ", valor_parcelas)
    print("Taxa de juros: ", juros*100, "%")
    print("Custo Efetivo Total: ", total)

    print("-------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n"))

    # se a opção for igual a "n" o programa é encerrado
    if opcao == 'n':
        break

print("Programa encerrado")