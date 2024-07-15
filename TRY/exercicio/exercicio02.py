# ​Escreva um programa Python que solicite ao usuário que insira dois números e gere uma exceção TypeError se as entradas não forem numéricas.
i = 0
while i < 4:
    try:
        x = float(input("Digite um numero: "))
    except:
        print("valor invalido!!! tente novamente")
    i = i + 1
