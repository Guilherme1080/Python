valor = float(input("digite o valor do premio: "))
desconto = (valor * 10) /100
parcela = valor / 3
comissao = (desconto * 5) /100
comissao2 = (valor * 5 ) /100
print(f"o valor do premio é {valor}")
print(f"o desconto é de {desconto}")
print(f"a parcela fica {parcela} em 3 vezes")
print(f"a 1º comissao fica {comissao}")
print(f"a 2º comissao fica {comissao2}")