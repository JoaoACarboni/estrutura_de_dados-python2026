# Definição do Aluno
class Aluno:
    def __init__(self, matricula, nome, n1, n2, n3):
        self.matricula = matricula
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        #OBS: self será preenchido pelo objeto que chamou o método

# Definição do Nó
# Cada nó guarda um aluno e aponta para o próximo
class No:
    def __init__(self, aluno):
        self.dados = aluno
        self.prox = None  # começa sem apontar para ninguém
        # OBS: None é o equivalente a null

# Definição da Fila
# A fila segue a regra FIFO:
# First In, First Out -- Primeiro a entrar, primeiro a sair
class Fila:
    def __init__(self):
        self.inicio = None  # frente da fila (quem sai)
        self.fim = None     # fundo da fila (quem entrou por último)

    # Verifica se está vazia
    def esta_vazia(self):
        return self.inicio is None

    # Enfileirar (entrar na fila)

    # O novo elemento sempre entra pelo fim
    def enfileirar(self, aluno):
        no = No(aluno)  # cria o novo nó

        if self.esta_vazia():
            # se a fila estava vazia, início e fim são o mesmo nó
            self.inicio = no
            self.fim = no
        else:
            # o último nó aponta para o novo
            self.fim.prox = no
            # o fim agora é o novo nó
            self.fim = no

        print(f"→ {aluno.nome} entrou na fila.")

    # Desenfileirar (sair da fila)
    # O elemento que sai é sempre o do início
    def desenfileirar(self):
        if self.esta_vazia():
            print("Fila vazia! Ninguém para remover.")
            return None

        # guarda quem vai sair
        removido = self.inicio.dados

        # o próximo vira o novo início
        self.inicio = self.inicio.prox

        # se a fila ficou vazia, o fim também é None
        if self.inicio is None:
            self.fim = None

        print(f"← {removido.nome} saiu da fila.")
        return removido

    # Espiar o primeiro (sem remover)
    # Mostra quem está na frente sem tirá-lo da fila
    def primeiro(self):
        if self.esta_vazia():
            print("Fila vazia!")
            return None
        return self.inicio.dados

    # Tamanho da fila
    def tamanho(self):
        cont = 0
        no = self.inicio
        while no is not None:
            cont += 1
            no = no.prox
        return cont

    # Imprime a fila
    # Mostra do início até o fim
    def imprime(self):
        if self.esta_vazia():
            print("Fila vazia!")
            return

        print("\nEstado da Fila (início - fim)")
        no = self.inicio
        while no is not None:
            print(f"  Matrícula: {no.dados.matricula} | Nome: {no.dados.nome} | "
                  f"Notas: {no.dados.n1} {no.dados.n2} {no.dados.n3}")
            no = no.prox
        print("--------------------------------------")


# MAIN

alunos = [
    Aluno(2, "Andre",   9.5, 7.8, 8.5),
    Aluno(4, "Ricardo", 7.5, 8.7, 6.8),
    Aluno(1, "Bianca",  9.7, 6.7, 8.4),
    Aluno(3, "Ana",     5.7, 6.1, 7.4),
]

fila = Fila()

print("=== Tamanho inicial:", fila.tamanho(), "===\n")

# Todos entram pela ordem da lista (pelo fim da fila)
print("=== Alunos entrando na fila ===")
for a in alunos:
    fila.enfileirar(a)

fila.imprime()
print("Tamanho:", fila.tamanho())

# Quem está na frente?
frente = fila.primeiro()
print(f"\nPrimeiro da fila (sem remover): {frente.nome}")

# Removendo um por um — sai sempre do início
print("\n=== Alunos saindo da fila (FIFO) ===")
while not fila.esta_vazia():
    fila.desenfileirar()
    fila.imprime()
    print("Tamanho:", fila.tamanho())