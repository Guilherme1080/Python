class Funcionario:
    def __init__(self,nome,sobrenome,hora_trabalhada,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.hora_trabalhada = hora_trabalhada
        self.valor_hora = valor_hora

    def nomecompleto(self):
        print(f"{self.nome} {self.sobrenome}")
    def calcularsalario(self):
        z = self.hora_trabalhada * self.valor_hora
        self.hora_trabalhada = z
        print(f"seu salario é de: {z}")
    def incrementarHoras(self):
        extra = float(input("Quantas horas extra vc fez esse mês: "))
        c = self.valor_hora * extra
        f = self.hora_trabalhada + c
        print(f"seu salario, mais a hora extra é de: {f}")
        

clt = Funcionario("Guilherme","Miranda",120,50)
clt.nomecompleto()
clt.calcularsalario()
clt.incrementarHoras()
