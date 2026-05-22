# Definição do Aluno
# Em Python usamos uma classe no lugar de struct
class Aluno:
    def __init__(self, matricula, nome, n1, n2, n3):
        self.matricula = matricula
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


# Definição do Nó (elemento)
class Elemento:
    def __init__(self, aluno):
        self.dados = aluno
        self.prox = None  # ponteiro para o próximo nó

# Definição da Lista
class Lista:
    def __init__(self):
        self.inicio = None  # lista começa vazia

    # Retorna o tamanho da lista
    def tamanho(self):
        cont = 0
        no = self.inicio
        while no is not None:
            cont += 1
            no = no.prox
        return cont

    # Insere no final da lista
    def insere_final(self, aluno):
        no = Elemento(aluno)

        if self.inicio is None:
            self.inicio = no
        else:
            aux = self.inicio
            while aux.prox is not None:
                aux = aux.prox
            aux.prox = no

    # Insere mantendo a lista ordenada pela matrícula
    def insere_ordenado(self, aluno):
        no = Elemento(aluno)

        ant = None
        atual = self.inicio

        while atual is not None and atual.dados.matricula < aluno.matricula:
            ant = atual
            atual = atual.prox

        if ant is None:
            no.prox = self.inicio
            self.inicio = no
        else:
            no.prox = atual
            ant.prox = no

    # Remove o último elemento
    def remove_final(self):
        if self.inicio is None:
            return False

        ant = None
        no = self.inicio

        while no.prox is not None:
            ant = no
            no = no.prox

        if ant is None:
            self.inicio = None
        else:
            ant.prox = None

        return True

    # Remove pelo número de matrícula
    def remove_meio(self, matricula):
        if self.inicio is None:
            return False

        ant = None
        no = self.inicio

        while no is not None and no.dados.matricula != matricula:
            ant = no
            no = no.prox

        if no is None:
            return False

        if ant is None:
            self.inicio = no.prox
        else:
            ant.prox = no.prox

        return True

    # Imprime todos os elementos
    def imprime(self):
        no = self.inicio
        while no is not None:
            print(f"Matrícula: {no.dados.matricula}")
            print(f"Nome: {no.dados.nome}")
            print(f"Notas: {no.dados.n1} {no.dados.n2} {no.dados.n3}")
            print("-------------------------")
            no = no.prox



# MAIN

alunos = [
    Aluno(2, "Andre",   9.5, 7.8, 8.5),
    Aluno(4, "Ricardo", 7.5, 8.7, 6.8),
    Aluno(1, "Bianca",  9.7, 6.7, 8.4),
    Aluno(3, "Ana",     5.7, 6.1, 7.4),
]

li = Lista()

print(f"Tamanho inicial: {li.tamanho()}")

for a in alunos:
    li.insere_final(a)

print("\nLista após inserção:")
li.imprime()
print(f"\nTamanho: {li.tamanho()}")

print("\nAntes da remoção da matrícula 1:")
li.imprime()
li.remove_meio(1)
print("\nApós a remoção da matrícula 1:")
li.imprime()

for i in range(4):
    li.remove_final()
    print("\nApós remoção:")
    li.imprime()
    print(f"Tamanho: {li.tamanho()}")

for a in alunos:
    li.insere_final(a)

print("\nLista final:")
li.imprime()

# Em Python não é necessário liberar memória manualmente!
