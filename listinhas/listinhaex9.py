#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do 
#número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
numero = float(input("digite um numero: "))
if(numero >= 0):
    calculo = numero ** (1/2)
    print(f"o valor é {calculo}")
else:
    print(f"numero invalido")
