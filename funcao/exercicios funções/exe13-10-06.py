def lista(tamanho , valor_padrao):
    return[valor_padrao] * tamanho
tamanho = int(input("qual o tamanho da lista que deseja: "))
valor_padrao = input("digite o valor padrão: ")
x = lista(tamanho , valor_padrao)
print(x)
lista(tamanho, valor_padrao)