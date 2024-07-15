# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma 
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se 
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”
numero = input("digite um numero: ")
pos = (numero[0])
pos2 = (numero[1])
pos3 = (numero[2])
var = int(pos)
var2 = int(pos2)
var3 = int(pos3)
soma = var + var2 + var3
if(var <= 0 and var2 <= 0 and var3 != 0):
    print(soma)
elif(var <= 0 and var2 != 0 and var3 != 0):
    print(soma)
elif(var <=0 and var2 <=0 and var3 <=0):
    print("numero inválido")
if(var >0):
    print(soma)

# Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda 
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi 
# aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

nota = float(input("digite sua primeira nota: "))
nota2 = float(input("digite a sua segunda nota: "))
nota3 = float(input("digite a sua terceira nota: "))
calculo = (nota + nota2) + (nota3 * 2) *10 /4
if(calculo >= 60):
    print(f"parabens vc está aprovado {calculo}")
else:
    print("vc está reprovado")
