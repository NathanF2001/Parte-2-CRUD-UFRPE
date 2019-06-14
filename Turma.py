import sqlite3
from tkinter import *
from Disciplina import *
from Aluno import *
from Professor import *

class Turma(object):
    def __init__(self,codigo_turma='', periodo = '', codigo_disciplina = '',
                 cpf_professor = '', cpf_aluno = ''):
        self.codigo_turma = codigo_turma
        self.periodo = periodo
        self.codigo_disciplina = codigo_disciplina
        self.cpf_professor = cpf_professor
        self.cpf_aluno = cpf_aluno

    def add_nova_turma(self):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute('''insert into Turmas
                        (codigot,periodo,codigod,cpfp,cpfa) values(?,?,?,?,?)''',(self.codigo_turma,self.periodo,
                                                                                  self.codigo_disciplina,self.cpf_professor,
                                                                                  self.cpf_aluno))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def read_turma(self):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select * from Turmas order by codigot")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dados
            

    def update_turma(self,id_):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        if self.codigo_turma != '':
            self.cursor.execute("""update Turmas set codigot = ? where id = ?""",(self.codigo_turma,id_))
        if self.periodo != '':
            self.cursor.execute("""update Turmas set periodo = ? where id = ?""",(self.periodo,id_))
        if self.codigo_disciplina != '':
            self.cursor.execute("""update Turmas set codigod = ? where id = ?""",(self.codigo_disciplina,id_))
        if self.cpf_professor != '':
            self.cursor.execute("""update Turmas set cpfp = ? where id = ?""",(self.cpf_professor,id_))
        if self.cpf_aluno != '':
            self.cursor.execute("""update Turmas set cpfa = ? where id = ?""",(self.cpf_aluno,id_))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def delete_turma(self,id_):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("""delete from Turmas where id = ?""",(id_,))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()
    #pesquisar de turma furnciona para retorna uma lista de 3 valores booleanos, que eles são utilizado caso o dado não esteja no sistema.
    #Caso exista em todas as exceções, os dados serão colocado em turmas sem precisar novos dados em outra área.
    def pesquisa_turmas(self,p,a,d):
        options = []
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf from Professores")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        p = (p,)
        a = (a,)
        d = (d,)
        if p in dados :
            options.append(False)
        else:
            options.append(True)
        
        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf from Alunos")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        if a in dados :
            options.append(False)
        else:
            options.append(True)

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo from Disciplina")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        if d in dados :
            options.append(False)
        else:
            options.append(True)

        return options




        

