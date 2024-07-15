hora = 40.50
salario = 2500.00
trabalho = float(input("digite as horas trabalhadas: "))
calculo = hora * trabalho
if(calculo > salario):
    soma = (calculo * 11) /100
    soma2 = calculo - soma
    print(f"o seu salario é: {soma2:.2f}")
else:
    print(f"o seu salario é {calculo}")