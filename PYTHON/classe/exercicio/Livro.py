class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def seteditora(self,novaeditora):
        self.editora = novaeditora
        print(f"a editora é nova {novaeditora}")

        

        

escritorio = Livro("Guilherme","igor","galera record",60)
print(f"essa é a editora {escritorio.editora}")
print("********"*20)
escritorio.seteditora("leitura")
print(escritorio.paginas)





    


    
