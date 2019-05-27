import sqlite3
from tkinter import *
class Aluno(object):
    #Metodo construtor básico para guardar o nome e cpf (os dados desse setor do CRUD)
    def __init__(self, nome= '',cpf_aluno = ''):
        self.nome = nome
        self.cpf_aluno = cpf_aluno
    # Isso é um método para que mude o objeto nome para um que foi estabelecido no parametro(não é obrigatório mais fica mais organizado)
    def set_nome(self,novo_nome):
        self.nome = novo_nome
    # Mesma coisa do que de cima
    def set_cpf(self,novo_cpf):
        self.cpf_aluno = novo_cpf
    #Método de adicionar aluno
    def add_novo_aluno(self):
        self.conexão = sqlite3.connect("dados/Alunos.db")   #Abrindo o banco de dados Alunos
        self.cursor = self.conexão.cursor()         #Cursor que vai executar a ação que eu mandar
        conf = self.confirmar(nome,cpf)     #executo o metodo confirmar guardando na variavel conf
        if conf:        #Se a variavel conf for True
            self.cursor.execute('''insert into Alunos
                            (nome,cpf) values(?,?)''',(self.nome,self.cpf_aluno))       #Ele vai inserir os dados no banco de dados, vale observar que não é necessário
                                                                                        # colocar o id, pois ele ja é inserido junto.
            self.conexão.commit()       #Salvar para não dar treta
        self.cursor.close()
        self.conexão.close()        #Fechar é bom para não abusar da memoria do seu pc, se você ja usa o Chrome não precisa abusar mais que isso.

    def read_aluno(self):
        self.conexão = sqlite3.connect("dados/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select * from Alunos order by nome")   #Aqui to selecionando todos os dados do banco de dados Alunos e pondo em ordem pela coluna "nome"
        dados = self.cursor.fetchall()  #adiciona todo os dados do cursor que foi selecionado em uma variavel que vira uma Lista
        print("{0:<5} {1:<15} {2:<60}".format("ID","CPF","NOME"))   #Para ficar bonitinho
        for posição,dado in enumerate(dados):   #Preciso da posição para saber qual dado que to mexendo e o dados em si vai ter a posição de 0 - o id / 1-o nome /2 - o cpf
            print("{0:<5} {1:<15} {2:<60}".format(dados[posição][0],dados[posição][2],dados[posição][1]))
        self.cursor.close()
        self.conexão.close()        #As maquinas agradecem
            

    def update_aluno(self,id_):
        self.conexão = sqlite3.connect("dados/Alunos.db")
        self.cursor = self.conexão.cursor()
        novo_nome = input("Insira novo Nome: (Digite nada se não quiser alterar)\n")    #auto explicativo, não?
        novo_cpf = input("Insira novo CPF: (Digite nada se não quiser alterar)\n")
        self.set_nome(novo_nome)        #isso e para mudar o objeto nome para o parametro desejado acima
        self.set_cpf(novo_cpf)          #isso e para mudar o objeto cpf para o parametro desejado acima
        if self.nome != '':
            self.cursor.execute("""update Alunos set nome = ? where id = ?""",(self.nome,id_))  #Aqui eu utilizo a id, eu acho o dado pela id, usando o where
        if self.cpf_aluno != '':
            self.cursor.execute("""update Alunos set cpf = ? where id = ?""",(self.cpf_aluno,id_))#Aqui eu utilizo a id, eu acho o dado pela id, usando o where
        self.conexão.commit()
        print("Dados atualizados")
        self.cursor.close()
        self.conexão.close()    #...

    def delete_aluno(self,id_):
        self.conexão = sqlite3.connect("dados/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select nome,cpf from Alunos where id = ?",(id_,))#Aqui é para mostrar o dado que vc quer deletar para ver se vc tem certeza
        nome,cpf = self.cursor.fetchone()
        e = self.confirmar(nome,cpf)
        if e:
            self.cursor.execute("""delete from Alunos where id = ?""",(id_,))   #Deleta o dado
            self.conexão.commit()
            print("Dado deletado")
        self.cursor.close()
        self.conexão.close() #


    def confirmar(self,nome,cpf):
        #Essa definição é so para confirmar se que executar
        a = input("Tem certeza que deseja executar essa ação nos seguintes dados:\n Nome: %s\n CPF: %s\n(Responda com 'SIM' OU 'NAO')"%(nome,cpf))
        if a == "SIM":
            print("Dados adicionados ao sistema")
            return True
        elif a == "NAO":
            print("Voltando ao menu")
            return False
        else:
            print("\nDeixe de ser palhaço é 'SIM' ou 'NAO'.\n")
            return self.confirmar(nome,cpf) 

    
def inserir_dados():
    #Vou nem comentar
    nome = input("Escolha um nome para adicionar ao sistema.")
    cpf = input("Escolha um CPF para adicionar ao sistema.")
    return nome,cpf

while True:
    #Menuzinho basico para aluno
    escolha =   int(input("""Selecione o que queres fazer:)
    1 - Novo dado
    2 - Atualizar dado
    3 - Consultar dados
    4 - Deletar dado
    """
    ))
    if escolha == 1:
        #Pegar os dados que queira colocar
        nome,cpf = inserir_dados()
        dados = Aluno(nome,cpf) #Abri  a classe
        dados.add_novo_aluno()  #Executa o add aluno
    elif escolha == 2:
        dados = Aluno() #Abri a classe
        dados.read_aluno()  #Executa read para mostrar todos os dados
        escolha = int(input("Escolha a id do dado que queira alterar")) #Pede id
        dados.update_aluno(escolha) #Da update de acordo com paramemtro escolha que é o id
    elif escolha == 3:
        dados = Aluno() #abri a classe
        dados.read_aluno()  #Mostrar todos os dados
    elif escolha == 4:
        #Mesma coisa de alterar so que tira
        dados = Aluno()
        dados.read_aluno()
        escolha = int(input("Escolha a id do dado que queira alterar"))
        dados.delete_aluno(escolha)




        

