sexo = str(input("digite o seu sexo: "))
altura = float(input("digite a sua altura: "))
if(sexo == "h" or "H"):
    calculo = (72.7 * altura) - 58
    print(f"o calculo para seu peso ideal é: {calculo}")
elif(sexo == "M" or "m"):
    calculo2 = (62.1 * altura) - 44,7
    print(f"o calculo para seu peso ideal é: {calculo2}")
