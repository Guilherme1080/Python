class Agenda():
    def __init__(self,dia,mes,ano,anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    
    def validar(self):
        x = input("qual é o dia que deseja fazer a anotacao: ")
        self.dia = x 
        c = input("qual é o mês que deseja fazer a anotacao: ")
        self.mes = c
        v = input("qual é o ano que deseja fazer a anotacao: ")
        self.ano = v
        return self
    def tarefa(self):
        tarefa = str(input("qual é a anotacao para esse dia: "))
        self.anotacao = tarefa
        print(f"anotado para {self.dia}/{self.mes}/{self.ano}  mandar :{self.anotacao}:")

a = Agenda("10",'10',"2000","oosdnonsdv")
a.validar()
a.tarefa()
