numero = float(input("digite um numero: "))
numero2 = float(input("digite outro numero: "))
if(numero > numero2):
    print(f"o numero maior é {numero}")
    soma = numero - numero2
    print(f"a diferença entre ambos é {soma}")
elif(numero2 > numero):
    print(f"o numero maior é {numero2}")
    soma2 = numero2 -numero
    print(f"a difereça entre ambos é {soma2}")
    