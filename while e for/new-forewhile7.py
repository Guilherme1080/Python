numero = int(input("digite um número inteiro positivo: "))
if(numero <= 0):
    print("por favor, insira um numero inteiro positivo")
else:
    print("os primeiros", numero, "numero ímpares naturais são: ")
    contador = 1
    while numero > 0:
        print(contador)
        contador += 2
        numero -= 1