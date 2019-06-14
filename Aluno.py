import sqlite3
from tkinter import *
#------Criação da classe Aluno------
class Aluno(object):
    #Método construtor com os parâmetros nome e cpf_aluno e colocaram eles como objeto.
    def __init__(self, nome= '',cpf_aluno = ''):
        self.nome = nome
        self.cpf_aluno = cpf_aluno
    #Método de adicionar aluno, abri-se o banco de dados e inseri o nove e o cpf
    def add_novo_aluno(self):
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute('''insert into Alunos
                        (nome,cpf) values(?,?)''',(self.nome,self.cpf_aluno))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()
    #Método de ler para colocar em uma lista, nessa etapa utiliza o selecionar todos os dados de Alunos ordenados pela coluna nome
    def read_aluno(self):
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select * from Alunos order by nome")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dados
    #Método para atualizar,coloquei exceção para se as instancias forem diferente de vazia,pois no meu programa se o usuário não deseja atualizar ele não
    #digita nada. Então utiliza o comando de atualizar a coluna, na linha onde tiver o id que foi gerado quando é inserido cada dado.
    def update_aluno(self,id_):
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        if self.nome != '':
            self.cursor.execute("""update Alunos set nome = ? where id = ?""",(self.nome,id_))
        if self.cpf_aluno != '':
            self.cursor.execute("""update Alunos set cpf = ? where id = ?""",(self.cpf_aluno,id_))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()
    #Método para deletar,utiliza o comando de deletar do Banco de dados de Alunos na linha onde tem o id que foi gerada no adicionar.
    def delete_aluno(self,id_):
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("""delete from Alunos where id = ?""",(id_,))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()
    #Método de pesquisar para que não haja cpf de alunos iguais
    def pesquisa_aluno(self,dado):
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf from Alunos")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        dado = (dado,)
        if dado in dados :
            return True
        else:
            return False
#Nos outros tipo é mesmo modelo de lógica,portanto não irei repeti-los(a única exceção e de turmas em pesquisar.
        
