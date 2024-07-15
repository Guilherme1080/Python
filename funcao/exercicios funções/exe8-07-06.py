def pesca():
    kg = float(input("quantos kgs de peixe foi pescado: "))
    if kg > 50:
        print("vc escedeu o limite")
        x = kg - 50
        print(f"o valor ultrapassado foi: {x} kilos")
        x = x * 4
        print(f"o valor de multa a ser pago é: {x}")
    else:
        print("nao ha taxa")
pesca()