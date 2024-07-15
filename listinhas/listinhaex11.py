numero = float(input("digite um numero: "))
if (numero > 0):
    calculo = numero * numero 
    calculo2 = numero ** (1/2)
    print(f"o numero elevado é {calculo}")
    print(f"a raiz desse numero é {calculo2}")
else:
    print("esse numero é invalido")