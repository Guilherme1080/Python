camisa_p = 35
camisa_m = 45
camisa_g = 55
p = int(input("quantas camisa pequena: "))
m = int(input("quantas camisa media: "))
g = int(input("quantas camisa grande: "))
calculo = p * camisa_p
calculo2 = m * camisa_m
calculo3 = g * camisa_g
print(f"o total de vendas arrecadado por camisa p é: {calculo}")
print(f"o total de vendas arrecadado por camisa m é: {calculo2}")
print(f"o total de vendas arrecadado por camisa g é: {calculo3}")
soma = calculo + calculo2 + calculo3
print(f"a soma de total ao dia é: {soma}")