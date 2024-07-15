class Carro():
    def __init__(self,modelo,marca,cor,ano,valor,nivel:0,consumo):
        self.modelo =modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def abastecer(self):
        a = float(input("digite quantos litros deseja abastecer o seu carro: "))
        z = a * 100
        self.nivel = z

        print(self.nivel)

    def andar(self):
        a = float(input("qual é a distancia que o carro percorreu: "))
        self.consumo = a
        print(f"o carro percorreu {a} km")
    
    def verificar_nivel(self):
        z = self.consumo / self.nivel
        print(f"para cada km foi gastou {z} de combustivel")

    def calcular_imposto(self):
        calculo = (self.valor * 2.5) /100
        print(calculo)
    
c = Carro("porsche 911", "porcshe","marrom","2024",1920000,0,0)
c.abastecer()
c.andar()
c.verificar_nivel()
c.calcular_imposto()
