salario_base = float(input("digite seu salario base: "))
desconto = 7
aumento = 5
desconto_salario = (salario_base * desconto) /100
aumento_novo = (salario_base * aumento) /100
novo_salario= desconto_salario + aumento_novo -salario_base
print(novo_salario)