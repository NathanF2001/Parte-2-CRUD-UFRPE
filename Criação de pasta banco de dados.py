import sqlite3
# O id vai servir para eu reconhecer o dados, sem precisar ta reconhecendo pelo
# nome,cpf,departamento,turma, e etc.

#------Criação do banco de dados Alunos --------
conexão = sqlite3.connect("Alunos.db")
cursor = conexão.cursor()
cursor.execute("""create table Alunos(
                id integer primary key autoincrement, 
                nome text,
                cpf text) """)# Aqui tou representando que cada dado vai ser uma
                             # Tupla contendo (id,nome,cpf)
conexão.commit() # Aquela salvada básica
cursor.close()
conexão.close()

#------Criação do banco de dados Professores --------
conexão = sqlite3.connect("Professores.db")
cursor = conexão.cursor()
cursor.execute("""create table Professores(
                id integer primary key autoincrement, 
                nome text,
                cpf text,
                departamento text)""")# Aqui tou representando que cada dado vai ser uma
                                      # Tupla contendo (id,nome,cpf,departamento)
conexão.commit() # Aquela salvada básica
cursor.close()
conexão.close()

#------Criação do banco de dados Disciplinas --------
conexão = sqlite3.connect("Disciplinas.db")
cursor = conexão.cursor()
cursor.execute("""create table Disciplinas(
                id integer primary key autoincrement, 
                nome text,
                codigo text)""")# Aqui tou representando que cada dado vai ser uma
                                # Tupla contendo (id,nome,codigo)
conexão.commit() # Aquela salvada básica
cursor.close()
conexão.close()

#------Criação do banco de dados Turmas --------
conexão = sqlite3.connect("Turmas.db")
cursor = conexão.cursor()
cursor.execute("""create table Turmas(
                id integer primary key autoincrement, 
                codigot text,
                periodo text,
                codigod text,
                cpfp text,
                cpfa text)""")# Aqui tou representando que cada dado vai ser uma
                              # Tupla contendo (id,codigot,periodo,codigod,cpfp,cpfa)
conexão.commit() # Aquela salvada básica
cursor.close()
conexão.close()
