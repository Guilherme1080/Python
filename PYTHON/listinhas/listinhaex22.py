# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente 
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.
dia = int(input("digite um numero entre 1 e 7: "))
if(dia == 1):
    print("hoje é domingo")
elif(dia == 2):
    print("hoje é segunda")
elif(dia == 3):
    print("hoje é terça")
elif(dia == 4):
    print("hoje é quarta-feira")
elif(dia == 5):
    print("hoje é quinta-feira")
elif(dia == 6):
    print("hoje é sexta-feira")
elif(dia == 7):
    print("hoje é sabadão")
else:
    print("numero invalido")