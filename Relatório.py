import sqlite3
from tkinter import *

#Aqui poderia utilizar apenas função, mas utilizei como uma classe para ficar organizado
class Relatório(object):
    def __init__(self):
        pass
    #Este método tem um parâmetro de cpf do professor a qual é necessário da para filtrar os dados que serão selecionados
    #Assim pegando todos os dados, abri-se um de disciplina para transformar-lo em um dicionário,pois o código da disciplina estará repsesentado em número e
    #eu quis apresenta-los como nomes em vez de número.
    #Final há apenas criação de uma relação como um dicionário, com a chave com valor da junção do codigo da turma e o periodo e o valor da chave como codigo
    #da turma que estará já como nome.
    def Todas_turmas_prof(self,cpfp):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigot,periodo,codigod from Turmas where cpfp = ? order by periodo",(cpfp,))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo,nome from Disciplina")
        dadosd = self.cursor.fetchall()
        dadosd = dict(dadosd)
        self.cursor.close()
        self.conexão.close()

        controlador = {}
        dadose = [[dadost[t][0],dadost[t][1],dadosd[dadost[t][2]]] for t in range(len(dadost))]

        for a in dadose:
            k = '/'.join([a[0],a[1]])
            if k not in controlador:
                controlador[k] = [a[2]]
            elif a[2] not in controlador[k]:
                controlador[k].append(a[2])
        return controlador
    #Esse método é para mostrar todos períodos do professor selecionado para que usuário escolha
    def Periodo_prof(self,cpf):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select periodo from Turmas where cpfp = ? order by periodo",(cpf,))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dadost
    #Esse método ele pega informação do cpf do professor e o periodo e filtra, a lógica é semelhante com de todos os periodos explicado acima
    def Lista_periodo_prof(self,cpf,periodo):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigot,codigod from Turmas where cpfp = ? and periodo = ? order by codigot",(cpf,periodo))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo,nome from Disciplina")
        dadosd = self.cursor.fetchall()
        dadosd = dict(dadosd)
        self.cursor.close()
        self.conexão.close()
        controlador = {}

        for a in dadost:
            if a[0] not in controlador:
                controlador[a[0]] = [dadosd[a[1]]]
            elif dadosd[a[1]] not in controlador[a[0]]:
                controlador[a[0]].append(dadosd[a[1]])

        return controlador
    #Metodo para todas turmas e periodos do aluno.
    def Todas_turmas_aluno(self,cpf):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigot,periodo,codigod from Turmas where cpfa = ? order by periodo",(cpf,))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo,nome from Disciplina")
        dadosd = self.cursor.fetchall()
        dadosd = dict(dadosd)
        self.cursor.close()
        self.conexão.close()

        controlador = {}
        
        dadose = [[dadost[t][0],dadost[t][1],dadosd[dadost[t][2]]] for t in range(len(dadost))]
        for a in dadose:
            k = '/'.join([a[0],a[1]])
            if k not in controlador:
                controlador[k] = [a[2]]
            elif a[2] not in controlador[k]:
                controlador[k].append(a[2])
            
        return controlador
    #Mostrar todos períodos do aluno, para o usuário selecionar
    def Periodo_aluno(self,cpf):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select periodo from Turmas where cpfa = ? order by periodo",(cpf,))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()
        return dadost
    #Mostrar todas turmas do periodo do aluno
    def Lista_periodo_aluno(self,cpf,periodo):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigot,codigod from Turmas where cpfa = ? and periodo = ? order by codigot",(cpf,periodo))
        dadost = self.cursor.fetchall()
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo,nome from Disciplina")
        dadosd = self.cursor.fetchall()
        dadosd = dict(dadosd)
        self.cursor.close()
        self.conexão.close()
        controlador = {}

        for a in dadost:
            if a[0] not in controlador:
                controlador[a[0]] = [dadosd[a[1]]]
            elif dadosd[a[1]] not in controlador[a[0]]:
                controlador[a[0]].append(dadosd[a[1]])
        return controlador
    #Aparti daqui começa a geração da ata de exercício:
    #Aqui vai mostrar todas turmas para que o usuário escolha a turma
    def todas_turmas(self):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigot from Turmas order by codigot")
        Turmas = list(set(self.cursor.fetchall()))
        self.cursor.close()
        self.conexão.close()

        return Turmas
    #Com a turma escolhida,será filtrado para mostrar todos periodos da turma
    def todos_periodos(self,turma):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select periodo from Turmas where codigot = ? order by periodo",(turma,))
        periodos = list(set(self.cursor.fetchall()))
        periodos = sorted(periodos)
        self.cursor.close()
        self.conexão.close()

        return periodos
    #Com os duas variaveis acima filtra para todos professores que tem os dados compatíveis com selecionados
    def todos_professores(self,periodo,turma):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpfp from Turmas where periodo = ? and codigot = ?",(periodo,turma,))
        professores = list(set(self.cursor.fetchall()))
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Professores.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf,nome from Professores")
        nomes = dict(self.cursor.fetchall())
        self.cursor.close()
        self.conexão.close()
        lista = [[nomes[a[0]],a[0]] for a in professores]
        lista = sorted(lista)

        return lista
    #E o ultimo filtro será de disciplina, que pegará todos os dados e fará novo filtro
    def todos_disciplina(self,periodo,professor_cpf,turma):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigod from Turmas where periodo = ? and cpfp = ? and codigot = ? order by codigod",(periodo,professor_cpf,turma,))
        disciplina = list(set(self.cursor.fetchall()))
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Disciplina.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select codigo,nome from Disciplina")
        nomes = dict(self.cursor.fetchall())
        self.cursor.close()
        self.conexão.close()
        lista = [[nomes[a[0]],a[0]] for a in disciplina]
        lista = sorted(lista)
        
        return lista
    #Com todos os dados, teremos dados suficiente para fazer a turma,assim o método abaixo ele pega todos os alunos com os dados adquiridos.
    def lista_alunos(self,periodo,turma,cpfp,disciplina):
        self.conexão = sqlite3.connect("data/Turmas.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpfa from Turmas where codigot = ? and periodo = ? and cpfp = ? and codigod = ?",(turma,periodo,cpfp,disciplina))
        Alunos = list(set(self.cursor.fetchall()))
        self.cursor.close()
        self.conexão.close()

        self.conexão = sqlite3.connect("data/Alunos.db")
        self.cursor = self.conexão.cursor()
        self.cursor.execute("select cpf,nome from Alunos")
        nomes = dict(self.cursor.fetchall())
        self.cursor.close()
        self.conexão.close()

        lista = [[nomes[a[0]],a[0]] for a in Alunos]
        lista = sorted(lista)

        return lista
    #A interface gráfica da ata ficou para pasta propriamente dita.
