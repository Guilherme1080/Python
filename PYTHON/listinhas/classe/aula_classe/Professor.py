class Professor:
    def __init__(self,Nome,sala,turno,idade):
        self.nome = Nome
        self.sala = sala
        self.idade = idade
        self.turno = turno

    def hello(self):
        print(f"Olá {self.nome}")

    
    def mostrarDados(self):
        print(f"Nome: {self.nome}")
        print(f"sala: {self.sala}")
        print(f"idade: {self.idade}")
        print(f"turno: {self.turno}")
        

prof = Professor("Thiago",204,"Matutino",25)
prof.hello()
prof.mostrarDados()