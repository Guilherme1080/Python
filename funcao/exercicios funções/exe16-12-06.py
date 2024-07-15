def meddia_inteiros(**kwargs):
    nome1 = int(input("digite um numero: "))
    nome2 = int(input("digite um numero: "))
    nome3 = int(input("digite um numero: "))
    res = (nome1 + nome2 + nome3) / 3
    print(res)
    return sum(kwargs)
meddia_inteiros()