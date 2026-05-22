#------------------------------
# EXEMPLO DE COMO O PYTHON É SIMPLES
#------------------------------

# Criar
alunos = []

# Inserir no final
alunos.append(Aluno(2, "Andre", 9.5, 7.8, 8.5))

# Inserir em posição específica
alunos.insert(0, Aluno(1, "Bianca", 9.7, 6.7, 8.4))

# Remover o último
alunos.pop()

# Remover por índice
alunos.pop(0)

# Tamanho
len(alunos)

# Imprimir
for a in alunos:
    print(a.nome)

