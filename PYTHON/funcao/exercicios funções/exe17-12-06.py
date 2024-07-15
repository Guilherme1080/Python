def armazenar_dados(**kwargs):
    dados_pessoa = {}
    for chave, valor in kwargs.items():
        dados_pessoa[chave] = valor
    
    
    for chave, valor in dados_pessoa.items():
        print(f"{chave}: {valor}")
        return 
nome = str(input("digite seu nome: "))
idade = int(input("digite sua idade: "))
cidade = str(input("digite sua cidade: "))
profissao = str(input("digite sua profissão: "))

armazenar_dados(nome=nome, idade=idade, cidade=cidade, profissão=profissao)