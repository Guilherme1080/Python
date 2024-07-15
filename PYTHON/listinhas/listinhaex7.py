# Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor 
# de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser 
# vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, faça um 
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda 

produto = float(input("digite o valor do preço dos produtos: "))
if(produto < 50.00):
    calculo = (produto * 45) /100
    calculo1 = produto + calculo
    print(f"o valor vendido é de {calculo1}")
elif(produto >= 50.00):
     calculo2 = (produto * 30) /100
     calculo3 = produto + calculo2
     print(f"o calculo foi de {calculo3}")

    
