class Pessoa:
    def __init__(self,nome, idade,endereco):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade

    def getNome(self):
        return self.nome
    
    def setIdade(self,novaIdade):
        self.idade = novaIdade
    
pessoa1 = Pessoa("Guilherme",15,"Marcelo Roberto")
print(pessoa1.getNome())
print(pessoa1.idade)
print("*****"*20)
pessoa1.setIdade(17)
print(pessoa1.idade)
print(pessoa1.endereco)



