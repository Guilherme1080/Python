class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 =nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def nota(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) /4
        if media >= 7:
            print("vc esta aprovado ")
        if media >= 5 and media <= 6.9:
            print("vc esta de exame")
        if media < 5:
            print("vc esta reprovado")

        return media
    
estudante = Aluno("Guilherme","202020",10,10,10,10)
print(estudante.nota())