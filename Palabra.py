from collections import deque

# Definir la lista como una deque (doble cola)
lista = deque()

# Añadir elementos a la lista
lista.append("Palabra")
lista.append(5)
lista.append(17)
lista.append("Palabra 2")

# Eliminar el último elemento
lista.pop()

# Mostrar el tamaño de la lista
print("El tamaño de la lista es:", len(lista))

# Mostrar el último elemento de la lista
print(lista[-1])
