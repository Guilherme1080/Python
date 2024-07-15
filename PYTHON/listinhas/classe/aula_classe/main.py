from Estudante import Estudante

matricula = input("Matricula: ")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nota = input("Digite sua nota: ")

aluno1 = Estudante(matricula,nome,idade,nota)
aluno1.mostrarDados()