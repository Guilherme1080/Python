# Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este 
# número. Isto e, janeiro se é 1, fevereiro é 2, e assim por diante.
dia = int(input("digite um numero entre 1 e 12: "))
if(dia == 1):
    print("jan")
elif(dia == 2):
    print("fev")
elif(dia == 3):
    print("mar")
elif(dia == 4):
    print("abr")
elif(dia == 5):
    print("mai")
elif(dia == 6):
    print("jun")
elif(dia == 7):
    print("jul")
elif(dia == 8):
    print("ago")
elif(dia == 9):
    print("set")
elif(dia == 10):
    print("out")
elif(dia == 11):
    print("nov")
elif(dia == 12):
    print("dez")
else:
    print("numero invalido")