# 1. Averigue que características tienen los siguientes sistemas operativos:

# a. CP/M: Kernel monolítico, monousuario y monotarea.
# b. UNIX: Kernel monolítico, multiusuario y multitarea. Algunas nuevas versiones de UNIX usan Microkernel.
# c. Windows: Kernel híbrido (combina elementos de los kernels monolíticos y microkernel), multiusuario y multitarea.
# d. Linux: Kernel monolítico, multiusuario y multitarea.
# e. MacOS: Kernel híbrido (combina elementos de los kernels monolíticos y microkernel), multiusuario y multitarea.
# f. Android: Kernel monolítico, multiusuario y multitarea.

# 3. 
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(21))

def pares(ls):
    return [x for x in ls if x % 2 == 0]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pares(lista))

def cuadrados(ls):
    return [x ** 2 for x in ls]

print(cuadrados(lista))

# 4.
class Caja: 
    def __init__(self, valor = None):
        self.__contenido = None

    def agregarContenido(self, valor):
        self.__contenido = valor
    
    def verContenido(self):
        return self.__contenido
    
    def tipoContenido(self):
        if self.estaVacia():
            raise Exception("No se puede pedir el tipo a una caja vacia")
        return type(self.__contenido)
    
    def estaVacia(self):
        return self.__contenido == None
    
    def combinar(self, otraCaja):
        if self.estaVacia() or otraCaja.estaVacia():
            raise Exception("No se pueden combinar cajas vacias")
        if self.tipoContenido() != otraCaja.tipoContenido():
            raise Exception("No se pueden combinar cajas de distintos tipos")
        if self.tipoContenido() is str:
            return Caja(self.verContenido() + otraCaja.verContenido())
        if self.tipoContenido() is int:
            return Caja(self.verContenido() + otraCaja.verContenido())
        if self.tipoContenido() is bool:
            return Caja(self.verContenido() and otraCaja.verContenido())
        return Caja()

    def __str__(self):
        if self.estaVacia():
            return "Caja vacia"
        return "Caja(" +str(self.__contenido) + ")"

#caja1 = Caja("a")
#caja2 = Caja("d")
caja3 = Caja(3)
caja4 = Caja(6)
#cajaCombinada1 = caja1.combinar(caja2)
cajaCombinada2 = caja3.combinar(caja4)