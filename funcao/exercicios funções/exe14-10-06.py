def calcular(consumo,preco):
    valor = consumo * preco
    return valor
def calcular_consumo(potencia,hora, preco):
    consumo =potencia * hora / 1000
    conta = calcular(consumo,preco)
    return conta
potencia = int(input("digite a potencia do aparelho: "))
tempo = int(input("quanto tempo foi ultilizado no mes: "))
valor = float(input("valor do KWH: "))
banho = calcular_consumo(potencia, tempo, valor)
print("R$: ",banho)