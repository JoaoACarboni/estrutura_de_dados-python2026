from collections import deque
# Collections é uma biblioteca padrão do Python que oferece estruturas de dados adicionais, como deque (double-ended queue), que é ideal para implementar filas.

# Criando a fila
fila = deque()

# Enfileirar (entra pelo fim)
fila.append("Andre")
fila.append("Ricardo")
fila.append("Bianca")
fila.append("Ana")

print("Fila:", list(fila))
print("Tamanho:", len(fila))

# Ver o primeiro sem remover
print("Primeiro:", fila[0])

# Desenfileirar (sai pelo início)
saiu = fila.popleft()
print(f"{saiu} saiu da fila")

print("Fila após remoção:", list(fila))