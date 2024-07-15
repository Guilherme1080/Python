# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. 
# As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("digite a sua idade: "))
trabalhado = str(input("a quanto tempo você trabalha: "))
if(idade >= 65):
    print("vc pode se aposentar")
elif(trabalhado >= "30 anos"):
    print("vc pode se aposentar")
elif(idade >= 60 and trabalhado >= "25 anos"):
    print("vc pode se aposentar")
else:
    print("vc nao pode se aposentar")
