horas = float(input("digite as horas trabalhadas: "))
valor = float(input("digite o valor da hora do trabalho: "))
salario = horas * valor
aumento = 10 
novo_salario = (salario * aumento) /100
adic = salario + novo_salario
print(adic)
