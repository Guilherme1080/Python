amigos = {
    'luiz': '1',
    'fernando': '2',
    'joaquim' : '3',
}
for item in amigos:
    print(item)
adc = str(input("deseja adicionar mais algum amigo ?: "))
if adc == "sim":
    adc2 = str(input("coloca o nonme dele aqui: "))
    amigos [adc2] = "4"
    print(amigos)
else: 
    for item in amigos:
        print(item)
    