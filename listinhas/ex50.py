entrada1 = int(input("Digite a coordenada x do primeiro ponto: "))
entrada2 = int(input("Digite a coordenada y do primeiro ponto: "))
entrada3 = int(input("Digite a coordenada x do segundo ponto: "))
entrada4 = int(input("Digite a coordenada y do segundo ponto: "))
dist = ((entrada1 - entrada3) ** 2 + (entrada2 - entrada4) ** 2) ** (1/2)
print(f"a Distância entre os pontos é de {dist:.2f}")

if dist >= 10:
    print(f"longe {dist:.2f}")
else:
    print(f"perto {dist:.2f}")