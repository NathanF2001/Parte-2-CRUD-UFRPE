from tkinter import *
from tkinter import ttk
from Aluno import *
from Professor import *
from Disciplina import *
from Turma import *
from Relatório import *
from Ata_de_exercicio import *
from functools import partial

class Interface(object):
    #Método construtor tem o que tem na primeira janela quando abre o programa
    def __init__(self, instancia = None):
        #self.add fica True quando utiliza o botão de adicionar, assim terá uma condição para retirar labels específica desse área
        #self.con ja funciona para o resto: alterar,consultar,alterar
        self.add = False
        self.con = False
        self.p = 0

        self.main_frame = Frame(instancia, bg= "#1a2e4f")
        self.main_frame.grid(row=0,column = 0,sticky = W+E+N+S)
        #Frame para ter mensagem de boas vindas ,direitos autorais e o simbolo da UFRPE essas que são informações mais estáticas
        self.second_frame = Frame(instancia, bg ="#46679f")
        self.second_frame.grid(row = 0,column = 0,sticky = W+E+N+S,ipadx = 13)
        #Frame para as informações dinâmicas
        self.third_frame = Frame(instancia, bg = "#1a2e4f")
        self.third_frame.grid(row = 1,column = 0,sticky = W+E+N+S)
        #Criação da Label da imagem UFRPE
        ufrpe_logo = PhotoImage(file = "ufrpe_logo.gif")
        self.ufrpe_logo = Label(self.second_frame,image = ufrpe_logo,bg = "#46679f")
        self.ufrpe_logo.image = ufrpe_logo 
        #Label de boas vindas
        self.boas_vindas = Label(self.second_frame,width = 22,text = "Bem vindo ao CRUD UFRPE",font = ("Century","20","bold"),fg= "white",bg = "#46679f")
        #Label de copyright
        self.copyright = Label(self.second_frame,text = "© Todos direitos reservados a Nathan Freitas",font = ("Century","7","bold"),bg = "#46679f")
        #Colocá-las na janela:
        self.ufrpe_logo.grid(row = 0,column = 0,rowspan = 4,sticky = W)
        self.boas_vindas.grid(row = 0,rowspan = 4,column = 1,columnspan =6 ,sticky = W)
        self.copyright.grid(row = 3,column= 2, columnspan = 5,sticky = E)  
        #Label escolha que tem a mensagem sobre uma orientação sobre o que fazer
        self.escolha = Label(self.third_frame,text = "Escolha em qual área desejas entrar :",font = ("Century","18","bold"),bg = "#b1ceff")
        self.escolha.grid(row = 0,column = 0,columnspan = 11,sticky = N+S+W+E)
        #Os justifcadores servem para ajustar o tamanho do botões
        self.justificador1 = Label(self.third_frame)
        self.justificador2 = Label(self.third_frame)
        self.justificador1['bg'] = self.justificador2['bg'] = "#1a2e4f"

        self.justificador1.grid(row = 3,column = 0,columnspan = 2,ipadx = 125)
        self.justificador2.grid(row = 3,column = 2,columnspan = 2,ipadx = 125)
        #Cada um dos botões são respectivamente: Professor,Aluno,Disciplina,Turma
        self.NO = Button(self.third_frame,height = 3,font = ("Century","31","bold"),bd = 5,fg = "#e39a07",activeforeground = "#e39a07",
                         bg = "#1a2e4f",activebackground = "#1a2e4f",text = 'Professor',command = lambda : self.menu_area('P'))
        self.NO.grid(row = 1,column = 0, columnspan = 2,sticky = W+E+N+S)

        self.NE = Button(self.third_frame,font = ("Century","31","bold"),bd = 5,fg = "#e39a07",activeforeground = "#e39a07",
                         bg = "#1a2e4f",activebackground = "#1a2e4f",text = 'Aluno',command = lambda : self.menu_area('A'))
        self.NE.grid(row=1,column=2,columnspan=2,sticky = W+E+N+S)

        self.SO = Button(self.third_frame,height = 3,font = ("Century","31","bold"),bd = 5,fg = "#e39a07",activeforeground = "#e39a07",
                         bg = "#1a2e4f",activebackground = "#1a2e4f",text = 'Disciplina',command = lambda : self.menu_area('D'))
        self.SO.grid(row=2,column=0,columnspan = 2,sticky = W+E+N+S)

        self.SE = Button(self.third_frame,font = ("Century","31","bold"),bd = 5,fg = "#e39a07",activeforeground = "#e39a07",
                         bg = "#1a2e4f",activebackground = "#1a2e4f",text = 'Turma',command = lambda : self.menu_area('T'))
        self.SE.grid(row=2,column=2,columnspan = 2,sticky = W+E+N+S)
        #Mensagem para dizer para gerar Relatório
        self.msg_inferior = Label(self.third_frame,text = "Gerar a Ata de exercício :",bg = "#424b5b",fg = "white",font = ("Century","9","bold"))
        self.msg_inferior.grid(row = 4,column = 0,columnspan = 2,sticky = W+E+N+S)
        #Botão para gerar relatório
        self.inferior = Button(self.third_frame,text = "Gerar",font = ("Century","10","bold"),fg = "#e39a07",activeforeground = "#e39a07",
                               bg = "#1a2e4f",activebackground = "#1a2e4f",command = self.Relatório_menu)
        self.inferior.grid(row = 4,column = 2,columnspan = 2,sticky = W+E+N+S)

    #Método para voltar as configurações iniciais
    def comandos_menu_principal(self):
        self.boas_vindas["text"] = "Bem vindo ao CRUD UFRPE"
        self.boas_vindas.grid(row = 0,rowspan = 4,column = 1,columnspan =5,sticky = W+E+N+S)
        self.msg_inferior.grid(row = 4,column = 0,columnspan = 2,sticky = W+E+N+S)
        self.inferior.grid(row = 4,column = 2,columnspan = 2,sticky = W+E+N+S)
        self.NO["text"] ="Professor"
        self.NE["text"] = "Aluno"
        self.SO["text"] = "Disciplina"
        self.SE["text"] = "Turma"
        self.NO["command"] = lambda : self.menu_area('P')
        self.NE["command"] = lambda : self.menu_area('A')
        self.SO["command"] = lambda : self.menu_area('D')
        self.SE["command"] = lambda : self.menu_area('T')
        self.msg_inferior["font"] = ("Century","9","bold")
        self.msg_inferior["text"] = "Gerar a Ata de exercício :"
        self.escolha["text"] = "Escolha em qual área desejas entrar :"
        self.voltar.grid_forget()
    #Método para esconder as labels que foram criada do inicio
    def esconder_widgets_principais(self):
        self.msg_inferior.grid_forget()
        self.inferior.grid_forget()
        self.NO.grid_forget()
        self.NE.grid_forget()
        self.SO.grid_forget()
        self.SE.grid_forget()
    #Método para voltar as labels do inicio
    def voltar_widget_principais(self):
        self.NO.grid(row = 1,column = 0, columnspan = 2,sticky = W+E+N+S)
        self.NE.grid(row=1,column=2,columnspan=2,sticky = W+E+N+S)
        self.SO.grid(row=2,column=0,columnspan = 2,sticky = W+E+N+S)
        self.SE.grid(row=2,column=2,columnspan = 2,sticky = W+E+N+S)

        self.msg_inferior["text"] = "Gerar a Ata de exercício :"
        self.msg_inferior.grid(row = 4,column = 0,columnspan = 2,sticky = W+E+N+S)

        self.inferior["text"] = "Gerar"
        self.inferior.grid(row = 4,column = 2,columnspan = 2,sticky = W+E+N+S)
    #Menu_area reutiliza os botões e coloca novas funções de Novo,Consulta,Atualizar e deletar
    def menu_area(self,tipo):
        self.escolha['fg'] = 'black'
        if tipo == 'A':
            self.boas_vindas["text"] = "Área : ALUNO"       
            self.msg_inferior["text"] = "Gerar Relatório de Alunos :"
            if self.add:
                self.add = False
                self.destruir_add_aluno()
                self.voltar_widget_principais()
            if self.con :
                self.con = False
                self.p = 0
                self.rollback_consulta_aluno()
                self.voltar.destroy()
                self.voltar_widget_principais()
        elif tipo == 'P':
            self.boas_vindas["text"] = "Área : PROFESSOR"   
            self.msg_inferior["text"] = "Gerar Relatório de Professor :"
            if self.add:
                self.add = False
                self.destruir_add_professor()
                self.voltar.destroy()
                self.voltar_widget_principais()
            if self.con :
                self.con = False
                self.p = 0
                self.rollback_consulta_aluno()
                self.voltar.destroy()
                self.voltar_widget_principais()
        elif tipo == 'D':
            self.boas_vindas["text"] = "Área : DISCIPLINA"       #text = Bem vindo ao CRUD UFRPE
            self.msg_inferior["text"] = "Gerar Relatório de Disciplina :"
            if self.add:
                self.add = False
                self.destruir_add_disciplina()
                self.voltar_widget_principais()
            if self.con :
                self.con = False
                self.p = 0
                self.rollback_consulta_aluno()
                self.voltar.destroy()
                self.voltar_widget_principais()
        elif tipo == 'T':
            self.boas_vindas["text"] = "Área : TURMA"       #text = Bem vindo ao CRUD UFRPE
            self.msg_inferior["text"] = "Gerar Relatório de Turma :"
            if self.add:
                self.add = False
                self.destruir_add_turma()
                self.voltar_widget_principais()
            if self.con :
                self.con = False
                self.p = 0
                self.rollback_consulta_aluno()
                self.voltar_widget_principais()
        self.NO["text"] = "Novo"
        self.NO["command"] = lambda : self.interface_add(tipo)
        self.NE["text"] = "Consulta"
        self.NE["command"] = lambda : self.Interface_consultar(tipo,'C')
        self.SO["text"] = "Atualizar"
        self.SO["command"] = lambda : self.Interface_consultar(tipo,'A')
        self.SE["text"] = "Deletar"
        self.SE["command"] = lambda : self.Interface_consultar(tipo,'D')
        self.escolha["text"] = "Escolha qual ação desejas executar :"
        self.voltar = Button(self.third_frame,text = "Voltar",command = self.comandos_menu_principal,font = ("Century","10","bold"),fg = "#e39a07",
                             activeforeground = "#e39a07",bg = "#1a2e4f",activebackground = "#1a2e4f")
        self.voltar.grid(row = 4,column = 0,columnspan = 4,sticky = W+E+N+S)
    #Mini método so pra limitar os caracteres dos cpf
    def limitar_tamanho(self,a):
        if len(a) > 14:
            return False
        else:
            return True
    #Método der adicionar dados
    def interface_add(self,tipo):
        self.add = True
        self.esconder_widgets_principais()
        self.escolha["text"] = "Novos dados : "
        self.escolha["fg"] = "black"
        #Esse limitador é do cpf
        limitador = self.main_frame.register(self.limitar_tamanho)
        #As entradas de Turma
        if tipo == 'T':
            self.codigot_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Código da turma :")
            self.inserir_codigot = Entry(self.third_frame,font = ("Century","12","bold"))
            self.inserir_codigot["font"] = ("Century","12","bold")

            self.periodo_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Período :")
            self.inserir_periodo = Entry(self.third_frame,font = ("Century","12","bold"))

            self.codigo_disciplina_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Código da disciplina :")
            self.inserir_codigo_disciplina = Entry(self.third_frame,font = ("Century","12","bold"))

            self.cpf_professor_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "CPF do Professor :")
            self.inserir_cpf_professor = Entry(self.third_frame,validate='key', validatecommand=(limitador, '%P'),font = ("Century","12","bold"))

            self.cpf_aluno_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "CPF do Aluno :")
            self.inserir_cpf_aluno = Entry(self.third_frame,validate='key', validatecommand=(limitador, '%P'),font = ("Century","12","bold"))

            self.codigot_pede.grid(row = 1,column = 0,sticky = W)
            self.inserir_codigot.grid(row = 1,column = 1,columnspan = 3,sticky = W)
            self.periodo_pede.grid(row = 2,column = 0,sticky = W)
            self.inserir_periodo.grid(row = 2,column = 1,columnspan = 3,sticky = W)
            self.codigo_disciplina_pede.grid(row = 3,column = 0,sticky = W)
            self.inserir_codigo_disciplina.grid(row = 3,column = 1,columnspan = 3,sticky = W)
            self.cpf_professor_pede.grid(row = 4,column = 0,sticky = W)
            self.inserir_cpf_professor.grid(row = 4,column = 1,columnspan = 3,sticky = W)
            self.cpf_aluno_pede.grid(row = 5,column = 0,sticky = W)
            self.inserir_cpf_aluno.grid(row = 5,column = 1,columnspan = 3,sticky = W)
        #As entradas das demais  
        else:
            self.nome_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo nome :")
            self.inserir_nome = Entry(self.third_frame,font = ("Century","12","bold"))
            if tipo == 'D':
                self.codigo_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo codigo :")
                self.inserir_codigo = Entry(self.third_frame,font = ("Century","12","bold"))
                self.codigo_pede.grid(row = 2,column = 0,columnspan = 2,sticky = W)
                self.inserir_codigo.grid(row = 2,column = 1,columnspan = 2,sticky = W)

            if tipo == 'A' or tipo == 'P':
                self.cpf_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo CPF  :")
                self.inserir_cpf = Entry(self.third_frame,validate='key', validatecommand=(limitador, '%P'),font = ("Century","12","bold"))
                self.cpf_pede.grid(row=2,column=0,sticky = W)
                self.inserir_cpf.grid(row=2,column=1,columnspan = 2,sticky = W)

            if tipo == 'P':
                self.departamento_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo Departamento  :")
                self.inserir_departamento_professor = Entry(self.third_frame,font = ("Century","12","bold"))
                self.departamento_pede.grid(row = 3,column = 0,columnspan = 2,sticky = W)
                self.inserir_departamento_professor.grid(row = 3,column = 2,sticky = W)

            self.nome_pede.grid(row = 1,column = 0,sticky = W)
            if tipo == 'P':
                self.inserir_nome.grid(row = 1 , column =1,columnspan = 2,sticky = W)
            else:
                self.inserir_nome.grid(row = 1 , column =1,columnspan = 3,sticky = W)

        self.confirmar = Button(self.third_frame,font = ("Century","10","bold"),fg = "#e39a07",activeforeground = "#e39a07",bg = "#1a2e4f",activebackground = "#1a2e4f",
                                text = "Enviar",command = lambda : self.add_dados_banco_de_dados(tipo))

        self.voltar.grid(row = 6,column = 0,columnspan = 2,sticky = W+E+N+S)
        self.confirmar.grid(row = 6,column = 2,columnspan = 5,sticky = W+E+N+S)
        

        self.voltar["command"] = lambda : self.menu_area(tipo)
    #Método para apagar informações da entrada para adicionar novas entradas
    def voltar_add(self,tipo):
        if tipo == 'T':
            self.inserir_codigot.delete(0,'end')
            self.inserir_periodo.delete(0,'end')
            self.inserir_codigo_disciplina.delete(0,'end')
            self.inserir_cpf_professor.delete(0,'end')
            self.inserir_cpf_aluno.delete(0,'end')
        else:
            self.inserir_nome.delete(0,'end')
            if tipo == 'P' or tipo == 'A':
                self.inserir_cpf.delete(0,'end')
                if tipo == 'P':
                    self.inserir_departamento_professor.delete(0,'end')
            elif tipo == 'D':
                self.inserir_codigo.delete(0,'end')
        self.escolha["text"] = "Novos dados: "
        self.escolha["fg"] = "black"
        self.confirmar["text"] = "Enviar"
        self.confirmar["command"] = lambda : self.add_dados_banco_de_dados(tipo)
    #Método específico para adicionar turma,como ja dito na pasta Turma, ela funciona de forma diferente
    #E quando tem dados que não estão do sistema ele pede para que adiciona,portanto é chamado esse método para adicionar os dados que falta(m)
    def adicionar_dados_turma(self,valor):
        self.mensagem_aviso.destroy()
        if valor[0]:
            self.nome_pedep = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo nome de professor:")
            self.inserir_nomep = Entry(self.third_frame,font = ("Century","12","bold"))
            self.departamento_pede = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo Departamento  :")
            self.inserir_departamento_professor = Entry(self.third_frame,font = ("Century","12","bold"))
            self.nome_pedep.grid(row = 1,column =0,columnspan = 2,sticky = W)
            self.inserir_nomep.grid(row= 1,column = 2,columnspan = 2,sticky = W+E)
            self.departamento_pede.grid(row = 2,column =0,columnspan = 2,sticky = W)
            self.inserir_departamento_professor.grid(row= 2,column = 2,columnspan = 2,sticky = W+E)
        if valor[1]:
            self.nome_pedea = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo nome de aluno:")
            self.inserir_nomea = Entry(self.third_frame,font = ("Century","12","bold"))
            self.nome_pedea.grid(row =3,column =0,columnspan = 2,sticky = W)
            self.inserir_nomea.grid(row=3,column = 2,columnspan = 2,sticky = W+E)
        if valor[2]:
            self.nome_peded = Label(self.third_frame,font = ("Century","20","bold"),bg = "#1a2e4f",fg = "#e39a07",text = "Novo nome de Disciplina:")
            self.inserir_nomed = Entry(self.third_frame,font = ("Century","12","bold"))
            self.nome_peded.grid(row =4,column =0,columnspan = 2,sticky = W)
            self.inserir_nomed.grid(row=4,column = 2,columnspan = 2,sticky = W+E)
        self.voltar['text'] = 'Voltar'
        self.voltar['command'] = lambda : self.tirar_novos_dados(valor)
        self.confirmar["text"] = "Enviar"
        self.confirmar["command"] = lambda : self.adicionar_dados_novos(valor)
    #Adicionar os dados de turma
    def adicionar_dados_novos(self,valor):
        if valor[0]:
            dados = Professor(self.inserir_nomep.get(),self.dadost.cpf_professor,self.inserir_departamento_professor.get())
            dados.add_novo_professor()
        if valor[1]:
            dados = Aluno(self.inserir_nomea.get(),self.dadost.cpf_aluno)
            dados.add_novo_aluno()
        if valor[2]:
            dados = Disciplina(self.inserir_nomed.get(),self.dadost.codigo_disciplina)
            dados.add_nova_disciplina()
        self.dadost.add_nova_turma()
        self.escolha["text"] = "Dados foram adicionados ao sistema."
        self.escolha["fg"] = "green"
        self.confirmar['text'] = 'OK'
        self.confirmar['command'] = lambda : self.tirar_novos_dados(valor)
    #Destruir labels de adicionar turma
    def tirar_novos_dados(self,valor):
        if valor[2]:
            self.nome_peded.destroy()
            self.inserir_nomed.destroy()
        if valor[1]:
            self.nome_pedea.destroy()
            self.inserir_nomea.destroy()
        if valor[0]:
            self.nome_pedep.destroy()
            self.inserir_nomep.destroy()
            self.departamento_pede.destroy()
            self.inserir_departamento_professor.destroy()
        self.confirmar.grid_forget()
        self.interface_add("T")
    #Método par adicionar os dados no banco de dados
    def add_dados_banco_de_dados(self,tipo):
        cpfi = False
        valor = False

        self.confirmar["text"] = "Ok"
        self.confirmar["command"] = lambda : self.voltar_add(tipo)
        if tipo == 'A':
            #Condição para que o cpf esteja no padrão do sistema
            if len(self.inserir_cpf.get()) == 14:
                dados = Aluno(self.inserir_nome.get(),self.inserir_cpf.get())
                valor = dados.pesquisa_aluno(self.inserir_cpf.get())
            else:
                valor = True
                cpfi = True
        elif tipo == 'P':
            #Condição para que o cpf esteja no padrão do sistema
            if len(self.inserir_cpf.get()) == 14:
                dados = Professor(self.inserir_nome.get(),self.inserir_cpf.get(),self.inserir_departamento_professor.get())
                valor = dados.pesquisa_professor(self.inserir_cpf.get())
            else:
                valor = True
                cpfi = True
        elif tipo == 'D':
            dados = Disciplina(self.inserir_nome.get(),self.inserir_codigo.get())
            valor = dados.pesquisa_disciplina(self.inserir_codigo.get())
        elif tipo == 'T':
            #Condição para que o cpf esteja no padrão do sistema
            if len(self.inserir_cpf_professor.get())== 14 and len(self.inserir_cpf_aluno.get()) == 14:
                self.conf = False
                self.dadost = Turma(self.inserir_codigot.get(),self.inserir_periodo.get(),self.inserir_codigo_disciplina.get(),self.inserir_cpf_professor.get(),self.inserir_cpf_aluno.get())
                bol = self.dadost.pesquisa_turmas(self.inserir_cpf_professor.get(),self.inserir_cpf_aluno.get(),self.inserir_codigo_disciplina.get())
                self.destruir_add_turma()
                self.voltar.grid(row = 10,column = 0,columnspan = 2,sticky = W+E+N+S)
                self.confirmar.grid(row = 10,column = 2,columnspan = 5,sticky = W+E+N+S)
                if (bol[0]) or (bol[1]) or (bol[2]):
                    self.confirmar_nova_turma(bol)
                else:
                    self.adicionar_dados_novos(bol)
            else:
                self.escolha["text"] = "CPF com caracteres insuficientes"
                self.escolha["fg"] = "#b0020c"
        #O código acima é apenas para Turma, abaixa está para o resto
        if tipo != 'T':
            #Essa condição é chamada quando tiver algo errado com o cpf
            if valor:
                if cpfi:
                    self.escolha["text"] = "CPF com caracteres insuficientes"
                    self.escolha["fg"] = "#b0020c"
                else:
                    self.escolha["text"] = "Cpf já cadastrado no sistema"
                    self.escolha["fg"] = "#b0020c"
                self.confirmar["text"] = "Ok"
                self.confirmar["command"] = lambda : self.voltar_add(tipo)
            #Se ocorrer tudo certo será adicionado
            else:
                if tipo == 'A':
                    dados.add_novo_aluno()
                elif tipo == 'P':
                    dados.add_novo_professor()
                elif tipo == 'D':
                    dados.add_nova_disciplina()
                self.escolha["text"] = "Dados foram adicionados ao sistema."
                self.escolha["fg"] = "green"
    #Método para da uma mensagem em relação a turma, a qual está escrito que precisa adicionar dados novos
    def confirmar_nova_turma(self,valor):
        self.mensagem_aviso = Label(self.third_frame,bg ="#1a2e4f",fg ="#e39a07",font = ("Century","15","bold"))
        self.mensagem_aviso["text"] = "Há dados inseridos que não estão cadastrados\nno sistema,deseja cadastra-los?"
        self.mensagem_aviso.grid(row = 1,column=0,columnspan = 4,sticky = W+E+N+S)
        self.confirmar["text"] = "Sim"
        self.confirmar["command"] = lambda : self.adicionar_dados_turma(valor)
        self.voltar["text"] = "Não"
    #Destruir adicionar aluno
    def destruir_add_aluno(self):
        self.nome_pede.destroy()
        self.inserir_nome.destroy()
        self.cpf_pede.destroy()
        self.inserir_cpf.destroy()
        self.voltar.destroy()
        self.confirmar.destroy()
    #Destruir adicionar professor
    def destruir_add_professor(self):
        self.nome_pede.destroy()
        self.inserir_nome.destroy()
        self.cpf_pede.destroy()
        self.inserir_cpf.destroy()
        self.voltar.destroy()
        self.departamento_pede.destroy()
        self.inserir_departamento_professor.destroy()
        self.confirmar.destroy()
    #Destruir adicionar disciplina
    def destruir_add_disciplina(self):
        self.codigo_pede.destroy()
        self.inserir_codigo.destroy()
        self.nome_pede.destroy()
        self.inserir_nome.destroy()
        self.confirmar.destroy()
        self.voltar.grid_forget()
    #Destruir adicionar turma
    def destruir_add_turma(self):
        self.codigot_pede.destroy()
        self.inserir_codigot.destroy()
        self.periodo_pede.destroy()
        self.inserir_periodo.destroy()
        self.codigo_disciplina_pede.destroy()
        self.inserir_codigo_disciplina.destroy()
        self.cpf_professor_pede.destroy()
        self.inserir_cpf_professor.destroy()
        self.cpf_aluno_pede.destroy()
        self.inserir_cpf_aluno.destroy()
        self.confirmar.grid_forget()
        self.voltar.grid_forget()
    #Esses orientadores serve para lista que contêm em consultar,deletar e alterar. Eles dizem que coluna fica cada informação
    def orientadores(self,tipo):
        if tipo == 'A' or tipo == 'D':
            if tipo == 'A':
                self.orientadores_cpf = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font = ("Century","15","bold"),text = "CPF")        #
                self.orientadores_cpf.grid(row = 1,column = 1,sticky = W+E+N+S,ipadx= 40)
            else:
                self.orientadores_codigo = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font = ("Century","15","bold"),text = "Código")
                self.orientadores_codigo.grid(row = 1,column = 1,sticky = W+E+N+S,ipadx= 20)
            self.orientadores_nome = Label(self.third_frame_s,text = 'Nome', bg = "#424b5b",fg = "#e39a07",font = ("Century","15","bold"))       #
            self.orientadores_num.grid(row = 1,column = 0,sticky = W+E+N+S)
            self.orientadores_nome.grid(row = 1,column = 2,columnspan = 4,sticky = W+E+N+S,ipadx= 180)
        elif tipo == 'P':
            self.orientadores_cpf = Label(self.third_frame_s,text = 'CPF',bg = "#424b5b", fg = "#e39a07",font = ("Century","15","bold"))        #
            self.orientadores_departamento = Label(self.third_frame_s,text = "Departamento",bg = "#424b5b", fg = "#e39a07",font = ("Century","15","bold"))
            self.orientadores_nome = Label(self.third_frame_s,text = "Nome",bg = "#424b5b", fg = "#e39a07",font = ("Century","15","bold"))       #
            self.orientadores_num.grid(row = 1,column = 0,sticky = W+E+N+S)
            self.orientadores_cpf.grid(row = 1,column = 1,sticky = W+E+N+S,ipadx= 40)
            self.orientadores_departamento.grid(row = 1,column = 2,sticky = W+E+N+S,ipadx= 40)
            self.orientadores_nome.grid(row = 1,column = 3,columnspan = 3,sticky = W+E+N+S,ipadx= 150)
        elif tipo == 'T':
            self.orientadores_codigot = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font =("Century","15","bold"),text = 'Codigo da turma')
            self.orientadores_periodo = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font =("Century","15","bold"),text = 'Período')
            self.orientadores_codigod = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font =("Century","15","bold"),text = 'Codigo da disciplina')
            self.orientadores_cpfp = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font =("Century","15","bold"),text = 'CPF do Professor')
            self.orientadores_cpfa = Label(self.third_frame_s,bg = "#424b5b",fg = "#e39a07",font =("Century","15","bold"),text = 'CPF do aluno')
            self.orientadores_num.grid(row = 1,column = 0,sticky = W+E+N+S)
            self.orientadores_codigot.grid(row = 1,column = 1,sticky = W+E+N+S,ipadx = 10)
            self.orientadores_periodo.grid(row = 1,column = 2,sticky = W+E+N+S,ipadx = 10)
            self.orientadores_codigod.grid(row = 1,column = 3,sticky = W+E+N+S,ipadx = 10)
            self.orientadores_cpfp.grid(row = 1,column = 4,sticky = W+E+N+S,ipadx = 10)
            self.orientadores_cpfa.grid(row = 1,column = 5,sticky = W+E+N+S,ipadx = 10)
    #Apesar de ter nome de interface consultar, ele funciona para alterar e deletar, por isso que recebe o parâmetro de tipo(Professor,aluno,disciplina,turma)
    #e área(Consultar,deletar,alterar)
    def Interface_consultar(self,tipo,area):
        #Criação de uma frame específica, pois ela será apagada para atualizar para próxima lista ou para voltar
        self.third_frame_s = Frame(self.third_frame, bg = "#1a2e4f")
        self.third_frame_s.grid(row = 1,column = 0,rowspan=4,columnspan = 7,sticky = W+E+N+S)
        self.esconder_widgets_principais()
        self.con = True

        self.orientadores_num = Label(self.third_frame_s, bg = "#424b5b",fg = "#e39a07",font = ("Century","15","bold"),text = 'Numero')        #
        self.orientadores(tipo)
        self.escolha['fg'] = 'black'
        #Ler todo os dados do tipo estabelecido
        if tipo == 'A':
            janela = Aluno()
            self.dados = janela.read_aluno()
            self.escolha["text"] = "Lista de Alunos cadrastrados :"
        elif tipo == 'P':
            janela = Professor()
            self.dados = janela.read_professor()
            self.escolha["text"] = "Lista de Professores cadrastrados :"
        elif tipo == 'D':
            janela = Disciplina()
            self.dados = janela.read_disciplina()
            self.escolha["text"] = "Lista de Disciplinas cadrastradas :"
        elif tipo == 'T':
            janela = Turma()
            self.dados = janela.read_turma()
            self.escolha["text"] = "Lista de Turmas cadrastradas :"
        # Essa condição é chamada,pois quero que a lista tenha 10 lista cada página
        while len(self.dados) % 10 != 0 or self.dados == []:
            if tipo == 'A' or tipo == 'D':
                self.dados.append(("","",""))
            elif tipo == 'P':
                self.dados.append(("","","",""))
            elif tipo == 'T':
                self.dados.append(("","","","","",""))

        self.todas_as_linhas_consultar(tipo,area)
        #Criação do botão para ir para próximo nomes da lista
        self.rightbutton = Button(self.third_frame_s)
        self.rightbutton["text"] = ">"
        self.rightbutton['fg'] = "#e39a07"
        self.rightbutton["font"] = ("Century","10","bold")
        self.rightbutton["command"] = lambda : self.Proximo_lista(tipo,area)
        self.rightbutton.grid(row = 12, column = 5,sticky = E)  #

        self.voltar.grid(row = 13,column = 0,columnspan = 7,sticky = W+E+N+S)
        self.voltar["command"] = lambda : self.menu_area(tipo)

    #Este método ele pegar toda dados e coloca em labels             
    def todas_as_linhas_consultar(self,tipo,area):
        self.tipo = tipo
        self.area = area
        #Labels para departamento
        if tipo == 'P':
            for k in range(10):
                self.third_label1 = Label(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][3] )
                self.third_label1.grid(row = 2+k, column = 2)

        #Labels para criar botão de alterar
        if area == 'A':
            self.orientadores_num['text'] = '-'
            for k in range(10):
                self.botao_1 = Button(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f", activebackground = "#1a2e4f",fg = "white",
                                      activeforeground = "white",command = partial(self.posição_a_ação,self.p+k),text = 'ALTERAR')
                self.botao_1.grid(row = 2+k,column = 0,sticky = W+E)
        #Labels para criar botão de deletar
        elif area == 'D':
            self.orientadores_num['text'] = '-'
            for k in range(10):
                self.botao_1 = Button(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f", activebackground = "#1a2e4f",fg = "white",
                                      activeforeground = "white",command = partial(self.posição_a_ação,self.p+k),text = 'DELETAR')
                self.botao_1.grid(row = 2+k,column = 0,sticky = W+E)
        else:
            #Labels ordenar na lista
            self.orientadores_num['text'] = 'Posição'
            for k in range(10):
                self.botao_1 = Label(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg = "white",
                                     text = self.p+k+1)
                self.botao_1.grid(row = 2+k,column = 0,sticky = W+E)
        #Labels para todo informações de turmas 
        if tipo == 'T':
            for k in range(10):
                self.label_codigot = Label(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][1])
                self.label_codigot.grid(row = 2+k,column = 1)
            for k in range(10):
                self.label_periodo = Label(self.self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][2])
                self.label_periodo.grid(row = 2+k,column = 2)
            for k in range(10):
                self.label_codigod = Label(self.self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][3])
                self.label_codigod.grid(row = 2+k,column = 3)
            for k in range(10):
                self.label_cpfp = Label(self.self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][4])
                self.label_cpfp.grid(row = 2+k,column = 4)
            for k in range(10):
                self.label_cpfa = Label(self.self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][5])
                self.label_cpfa.grid(row = 2+k,column = 5)

            
        else:
            for k in range(10):
                self.first_label1 = Label(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][2])
                self.first_label1.grid(row = 2+k,column = 1)
            for k in range(10):      
                self.nome1 = Label(self.third_frame_s,font = ("Century","10","bold"),bg = "#1a2e4f",fg ="white",text = self.dados[self.p+k][1])
                if tipo == 'A' or tipo == 'D':
                    self.nome1.grid(row = 2+k, column = 2,columnspan = 4)
                elif tipo == 'P':
                    self.nome1.grid(row = 2+k, column = 3,columnspan = 3)

    def posição_a_ação(self,p):
        if self.area == 'A':
            self.alterar_aluno(p,self.tipo,self.area)
        else:
            self.deletar_aluno(p,self.tipo,self.area)
            
        
    #Método para próximo da lista
    def Proximo_lista(self,tipo,area):
        if self.p+10 < len(self.dados):
            self.p+=10
            self.rollback_consulta_aluno()
            self.Interface_consultar(tipo,area)
            if self.p >= 10:
                self.leftbutton = Button(self.third_frame_s)
                self.leftbutton["text"] = "<"
                self.leftbutton["font"] = ("Century","10","bold")
                self.leftbutton['fg'] = "#e39a07"
                self.leftbutton["command"] = lambda : self.Anterior_lista(tipo,area)
                self.leftbutton.grid(row= 12, column = 0,sticky = W)
    
            if self.p == len(self.dados)-10:
                self.rightbutton.grid_forget()
    #Método para anterior da lista
    def Anterior_lista(self,tipo,area):
        if self.p-10 >=0:
            if self.p == len(self.dados)-10:
                self.rightbutton.grid(row = 12, column = 5,sticky = E)
            self.p-=10
            self.rollback_consulta_aluno()
            self.Interface_consultar(tipo,area)
            if self.p >= 10:
                self.leftbutton = Button(self.third_frame_s)
                self.leftbutton["text"] = "<"
                self.leftbutton["font"] = ("Century","10","bold")
                self.leftbutton['fg'] = "#e39a07"
                self.leftbutton["command"] = lambda : self.Anterior_lista(tipo,area)
                self.leftbutton.grid(row= 12, column = 0,sticky = W)
    #aqui é para deletar a frame para ir para próxima página ou sair da lista
    def rollback_consulta_aluno(self):
        self.third_frame_s.destroy()
    #Esse método ele pega o id do dado e aproveita o método adicionar para fazer alterações
    def alterar_aluno(self,posição,tipo,area):
        self.posição = posição
        self.id = self.dados[posição][0]
        self.rollback_consulta_aluno()

        self.voltar.grid(row = 4,column = 0,columnspan = 4,sticky = W+E+N+S)

        self.interface_add(tipo)
        self.voltar['command'] = lambda : self.voltar_alterar(tipo,area)
        self.escolha["text"] = "Alterar : (Escreva nada se não quiser alterar)"
        self.escolha["fg"] = "black"
        self.escolha["font"] = ("Century","14","bold")
        self.confirmar["command"] = lambda : self.alterar_dados_alunos(tipo,area)
    #Destroi adicionar e chama a lista
    def voltar_alterar(self,tipo,area):
        if tipo == 'A':
            self.destruir_add_aluno()
        elif tipo == 'P':
            self.destruir_add_professor()
        elif tipo == 'D':
            self.destruir_add_disciplina()
        elif tipo == 'T':
            self.destruir_add_turma()
        self.voltar = Button(self.third_frame,text = "Voltar",command = self.comandos_menu_principal,font = ("Century","10","bold"),fg = "#e39a07",
                             activeforeground = "#e39a07",bg = "#1a2e4f",activebackground = "#1a2e4f")
        self.Interface_consultar(tipo,area)
    #Alterar no banco de dados
    def alterar_dados_alunos(self,tipo,area):
        valor = False
        if tipo == 'A':
            dados = Aluno(self.inserir_nome.get(),self.inserir_cpf.get())
            valor = dados.pesquisa_aluno(self.inserir_cpf.get())
        elif tipo == 'P':
            dados = Professor(self.inserir_nome.get(),self.inserir_cpf.get(),self.inserir_departamento_professor.get())
            valor = dados.pesquisa_professor(self.inserir_cpf.get())
        elif tipo == 'D':
            dados = Disciplina(self.inserir_nome.get(),self.inserir_codigo.get())
            valor = dados.pesquisa_disciplina(self.inserir_codigo.get())
        elif tipo == 'T':
            dados = Turma(self.inserir_codigot.get(),self.inserir_periodo.get(),self.inserir_codigo_disciplina.get(),self.inserir_cpf_professor.get(),self.inserir_cpf_aluno.get())
        if valor :
            if tipo == 'A' or tipo == 'P':
                self.escolha["text"] = "CPF ja cadastrado no sistema, porfavor insira outro."
            elif tipo == 'D':
                self.escolha["text"] = "Codigo ja cadastrado no sistema, porfavor insira outro."
            self.escolha["font"] = ("Century","13","bold")
            self.escolha["fg"] = "red"
            self.confirmar["text"] = "OK"
            self.confirmar["command"] = lambda : self.alterar_aluno(self.posição,tipo,area)
        else:
            if tipo == 'A':
                dados.update_aluno(self.id)
            elif tipo == 'P':
                dados.update_professor(self.id)
            elif tipo == 'D':
                dados.update_disciplina(self.id)
            elif tipo == 'T':
                dados.update_turma(self.id)
            self.escolha["text"] = "Dados alterados"
            self.escolha["fg"] = "green"
            self.confirmar["text"] = "OK"
            self.confirmar["command"] = lambda : self.voltar_alterar(tipo,area)
    #Deletar aluno tem uma mensagem perguntando se deseja deletar e mostra os dados que será deletado
    def deletar_aluno(self,posição,tipo,area):
        self.posição = posição
        self.rollback_deletar(tipo)
        self.id = self.dados[posição][0]
        self.Mensagem1 = Label(self.third_frame)
        self.Mensagem1["text"] = "Tem certeza que deseja deletar os seguintes dados :"
        self.Mensagem2 = Label(self.third_frame)
        if tipo == 'A':
            self.Mensagem2["text"] = "\nNome : \n%s \n\nCPF : \n%s\n"%(self.dados[posição][1],self.dados[posição][2])
        elif tipo == 'P':
            self.Mensagem2["text"] = "\nNome : \n%s \n\nCPF : \n%s \n\nDepartamento : \n%s\n"%(self.dados[posição][1],self.dados[posição][2],self.dados[posição][3])
        elif tipo == 'D':
            self.Mensagem2["text"] = "\nNome : \n%s \n\nCódigo : \n%s \n"%(self.dados[posição][1],self.dados[posição][2])
        elif tipo == 'T':
            self.Mensagem2["text"] = "\nCódigo da Turma : \n%s \n\nPeríodo : \n%s \n\nCódigo da disciplina : \n%s \n\nCPF do professor : \n%s \n\nCPF do aluno : \n%s \n"%(self.dados[posição][1],self.dados[posição][2],
                                                                                                                                                                           self.dados[posição][3],self.dados[posição][4],
                                                                                                                                                                           self.dados[posição][5])
        self.Mensagem1["bg"] = self.Mensagem2["bg"] = "#1a2e4f"
        self.Mensagem1["fg"] = self.Mensagem2["fg"] = "#e39a07"
        self.Mensagem1["font"] = self.Mensagem2["font"] =("Century","14","bold")
        self.Mensagem1.grid(row = 1,column = 0,columnspan = 4)
        self.Mensagem2.grid(row=2,column =0,columnspan = 4,rowspan = 6)
        self.escolha["text"] = "Confirmação"

        self.confirmar = Button(self.third_frame)
        self.confirmar["text"] = "Confirmar"
        self.confirmar["font"] = ("Century","10","bold")
        self.confirmar["fg"]= self.confirmar["activeforeground"]  = "#e39a07"
        self.confirmar["bg"] = self.confirmar["activebackground"] = "#1a2e4f"
        self.confirmar["width"] = 20
        self.confirmar["command"] = lambda : self.deletar_dados_alunos(tipo,area)
        self.confirmar.grid(row=8,column = 2,columnspan = 2,sticky = W+E+N+S)

        self.voltar["command"] = lambda : self.voltar_deletar(tipo,area)
        self.voltar.grid(row = 8,column = 0,columnspan = 2,sticky = W+E+N+S)


    def voltar_deletar(self,tipo,area):
        self.Mensagem1.destroy()
        self.Mensagem2.destroy()
        self.confirmar.destroy()
        self.Interface_consultar(tipo,area)
    #Confirmado será exercutado esse método que irá deletar o dado
    def deletar_dados_alunos(self,tipo,area):
        if tipo == 'A':
            dados = Aluno()
            dados.delete_aluno(self.id)
        elif tipo == 'P':
            dados = Professor()
            dados.delete_professor(self.id)
        elif tipo == 'D':
            dados = Disciplina()
            dados.delete_disciplina(self.id)
        elif tipo == 'T':
            dados = Turma()
            dados.delete_turma(self.id)
        self.voltar_deletar(tipo,area)
        self.p = 0

    def rollback_deletar(self,tipo):
        if tipo == 'T':
            self.orientadores_codigot.destroy()
            self.orientadores_periodo.destroy()
            self.orientadores_codigod.destroy()
            self.orientadores_cpfp.destroy()
            self.orientadores_cpfa.destroy()
        else:
            self.orientadores_num.destroy()
            if tipo == 'A' or tipo == 'P':
                self.orientadores_cpf.destroy()
            self.orientadores_nome.destroy()
            if tipo == 'D':
                self.orientadores_codigo.destroy()
            if tipo == 'P':
                self.orientadores_departamento.destroy()
        self.rollback_consulta_aluno()
    #A parti daqui é relatório de aluno e professor
    def Relatório_menu(self):
        self.voltar = Button(self.third_frame,text = 'Voltar',command = self.rollback_relatório,font = ("Century","10","bold"),
                             fg = "#e39a07",activeforegroun = "#e39a07",bg = "#1a2e4f",activebackgroun = "#1a2e4f")
        self.voltar.grid(row = 4,column = 0,columnspan = 5,sticky = W+E+N+S)
        self.esconder_widgets_principais()
        #Botões para escolha de qual ação queira agir
        self.escolha1 = Button(self.third_frame,text = 'Gerar relatório do Professor',font = ("Century","15","bold"),fg = "#e39a07",activeforeground = "#e39a07",
                               bg = "#1a2e4f",activebackground = "#1a2e4f",command = self.lista_lista_de_professores)
        self.escolha2 = Button(self.third_frame,text = 'Gerar relatório do Aluno',font = ("Century","15","bold"),fg = "#e39a07",activeforeground = "#e39a07",
                               bg = "#1a2e4f",activebackground = "#1a2e4f",command = self.lista_lista_de_aluno)
        self.escolha3 = Button(self.third_frame,text = 'Gerar a Ata de exercício',font = ("Century","15","bold"),fg = "#e39a07",activeforeground = "#e39a07",
                               bg = "#1a2e4f",activebackground = "#1a2e4f",command = self.Pede_turma)
        self.escolha1.grid( row = 1, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha2.grid( row = 2, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha3.grid( row = 3, column = 0,columnspan = 4,sticky = W+E+N+S)
    # O relatório é baseado em listbox que o usuário seleciona o dado e ele é capturado 
    def rollback_relatório(self):
        self.voltar.destroy()
        self.escolha1.destroy()
        self.escolha2.destroy()
        self.escolha3.destroy()
        self.voltar_widget_principais()

    def lista_lista_de_professores(self):
        self.escolha1.grid_forget()
        self.escolha2.grid_forget()
        self.escolha3.grid_forget()
        
        dados = Professor()
        self.professores = dados.read_professor()
        self.scroll = Scrollbar(self.third_frame)
        self.listbox = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))

        for professor in self.professores:
            self.listbox.insert(END, "{0:}|||{1:}|||{2:}".format(professor[2],professor[1],professor[3]))

        self.scroll.config(command = self.listbox.yview)

        self.botão = Button(self.third_frame,text = 'Escolher',command = self.posição_na_lista_professor,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07" )
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)

        self.listbox.grid(row = 1,column = 0,columnspan = 4,sticky =W+E)
        self.scroll.grid(row = 1,column = 4,sticky = N+S)
        self.voltar["command"] = self.apagar_

    def apagar_(self):
        self.scroll.destroy()
        self.listbox.destroy()
        self.botão.destroy()
        self.voltar["command"] = self.rollback_relatório
        self.escolha1.grid( row = 1, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha2.grid( row = 2, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha3.grid( row = 3, column = 0,columnspan = 4,sticky = W+E+N+S)

    def posição_na_lista_professor(self):
        self.listbox.grid_forget()
        self.scroll.grid_forget()
        self.posição = int(str(self.listbox.curselection())[1:-1].strip(','))
        self.botão0 = Button(self.third_frame,text = 'Todas Turmas',command = self.Todas_turmas_professor,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07")
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.botão['text'] = 'Por período'
        self.botão['command'] = self.Turmas_periodo_professor
        self.voltar["command"] = self.apagar_1

    def apagar_1(self):
        self.botão0.destroy()
        self.botão['command'] = self.posição_na_lista_professor
        self.botão['text'] = 'Escolher'
        self.listbox.grid(row = 1,column = 0,columnspan = 4,sticky =W+E)
        self.scroll.grid(row = 1,column = 4,sticky = N+S)
        self.voltar["command"] = self.apagar_

    def Todas_turmas_professor(self):
        self.botão0.grid_forget()
        self.botão.grid_forget()
        lista = Relatório()
        dic1 = lista.Todas_turmas_prof(self.professores[self.posição][2])
        self.listbox1 = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))
        self.listbox1.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        for a in dic1:
            o = a.split('/')
            self.listbox1.insert(END, "Turma:%s ||| Período: %s"%(o[0],o[1]))
            for b in dic1[a]:
                self.listbox1.insert(END,"{0:}{1:<60}".format(' '*10,b))
        self.voltar["command"] = self.apagar_2

    def apagar_2(self):
        self.listbox1.grid_forget()
        self.scroll.grid_forget()
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.voltar["command"] = self.apagar_1

    def Turmas_periodo_professor(self):
        self.botão0.grid_forget()
        self.botão.grid_forget()
        lista = Relatório()
        self.periodos = set(lista.Periodo_prof(self.professores[self.posição][2]))
        self.periodos = tuple(self.periodos)
        self.listbox1 = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))
        self.listbox1.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        for a in self.periodos:
            self.listbox1.insert(END, "{}".format(a[0]))
        self.botãop = Button(self.third_frame,text = 'Escolher',command = self.periodo_professor,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07" )
        self.botãop.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.voltar["command"] = self.apagar_3

    def apagar_3(self):
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.listbox1.destroy()
        self.botãop.destroy()
        self.voltar["command"] = self.apagar_1

    def periodo_professor(self):
        self.botãop.grid_forget()
        self.local = int(str(self.listbox1.curselection())[1:-1].strip(','))
        periodo = self.periodos[self.local][0]
        self.listbox1.delete(0,'end')
        lista = Relatório()
        l = lista.Lista_periodo_prof(self.professores[self.posição][2],periodo)
        self.listbox1.insert(END, "___{}___:".format(periodo))
        for a in l:
            self.listbox1.insert(END, "_{}_:".format(a))
            for b in l[a]:
                self.listbox1.insert(END, "{0:}{1:<60}".format(' '*10,b))



    def lista_lista_de_aluno(self):
        self.escolha1.grid_forget()
        self.escolha2.grid_forget()
        self.escolha3.grid_forget()
        
        dados = Aluno()
        self.alunos = dados.read_aluno()
        self.scroll = Scrollbar(self.third_frame)
        self.listbox = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))

        for aluno in self.alunos:
            self.listbox.insert(END, "{0:}|||{1:}".format(aluno[1],aluno[2]))

        self.scroll.config(command = self.listbox.yview)

        self.botão = Button(self.third_frame,text = 'Escolher',command = self.posição_na_lista_aluno,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07" )
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)

        self.listbox.grid(row = 1,column = 0,columnspan = 4,sticky =W+E)
        self.scroll.grid(row = 1,column = 4,sticky = N+S)
        self.voltar["command"] = self.apagar_4

    def apagar_4(self):
        self.scroll.destroy()
        self.listbox.destroy()
        self.botão.destroy()
        self.voltar["command"] = self.rollback_relatório
        self.escolha1.grid( row = 1, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha2.grid( row = 2, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha3.grid( row = 3, column = 0,columnspan = 4,sticky = W+E+N+S)

    def posição_na_lista_aluno(self):
        self.listbox.grid_forget()
        self.scroll.grid_forget()
        self.posição = int(str(self.listbox.curselection())[1:-1].strip(','))
        self.botão0 = Button(self.third_frame,text = 'Todas Turmas',command = self.Todas_turmas_aluno,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07")
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.botão['text'] = 'Por período'
        self.botão['command'] = self.Turmas_periodo_aluno
        self.voltar["command"] = self.apagar_1

    def apagar_5(self):
        self.botão0.destroy()
        self.botão['command'] = self.posição_na_lista_aluno
        self.botão['text'] = 'Escolher'
        self.listbox.grid(row = 1,column = 0,columnspan = 4,sticky =W+E)
        self.scroll.grid(row = 1,column = 4,sticky = N+S)
        self.voltar["command"] = self.apagar_4

    def Todas_turmas_aluno(self):
        self.botão0.grid_forget()
        self.botão.grid_forget()
        lista = Relatório()
        dic1 = lista.Todas_turmas_aluno(self.alunos[self.posição][2])
        self.listbox1 = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))
        self.listbox1.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        for a in dic1:
            o = a.split('/')
            self.listbox1.insert(END, "Turma:%s ||| Período: %s"%(o[0],o[1]))
            for b in dic1[a]:
                self.listbox1.insert(END,"{0:}{1:<60}".format(' '*10,b))
            
        self.voltar["command"] = self.apagar_6

    def apagar_6(self):
        self.listbox1.grid_forget()
        self.scroll.grid_forget()
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.voltar["command"] = self.apagar_5

    def Turmas_periodo_aluno(self):
        self.botão0.grid_forget()
        self.botão.grid_forget()
        lista = Relatório()
        self.periodos = set(lista.Periodo_aluno(self.alunos[self.posição][2]))
        self.periodos = tuple(self.periodos)
        self.listbox1 = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))
        self.listbox1.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        for a in self.periodos:
            self.listbox1.insert(END, "{}".format(a[0]))
        self.botãop = Button(self.third_frame,text = 'Escolher',command = self.periodo_aluno,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07" )
        self.botãop.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.voltar["command"] = self.apagar_7

    def apagar_7(self):
        self.botão0.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.listbox1.destroy()
        self.botãop.destroy()
        self.voltar["command"] = self.apagar_5

    def periodo_aluno(self):
        self.botãop.grid_forget()
        self.local = int(str(self.listbox1.curselection())[1:-1].strip(','))
        periodo = self.periodos[self.local][0]
        self.listbox1.delete(0,'end')
        lista = Relatório()
        l = lista.Lista_periodo_aluno(self.alunos[self.posição][2],periodo)
        self.listbox1.insert(END, "___{}___:".format(periodo))
        for a in l:
            self.listbox1.insert(END, "_{}_:".format(a))
            for b in l[a]:
                self.listbox1.insert(END, "{0:}{1:<60}".format(' '*10,b))

    def Pede_turma(self):
        self.escolha1.grid_forget()
        self.escolha2.grid_forget()
        self.escolha3.grid_forget()
        self.listbox = Listbox(self.third_frame,bg ="#1a2e4f",fg = "#e39a07",font = ("Century","10","bold"))
        self.listbox.grid(row = 1,column = 0,columnspan = 5,sticky =W+E)
        self.dado = Relatório()
        self.turmas = self.dado.todas_turmas()
        for a in self.turmas:
            self.listbox.insert(END, "{}".format(a[0]))
        self.botão = Button(self.third_frame,text = 'Escolher',command = self.Pede_periodo,font =("Century","12","bold"),bg ="#1a2e4f",fg = "#e39a07" )
        self.botão.grid(row=2,column =0,columnspan = 5,sticky = W+E)
        self.voltar['command'] = self.tirar_ata

    def Pede_periodo(self):
        p = int(self.listbox.curselection()[0])
        self.turma = self.turmas[p][0]
        self.listbox.delete(0,'end')
        self.periodos = self.dado.todos_periodos(self.turma)
        for a in self.periodos:
            self.listbox.insert(END, "{}".format(a[0]))
        self.botão['command'] = self.Pede_professor
        
    def Pede_professor(self):
        p = int(self.listbox.curselection()[0])
        self.periodo = self.periodos[p][0]
        self.listbox.delete(0,'end')
        self.professores = self.dado.todos_professores(self.periodo,self.turma)
        for a in self.professores:
            self.listbox.insert(END, "{} ||| {}".format(a[0],a[1]))
        self.botão['command'] = self.Pede_disciplina

    def Pede_disciplina(self):
        p = int(self.listbox.curselection()[0])
        self.professor = self.professores[p]
        self.listbox.delete(0,'end')
        self.disciplinas = self.dado.todos_disciplina(self.periodo,self.professor[1],self.turma)
        for a in self.disciplinas:
            self.listbox.insert(END, "{}".format(a[0]))
        self.botão['command'] = self.Pegar_disciplina
        
    def Pegar_disciplina(self):
        p = int(self.listbox.curselection()[0])
        self.disciplina = self.disciplinas[p]
        self.alunos = self.dado.lista_alunos(self.periodo,self.turma,self.professor[1],self.disciplina[1])
        top = Toplevel()
        ata = Ata(self.periodo,self.professor,self.disciplina,self.turma,self.alunos,top)

    def tirar_ata(self):
        self.listbox.destroy()
        self.botão.destroy()
        self.escolha1.grid( row = 1, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha2.grid( row = 2, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.escolha3.grid( row = 3, column = 0,columnspan = 4,sticky = W+E+N+S)
        self.voltar['command'] = self.rollback_relatório
        
#O que é executado todo vez que abre:
root = Tk()
instancia = Interface(root)
root.wm_iconbitmap("CRUD.ico")
root.winfo_width()
root.title("CRUD UFRPE")
root["bg"] = "#46679f"
largura, altura = (root.winfo_screenwidth()), (root.winfo_screenheight())
root.geometry("+150+50")
root.resizable(width=False, height=False)
root.mainloop()
