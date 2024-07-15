numero = int(input("digite um numero: "))
numero_impar = 0
lista = []
if (numero > 0 and numero %2 == 0):
    for i in range(numero):
        lista.append(numero_impar)
        numero_impar += 2
    for item in lista:
         if item <= numero:
             print(item)
        
else:
    print("numero invalido")
