preco = float(input("digite o valor: "))
if(preco <= 50):
    novopreco = preco + (preco * 0.05)
elif(preco > 50 and preco <= 100):
    novopreco = preco + (preco * 0.10)
else:
    novopreco = preco + (preco * 0.15)
    print(novopreco)