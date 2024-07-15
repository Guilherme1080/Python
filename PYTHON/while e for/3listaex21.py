pares = 0
impares = 1

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o primeiro numero: "))
for numero in range(n1, n2 + 1):
    if numero %2 == 0:
        pares = numero + pares
    else:
        impares = numero + impares
print(f"a soma dos numero pares é {pares}")
print(f"multiplicação dos números ímpares {impares}")