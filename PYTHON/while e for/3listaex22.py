lista = 10
x = []
for i in range (lista):
    x.append(float(input("digite a sua nota e (digite uma nota invalida para sair): "))) 
    for item in x:
        if item > 10 and item < 0:
            print("numero invalido")
        


