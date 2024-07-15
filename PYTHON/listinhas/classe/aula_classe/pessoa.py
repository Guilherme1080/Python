class Pessoa:
    def __init__(self,id = 0, nome=""):
        self.id = id
        self.nome = nome
    
    def Hello(self):
        print(f"Olá {self.nome}")

pes1 = Pessoa()
print(pes1.id)
print("Bom dia")
name = input("digite seu nome: ")
pes1.nome = name
pes1.Hello()