from collections import deque

lista = deque() # Definir la lista como una deque (doble cola)

# Añadir elementos a la lista
lista.append("Palabra")
print(lista)
lista.append(5)
print(lista)
lista.append(17)
print(lista)
lista.append("Palabra 2")
print(lista)
print("El tamaño de la lista es:", len(lista))

lista.pop() # Eliminar el último elemento

print("El tamaño de la lista al eliminar el ultimo elemento:", len(lista)) # Mostrar el tamaño de la lista

print(lista[-1]) # Mostrar el último elemento de la lista
