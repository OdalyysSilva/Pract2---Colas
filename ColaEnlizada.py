class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ColaEnlazada:
    def __init__(self):
        self.front = None  # Primer nodo de la cola
        self.rear = None   # Último nodo de la cola
        self.size = 0      # Tamaño de la cola

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def frente(self):
        if self.is_empty():
            return None
        return self.front.data

    def encolar(self, info):
        nuevo_nodo = Nodo(info)  # Crear un nuevo nodo con la información
        if self.is_empty():
            self.front = nuevo_nodo  # Si la cola está vacía, el nuevo nodo es el frente
        else:
            self.rear.next = nuevo_nodo  # Conectar el último nodo con el nuevo nodo
        self.rear = nuevo_nodo  # Actualizar el último nodo
        self.size += 1

    def desencolar(self):
        if self.is_empty():
            return None
        data = self.front.data  # Obtener la información del frente
        self.front = self.front.next  # Mover el frente al siguiente nodo
        self.size -= 1
        if self.is_empty():
            self.rear = None  # Si la cola queda vacía, rear también se pone en None
        return data

class Orden:
    def __init__(self, qtty, cliente):
        self.cliente = cliente
        self.qtty = qtty

    def imprimir(self):
        print(f"     Cliente: {self.cliente}")
        print(f"     Cantidad: {self.qtty}")
        print("     ------------")

    def obtener_cliente(self):
        return self.cliente

    def obtener_cantidad(self):
        return self.qtty

if __name__ == "__main__":
    cola = ColaEnlazada()

    # Agregar algunas órdenes a la cola
    cola.encolar(Orden(5, "Alice"))
    cola.encolar(Orden(3, "Bob"))
    cola.encolar(Orden(10, "Charlie"))

    # Imprimir todas las órdenes en la cola usando un bucle while
    nodo_actual = cola.front  # Iniciar desde el frente de la cola
    while nodo_actual is not None:
        orden = nodo_actual.data  # Obtener la información del nodo
        orden.imprimir()  # Llamar al método imprimir() de Orden
        nodo_actual = nodo_actual.next  # Moverse al siguiente nodo
