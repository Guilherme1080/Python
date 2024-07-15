presunto = 50
queijo = 50
hamburger = 100
lanche = int(input("qual é a quantidade de lanches vc vai fazer hoje: "))
calculo = presunto / 1000
calculo2 = 2 * queijo / 1000
calculo3 = hamburger / 1000
valor =  calculo * lanche
valor2 =  calculo2 * lanche
valor3 =  calculo3 * lanche 
soma = (calculo + calculo2 + calculo3) *lanche
print(f"vc vai precisar de {valor} de presunto, {valor2} de queijo, {valor3} de hamburger, o total de kg de alimento é {soma}")