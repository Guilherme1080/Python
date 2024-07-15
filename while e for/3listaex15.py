numero = int(input("digite um numero: "))
numero_impar = 0
lista = []
if (numero > 0 and numero %2 == 0):
    for i in range(numero):
        lista.append(numero_impar)
        dec = sorted(lista, reverse=True)
        numero_impar += 2
    for item in dec:
         if item <= numero:
             print(item)
        
else:
    print("numero invalido")
