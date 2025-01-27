#Crear una Clase Producto con los siguientes atributos:
# - código
# - nombre
# - precio 
#Crea su constructor, getter y setter y una función llamada calcular_total, donde le pasaremos unas unidades y nos debe calcular el precio final.
class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    def Calcular_Total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return 'codigo:' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)


class Pedido:


    def __init__(self, producto, Cantidades):
        self.producto = producto
        self.Cantidades = Cantidades

    def total_pedidos(self):
        total = 0

        for (p, c) in zip(self.__producto, self.__Cantidades):
            print('Producto-> ', p.nombre, ', Cantidad: '+ str(c))

    def mostrar_pedido(self):
        for (p, c) in zip(self.__producto, self.__Cantidades):
            total = total + p.calcular_total(c)


p1 = Producto(1, 'producto 1', 5)
p2 = Producto(2, 'producto 2', 15)
p3 = Producto(3, 'producto 3', 30)

print(p1)
print(p2)
print(p3)

print(p1.Calcular_Total(5))
print(p2.Calcular_Total(2))
print(p3.Calcular_Total(10))


producto = [p1, p2, p3]
cantidades = [5, 10, 2]

precio = Pedido(producto, cantidades)

print('Total peidos')