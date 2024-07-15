def  parcelamento():
    valor = float(input("qual o valor do veiculo: "))
    entrada = float(input("digite o valor da entrada: "))
    parcela = int(input("em quantas parcelas vai ser: "))
    calculo = valor - entrada
    if parcela == parcela:
        res = (calculo * parcela) /100
        x = res + calculo
        a = x / parcela
        print(f"o valor das parcelas será {parcela}X de {a:.2f}")
        print(f"a taxa de juros é de {parcela}%")
parcelamento()
