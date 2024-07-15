print("bem vindo a calculadora: ")
print("----" * 30)
soma = str(input("oque vc deseja calcular (+,-,/,*,): "))
if(soma == "+"):
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo  numero: "))
    calculo = n1 + n2
    print(f"o resultado é {calculo}")
elif(soma == "-"):
    n3 = float(input("digite o primeiro numero: "))
    n4 = float(input("digite o segundo  numero: "))
    calculo = n3 - n4
    print(f"o resultado é {calculo}")
elif(soma == "*"):
    n3 = float(input("digite o primeiro numero: "))
    n4 = float(input("digite o segundo  numero: "))
    calculo = n3 * n4
    print(f"o resultado é {calculo}")
elif(soma == "/"):
    n3 = float(input("digite o primeiro numero: "))
    n4 = float(input("digite o segundo  numero: "))
    calculo = n3 / n4
    print(f"o resultado é {calculo}")
else:
    print("numero não é dividido")