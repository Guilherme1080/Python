class Triangulo:
    def __init__(self,LadoA,LadoB,LadoC):
        self.ladoa = LadoA
        self.ladob = LadoB
        self.ladoc = LadoC

    def calcular_Perimetro(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        return perimetro
    
    def get_MaiorLado(self):
       return max(self.ladoa, self.ladob,self.ladoc)
    
    def calcular_Area(self): # fórmula que calcula area dos triangulos pelos lados 
        p = self.ladoa + self.ladob + self.ladoc
        area = (p * (p - self.ladoa) * (p - self.ladob) * (p - self.ladoc)) ** 0.5
        return area

        

ladoA = int(input("Valor do lado a:"))
ladoB = int(input("Valor do lado b:"))
ladoC = int(input("Valor do lado c:"))

triangulo1 = Triangulo(ladoA,ladoB,ladoC)

print(f'perímetro {triangulo1.calcular_Perimetro()}')
print(f'maior lado {triangulo1.get_MaiorLado()}')
print(f'area {triangulo1.calcular_Area()}')

