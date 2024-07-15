numero = int(input("Digite um número entre 100 e 9999: "))
if (100 <= numero <= 9999):
        numero_str = str(numero)
        for algarismo in numero_str:
            print(algarismo)
else:
        print("O número deve estar entre 100 e 9999.") 

