numero = float(input("digite um numero: "))
numero2 = float(input("digite outro numero: "))
numero3 = float(input("digite um numero: "))
if(numero < numero2 <numero3):
    print("esta em ordem crescente")
elif(numero > numero2 >numero3):
    print("nao esta em ordem crescente")
elif(numero2 < numero <numero3):
    print("nao esta em ordem crescente")
elif(numero3 < numero <numero2):
    print("nao esta em ordem crescente")
elif(numero2 < numero3 <numero):
    print("nao esta em ordem crescente")
