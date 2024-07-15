numero = int(input("quantas vezes vc deseja digitar o numero: "))
contador = 0
lista = []
while numero > contador:
    lista.append(float(input("digite um numero: ")))
    contador += 1
for item in lista:
    print(item)
print(f"o maior numero da sua lista é: ")
print(max(lista))

