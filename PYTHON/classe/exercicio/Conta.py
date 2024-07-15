class Banco():
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def deposito(self):
        print(f"o seu saldo atual é {self.saldo}")
        a = float(input("digite o valor que deseja depositar: "))
        z = self.saldo + a
        self.saldo = z
    def saque(self):
        print(f"seu Novo saldo é de {self.saldo}")
        s = float(input("Qual é o valor que deseja sacar: "))
        if s > self.saldo:
            print("vc nao tem saldo suficiente")
        else:
            print("valor retirado")
            x = self.saldo - s
            print("seu saldo atual é de",x)





usuario = Banco("Guilherme",123456789,202020,20.00)
usuario.deposito()
usuario.saque()