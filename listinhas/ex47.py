valor = 32.50
extra = 44.50
hora = float(input("fala as suas horas trabalhas por mes: "))
hora_extra = float(input("quantas horas extras vc fez: "))
calculo = valor * hora
calculo2 = hora_extra * extra
soma = calculo + calculo2
print(f"o seu salario bruto é de {soma}")
