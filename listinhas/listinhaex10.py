numero = float(input("digite um numero: "))
if(numero >= 0):
    calculo = numero ** (1/2)
    print(f"o valor é {calculo}")
elif(numero < 0):
    calculo2 = numero * numero
    print(f"o calculo é {calculo2}")