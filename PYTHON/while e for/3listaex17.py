numero = int(input("digite um numero: "))
numero_impar = 0
lista = []
if (numero > 0):
    for i in range(numero):
        lista.append(numero_impar)
        numero_impar += 1
        soma = sum(lista) + numero
    print(soma)
        
else:
    print("numero invalido")