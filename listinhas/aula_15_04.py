nome = input("\n digite seu nome completo:  ")
vencimento = input("\n qual é o dia de vencimento do seu cartão: ")
mes = input("\n digite o mês da sua fatura: ")
valor = float(input("\n digite o valor da sua fatura (exemplo 999.99):  "))

print("-----" * 20)
print(f"\n Olá, {nome}")
print(f"\n A sua fatura com vencimento em {vencimento} de {mes} no valor de R$ {valor} esta fechada")

