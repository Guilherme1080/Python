def eh_bissexto(ano):
    if(ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False
ano = int(input("digite o ano: "))
if eh_bissexto(ano):
    print(ano," é um bissexto")
else: 
    print(ano," não é um bissexto")