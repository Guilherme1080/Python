totalnum = 0
pares = 0
while True:
    numero = int(input("digite um numero inteiro (digite 0 para encerrar)"))
    if numero == 0:
        break
    totalnum += 1
    if numero % 2 == 0:
        pares += 1
print("total de numeros lidos é ", totalnum )
print("numero de valores pares", pares)
