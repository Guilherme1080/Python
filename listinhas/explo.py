import sys
nome = str(input("digite o seu nome completo: "))
cargo = str(input("digite o seu cargo: "))
email = str(input("digite seu email: "))
idade = int(input("digite a sua idade: "))
if(idade < 18):
    print("vc nao esta aprovado")
    print(f"iremos mandar uma mensagem para esse email > {email}")
    print("obrigado pela a participação")
    sys.exit()
else:
    print("vc passou da primeira fase")
    print("2º fase")
curso = str(input("digite se vc tem algum curso de qualificação: "))
if(curso := "sim"):
    curso1 = str(input("qual? :"))
    print("vc está aprovado")
    print("vc passou para a proxima fase")
else:
    print("vc nao passou para a proxima fase")
    print(f"iremos mandar uma mensagem para esse email > {email}")
    print("obrigado pela a participação")
    sys.exit()
print("3º fase")
nota = float(input("qual foi sua nota na prova: "))
if(nota >= 7.0 ):
    print("parabens, vc esta aprovado para a final")
else:
    print("sua nota não foi aprovado")
    print(f"iremos mandar uma mensagem para esse email > {email}")
    print("obrigado pela a participação")