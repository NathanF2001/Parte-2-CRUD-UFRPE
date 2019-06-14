import sqlite3
from tkinter import *
class Disciplina(object):
    def __init__(self,nome= '',codigo = ''):
        self.nome = nome
        self.codigo = codigo

    def add_nova_disciplina(self):
        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute('''insert into Disciplina
                            (nome,codigo) values(?,?)''',(self.nome,self.codigo))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def read_disciplina(self):
        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select * from Disciplina order by nome")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dados

    def update_disciplina(self,id_):
        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        if self.nome != '':
            self.cursor.execute("""update Disciplina set nome = ? where id = ?""",(self.nome,id_))
        if self.codigo != '':
            self.cursor.execute("""update Disciplina set codigo = ? where id = ?""",(self.codigo,id_))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def delete_disciplina(self,id_):
        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("""delete from Disciplina where id = ?""",(id_,))
        self.conexão.commit()
        self.cursor.close()
        self.conexão.close()

    def pesquisa_disciplina(self,dado):
        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo from Disciplina")
        dados = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        dado = (dado,)
        if dado in dados :
            return True
        else:
            return False
        
