import sqlite3
from tkinter import *
class Professor(object):
    def __init__(self,nome= '',cpf_professor = '',departamento= ''):
        self.nome = nome
        self.cpf_professor = cpf_professor
        self.departamento = departamento

    def add_novo_professor(self):
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute('''insert into Professores
                            (nome,cpf,departamento) values(?,?,?)''',(self.nome,
                                                                      self.cpf_professor,
                                                                      self.departamento))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def read_professor(self):
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select * from Professores order by nome")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dados

    def update_professor(self,id_):
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        if self.nome != '':
            self.cursor.execute("""update Professores set nome = ? where id = ?""",(self.nome,id_))
        if self.cpf_professor != '':
            self.cursor.execute("""update Professores set cpf = ? where id = ?""",(self.cpf_professor,id_))
        if self.departamento != '':
            self.cursor.execute("""update Professores set departamento = ? where id = ?""",(self.departamento,id_))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def delete_professor(self,id_):
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("""delete from Professores where id = ?""",(id_,))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def pesquisa_professor(self,dado):
        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf from Professores")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        dado = (dado,)
        if dado in dados :
            return True
        else:
            return False
