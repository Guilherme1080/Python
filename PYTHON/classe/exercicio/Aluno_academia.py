class Aluno_academia():
    def __init__(self,nome,idade,peso,altura,mensalidade = 120):
        self.nome = nome
        self.idade =idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def promocao(self):
        i = int(input("Quantos anos vc tem: "))
        self.idade = i
        if i < 18:
            print("vc possui um desconto!")
        else:
            print("vc nao possui desconto")
    def calcular(self):
        p = float(input("Qual é o seu peso: "))
        a = float(input("Qual é o sua altura (cm): "))
        self.peso = p
        self.altura = a
        imc = (self.altura * self.altura) /self.peso
        print(f"seu imc é {imc}")

aluno = Aluno_academia("Guilherme",18,60,190)
aluno.promocao()
aluno.calcular()