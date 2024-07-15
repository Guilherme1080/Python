def reverso(n1 = int):
    reverso = str(abs(n1))[::-1]
    res = int(reverso)
    return res

n1 = int(input("digite um numero: "))
print(reverso(n1))
    