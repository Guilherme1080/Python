#Seu João precisa fazer um empréstimo automático no aplicativo, o banco aprova a transação de 
# acordo com as seguintes condições: Leia o salário de um trabalhador e o valor da prestação de 
# um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não 
# concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input("digite o seu salario: "))
imprestimo = float(input("quantos deseja pegar de imprestimo: "))
prestacao = (imprestimo * 20) /100