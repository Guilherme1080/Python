vendas = float(input("quantas pao vender hoje: "))
vendas1 = float(input("quantas broas vender hoje: "))

pao = 0.12
broa = 1.50

calculo = pao * vendas
calculo2 = broa * vendas1

soma = calculo + calculo2
desconto = (soma * 10) /100

print(f"o valor arrecadado dos dois produtos juntos é:  {soma}")
print(f"a reserva de 10% equivale a: {desconto}")