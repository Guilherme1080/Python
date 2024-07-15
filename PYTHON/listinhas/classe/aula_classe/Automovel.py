class Automovel:
    def __init__(self,marca,modelo,cor="Branco",ano="2024",placa="ABC-1234"):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.ano =ano
    def ligar(self):
        print(f"{self.marca} ligada")
    
    def getDados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"ano: {self.ano}")
        print(f"Placa: {self.placa}")

carro1 = Automovel("BMW","328i","Azul","1999","ROI-6151")
carro1.getDados()
carro1.ligar()