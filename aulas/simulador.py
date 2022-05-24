# Aula de TPA - Professor Júnior Gonçalves 
# Algoritmo para Simulação de Investimento no Tesouro Direto

while True:
    print("---------------------------------")
    print("   Seja bem-vindo(a) ao Mybank   ")
    print("    SIMULADOR DE INVESTIMENTO    ")
    print("---------------------------------")
    print("Títulos disponíveis:")
    print("1 - Tesouro Prefixado 2024")
    print("2 - Tesouro Prefixado 2026")

    titulo = int(input("Qual título você gostaria de fazer uma simulação?: "))

    # Definindo as variáveis de acordo com o título selecionado
    if titulo == 1:
        juros = 0.169
        tempo = 32
    else:
        juros = 0.192
        tempo = 50
    
    imposto = 0.15
    taxa = 0.0025
    
    # solicitando informações sobre o empréstimo
    inicial = float(input("Qual o valor você quer investir?: "))
    aportes = int(input("Se você for investir todo o mês, qual o valor?: "))
    
    # calculando os valores
    total = inicial + (aportes * tempo)
    bruto = total + (total * juros)
    rendimento = bruto - total
    ir = rendimento * imposto
    b3 = total * taxa
    liquido = bruto - ir - b3

    print("-------------------------------")
    print("    RESULTADO DA SIMULAÇÃO     ")
    print("-------------------------------")
    print("Valor inicial investido: ", inicial)
    print("Aportes de ",aportes," por ",tempo," meses")
    print("Valor total investido ",total)
    print("-------------------------------")
    print("Valor bruto: ", bruto)
    print("I.R.: ", ir)
    print("Taxa da B3: ", b3)
    print("Valor líquido: ", liquido)
 
    print("-------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n: "))

    # se a opção for igual a "n" o programa é encerrado
    if opcao == 'n':
        break

print("Programa encerrado")