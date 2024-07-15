#A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 
#até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame 
#final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de 
#Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela 
#se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi 
#aprovado. Faça todas as verificações necessárias.
nota1 = float(input("qual foi a sua nota no labolatorio: "))
nota2 = float(input("qual foi a sua nota da avaliação semestral: "))
nota3= float(input("qual foi a sua nota do exame final: "))
calculo = (nota1 + nota2 + nota3) /3
if(calculo <= 2.9):
    print("vc esta reprovado")
elif(calculo >= 3.0 and calculo <= 5.9):
    print("vc esta de exame")
elif(calculo >= 5.9 and calculo <= 10.0):
    print("vc esta aprovado")
else:
    print("nota invalida")