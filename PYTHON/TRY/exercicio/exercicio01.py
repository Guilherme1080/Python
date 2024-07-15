i = 0 
soma = 0 
while i < 10:
    try:
        x = int(input("Digite um numero: "))
        soma += x
        i+=1
    except:
        print("valor invalido!!! tente novamente")

print(soma)