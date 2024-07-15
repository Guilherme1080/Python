def Horas(horas,minutos,segundos):
    horas = horas * 3600
    minutos = minutos* 60
    segundos = segundos * 1
    res = horas + minutos + segundos
    print(res)

h = int(input("digite horas: "))
m = int(input("digite minutos: "))
s = int(input("digite segundos: "))

Horas(h,m,s)
