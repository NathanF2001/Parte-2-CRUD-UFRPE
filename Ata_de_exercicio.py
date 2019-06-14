from tkinter import *
from datetime import datetime

class Ata(object):
    #Método construtor para guardar todas as informações adquiridas. Elas serão utilizadas para colocá-las na ata
    #É bom enfatizar que o parâmetro top, é o Toplevel, que é uma janela que é aberta a parte do programa, e ela conterá a ata
    def __init__(self,periodo= '',professor = [],disciplina = [],turma = '',alunos = [],top = ''):
        self.periodo = periodo
        self.professor = professor
        self.disciplina = disciplina
        self.turma = turma
        self.alunos = alunos
        self.top = top
        self.interface()

    def interface(self):
        #datetime é para pega a hora e a data que pediu para gerar
        data = datetime.now()
        #Criação de frame para conter as Labels
        self.frame_principal = Frame(self.top,bg = 'white',relief = 'flat',highlightbackground = 'black',
                                     highlightthickness= 2)
        self.frame_principal.grid(row=0,column = 0,sticky = W+E+N+S)
        #Label da logo da UFRPE
        ufrpe_logo2 = PhotoImage(file = "ufrpe_logo2.gif")
        self.ufrpe_logo = Label(self.frame_principal,bg = 'white')
        self.ufrpe_logo["image"] = ufrpe_logo2
        self.ufrpe_logo.image = ufrpe_logo2
        self.ufrpe_logo.grid(row = 0,rowspan = 4,column = 0,sticky = N)
        #Label texto 
        Texto1 = Label(self.frame_principal,bg = 'white',font = ('Calibri','16'))
        Texto1['text'] = 'UNIVERSIDADE FEDERAL RURAL DE\nPERNAMBUCO'
        Texto1.grid(row = 0, column = 2, columnspan = 3,ipadx = 40)
        #Label texto
        Texto2 = Label(self.frame_principal,bg = 'white',font = ('Calibri','12'))
        Texto2['text'] = 'DEPARTAMENTO DE REGISTRO E CONTROLE ACADÊMICO\nCOORD. DE BACHARELADO SISTEMAS DE INFORMAÇÃO'
        Texto2.grid(row = 1, column = 1, columnspan = 5)
        #Label texto
        Texto3 = Label(self.frame_principal,bg = 'white',font = ('Calibri','12','bold'))
        Texto3['text'] = 'Ata de Presença'
        Texto3.grid(row = 2, column = 1, columnspan = 5)
        #Label texto
        Texto4 = Label(self.frame_principal,bg = 'white',font = ('Calibri','11'))
        Texto4['text'] = '{:0>2}/{:0>2}/{}'.format(data.day,data.month,data.year)
        Texto4.grid(row = 3, column = 1, columnspan = 5)
        #Label texto
        dia = Label(self.frame_principal,bg = 'white',font = ('Calibri','11'))
        dia['text'] = 'DATA:{:0>2}/{:0>2}/{}'.format(data.day,data.month,data.year)
        dia.grid(row = 0, column = 6, sticky = S)
        #Label texto
        hora = Label(self.frame_principal,bg = 'white',font = ('Calibri','11'))
        hora['text'] = 'HORA:{:0>2}:{:0>2}'.format(data.hour,data.minute)
        hora.grid(row = 1, column = 6, sticky = N)
        #Frame secundária onde terá as informações que foram adquiridas, sem ser os nomes que será guardada em outra frame
        self.frame_secundaria = Frame(self.top,bg = 'black',relief = 'solid',highlightbackground = 'black',
                                     highlightthickness= 2)
        self.frame_secundaria.grid(row=0,column = 1,sticky = W+E+N+S)
        #Label texto
        Texto4 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'CÓDIGO DA DISCIPLINA',
                       relief = 'solid',borderwidth=1,width = 19)
        Texto4.grid(row = 0, column = 0,sticky = W)
        #Label texto da disciplina
        Mensagem1 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = self.disciplina[1],relief = 'solid',borderwidth=1,width = 19)
        Mensagem1.grid(row = 1, column = 0,sticky = W)
        #Label texto
        Texto5 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'PERÍODO',
                       relief = 'solid',borderwidth=1,width = 19)
        Texto5.grid(row = 0, column = 1,sticky = W)
        #Label texto período
        Mensagem2 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = self.periodo,relief = 'solid',borderwidth=1,width = 19)
        Mensagem2.grid(row = 1, column = 1,sticky = W)
        #Label texto
        Texto6 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'TURMA',
                       relief = 'solid',borderwidth=1,width = 9)
        Texto6.grid(row = 0, column = 2,sticky = W)
        #Label texto turma
        Mensagem3 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = self.turma,relief = 'solid',borderwidth=1,width = 9)
        Mensagem3.grid(row = 1, column = 2,sticky = W)
        #Label texto
        Texto7 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'VAGAS',
                       relief = 'solid',borderwidth=1,width = 9)
        Texto7.grid(row = 0, column = 3,sticky = W)
        #Label texto vagas
        Mensagem4 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = '0',relief = 'solid',borderwidth=1,width = 9)
        Mensagem4.grid(row = 1, column = 3,sticky = W)
        #Label texto
        Texto8 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'NOME DA DISCIPLINA',
                       relief = 'solid',borderwidth=1,width = 9)
        Texto8.grid(row = 2, column = 0,columnspan = 5,ipadx = 245,sticky = W)
        #Label texto nome da disciplina
        Mensagem5 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = self.disciplina[0],relief = 'solid',borderwidth=1,width = 9)
        Mensagem5.grid(row = 3, column = 0,columnspan = 5,sticky = W,ipadx = 245)
        #Label texto
        Texto9 = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'NOME DO PROFESSOR(ES)',
                       relief = 'solid',borderwidth=1,width = 9)
        Texto9.grid(row = 4, column = 0,columnspan = 5,ipadx = 245,sticky = W)
        #Label texto nome do professor
        Mensagem6 = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = self.professor[0],relief = 'solid',borderwidth=1,width = 9,height = 2)
        Mensagem6.grid(row = 5, column = 0,columnspan = 5,sticky = W,ipadx = 245)
        # Essa frame é so para ter uma espaçamento entre as frames acima e que vem a seguir
        self.mensagem_branco = Frame(self.top,bg = 'white')
        self.mensagem_branco.grid(row = 1,column = 0,columnspan = 2,sticky = W+E+N+S)
        #--------Frame Nomes------------
        self.frame_nomes = Frame(self.top,bg = 'white',relief = 'flat',highlightbackground = 'black',
                                     highlightthickness= 2)
        self.frame_nomes.grid(row=2,column = 0,columnspan= 2,sticky = W+E+N+S)
        #Coluna da posição ordenada
        ORD = Label(self.frame_nomes,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'ORD',relief = 'solid',borderwidth=1,width = 4)
        ORD.grid(row=0,column = 0)
        #Coluna da Nota dos alunos
        NOTA = Label(self.frame_nomes,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'NOTA',relief = 'solid',borderwidth=1,width = 7)
        NOTA.grid(row=0,column = 1)
        #Coluna do CPF do aluno
        CPF = Label(self.frame_nomes,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'CPF',relief = 'solid',borderwidth=1,width = 14)
        CPF.grid(row=0,column = 2)
        #Coluna do nome do aluno
        ALUNO = Label(self.frame_nomes,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'NOME DO(A) ALUNO(A)',relief = 'solid',borderwidth=1,width = 57)
        ALUNO.grid(row=0,column = 3)
        #Coluna das assinaturas
        ASI = Label(self.frame_nomes,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'ASSINATURA',relief = 'solid',borderwidth=1,width = 57)
        ASI.grid(row=0,column = 4)
        #self.p é a posição na lista do dados do aluno
        self.p = 0
        #self.pag é a página da ata de exercício
        self.pag = 1
        #A ata terá 22 alunos por página por isso que coloco a condição para ter um número que seja dividido por 22
        while len(self.alunos) % 22 != 0 or len(self.alunos) == 0:
            self.alunos.append(['',''])
        #Condição para criação de um botão para é para o próximos nomes
        if len(self.alunos)>22:
            self.rightbutton = Button(self.mensagem_branco, text = '>',bg = 'black',fg = 'white',command = self.Proximo)
            self.rightbutton.pack(side = RIGHT)
        self.todos_nomes()

        self.top.mainloop()

    #Aqui irá pega os dados dos alunos e organizará nas respectiva colunas
    def todos_nomes(self):
        #Essas duas Labels estão aqui pois elas são dinâmicas vão está mudado sempre que a página foi trocado
        PAGT = Label(self.frame_secundaria,bg = '#d1d1d1',font = ('Calibri','11','bold'),text = 'PÁGINA',
                       relief = 'solid',borderwidth=1,width = 9)
        PAGT.grid(row = 0, column = 4,sticky = W)

        PAGR = Label(self.frame_secundaria,bg = 'white',font = ('Calibri','11'),text = '{}/{}'.format(self.pag,len(self.alunos)//22),relief = 'solid',borderwidth=1,width = 9)
        PAGR.grid(row = 1, column = 4,sticky = W)
        #Coluna de posição        
        t = 1
        for a in range(22):
            ORD = Label(self.frame_nomes,bg = 'white',font = ('Calibri','11','bold'),text = self.p+t,relief = 'solid',borderwidth=1,width = 4)
            ORD.grid(row = t,column = 0)
            t+=1
        #Coluna de Notas
        n = 1
        for a in range(22):
            NOTA = Label(self.frame_nomes,bg = 'white',font = ('Calibri','11','bold'),text = '',relief = 'solid',borderwidth=1,width = 7)
            NOTA.grid(row=n,column = 1)
            n+=1
        #Coluna de Cpf's
        c = 0
        for a in range(22):
            CPF = Label(self.frame_nomes,bg = 'white',fg = 'blue',font = ('Calibri','11','bold'),text = self.alunos[self.p+c][1],relief = 'solid',borderwidth=1,width = 14)
            CPF.grid(row=c+1,column = 2)
            c+=1
        #Coluna de nome do aluno
        n = 0
        for a in range(22):
            ALUNO = Label(self.frame_nomes,bg = 'white',fg = 'blue',font = ('Calibri','11','bold'),text = self.alunos[self.p+n][0],relief = 'solid',borderwidth=1,width = 57)
            ALUNO.grid(row=n+1,column = 3)
            n+=1
        #Coluna de assinatura
        s = 1
        for a in range(22):
            ASI = Label(self.frame_nomes,bg = 'white',font = ('Calibri','11','bold'),text = '',relief = 'solid',borderwidth=1,width = 57)
            ASI.grid(row=s,column = 4)
            s+=1
    #Metodo para ir para próxima página
    def Proximo(self):
        self.p += 22
        if self.pag == 1:
            self.leftbutton = Button(self.mensagem_branco, text = '<',bg = 'black',fg = 'white',command = self.Anterior)
            self.leftbutton.pack(side = LEFT)
        self.pag += 1
        if self.pag == len(self.alunos)//22:
            self.rightbutton.pack_forget()
        self.todos_nomes()
    #Método para ir para página anterior
    def Anterior(self):
        self.p -= 22
        if self.pag == len(self.alunos)//22:
            self.rightbutton.pack(side = RIGHT)
        self.pag -=1
        if self.pag == 1:
            self.leftbutton.pack_forget()
        self.todos_nomes()
