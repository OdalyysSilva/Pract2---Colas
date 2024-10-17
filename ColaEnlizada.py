class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad

    def imprimir_pedido(self):
        print(f"     Cliente: {self.cliente}")
        print(f"     Cantidad: {self.cantidad}")
        print("     ------------")

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_cliente(self):
        return self.cliente

class Nodo:
    def __init__(self, info=None, siguiente=None):
        self.info = info
        self.siguiente = siguiente

    def obtener_siguiente(self):
        return self.siguiente

    def establecer_siguiente(self, siguiente):
        self.siguiente = siguiente

class InterfazCola:
    def tamaño(self):
        pass

    def esta_vacia(self):
        pass

    def frente(self):
        pass

    def encolar(self, info):
        pass

    def desencolar(self):
        pass

    def imprimir_info(self):
        pass

    def obtener_n_elemento(self, pos):
        pass

class Cola(InterfazCola):
    def __init__(self):
        self.nodo_frente = None
        self.nodo_final = None
        self.contador = 0

    def tamaño(self):
        return self.contador

    def esta_vacia(self):
        return self.nodo_frente is None

    def frente(self):
        if self.esta_vacia():
            return None
        return self.nodo_frente.info

    def encolar(self, info):
        nuevo_nodo = Nodo(info)
        if self.esta_vacia():
            self.nodo_frente = self.nodo_final = nuevo_nodo
        else:
            self.nodo_final.establecer_siguiente(nuevo_nodo)
            self.nodo_final = nuevo_nodo
        self.contador += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        desencolado = self.nodo_frente.info
        self.nodo_frente = self.nodo_frente.obtener_siguiente()
        self.contador -= 1
        if self.esta_vacia():
            self.nodo_final = None
        return desencolado

    def imprimir_info(self):
        print("********* ESTADO DE LA COLA *********")
        print(f"   Tamaño: {self.tamaño()}")
        nodo = self.nodo_frente
        i = 1
        while nodo is not None:
            print(f"   ** Elemento {i}")
            nodo.info.imprimir_pedido()
            nodo = nodo.obtener_siguiente()
            i += 1
        print("*************************************")

    def obtener_n_elemento(self, pos):
        if pos < 1 or pos > self.tamaño():
            return None
        actual = self.nodo_frente
        for i in range(1, pos):
            actual = actual.obtener_siguiente()
        return actual.info

if __name__ == "__main__": # Clase PruebaCola para probar la cola
    pedido1 = Pedido(20, "cliente1") # Crear pedidos
    pedido2 = Pedido(30, "cliente2")
    pedido3 = Pedido(40, "cliente3")
    pedido4 = Pedido(50, "cliente4")

    cola = Cola() # Crear cola

    cola.encolar(pedido1) # Añadir pedidos a la cola
    cola.encolar(pedido2)
    cola.encolar(pedido3)
    cola.encolar(pedido4)

    cola.imprimir_info() # Imprimir la información de la cola

    print("\nPrimer elemento en la cola:") # Mostrar el primer elemento sin quitarlo
    primer_pedido = cola.frente()
    if primer_pedido:
        primer_pedido.imprimir_pedido()

    print("\nDesencolando el primer elemento:") # Quitar el primer elemento de la cola
    pedido_desencolado = cola.desencolar()
    if pedido_desencolado:
        pedido_desencolado.imprimir_pedido()

    cola.imprimir_info() # Imprimir la cola después de eliminar un elemento

    print("\nTercer elemento en la cola:") # Obtener el tercer elemento sin eliminarlo
    tercer_pedido = cola.obtener_n_elemento(3)
    if tercer_pedido:
        tercer_pedido.imprimir_pedido()
