def Pot(base, expoente):
    for i in range(1, expoente + 1):
        resultado = base ** i
        print(f"{base} ** {i} = {resultado}")

base = int(input("digite a base: "))
expoente = int(input("digite o expoente: "))
Pot(base,expoente)