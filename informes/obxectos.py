class Punto:
    """
    Clase que define a un punto en un plano de duas dimensions
    Exemplo de documentación segundo o PEP 257
    """

    def __init__(self, x=0, y=0):
        """
        Constructor que define las propiedades de x e y dun punto bidimensional.

        :param x: Coordenada x do punto
        :param y: Coordenada y do punto
        """
        self.x = x
        self.y = y


class Circulo(Punto):
    def __init__(self, x, y, r):
        Punto.__init__(self, x, y)
        self.r = r


class Punto2:
    """Clase que representa puntos no primeiro cuarante
    Implica que x>o e y>0
    """

    def __init__(self, x, y):
        """x e y estan ocultos"""
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        if x > 0:
            self.__x = x
        else:
            self.__x = 0
            print("Valor inicializado en 0")

    def setY(self, y):
        if y > 0:
            self.__y = y
        else:
            raise ValueError
            #self.__y = 0
            p#rint("Valor inicializado en 0")

    # Sirve para comparar este objeto con otro Ej p seria distinto a p2 poir que las coordenadas no son iguales
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    x = property (getX, setX)

    y = property (getY, setY)


p2 = Punto2(3, 5)
print(p2._Punto2__x)
# print(p2._Punto2__getY())

p = Punto(1, 3)
c = Circulo(2, 3, 6)
print(p.x)
print(c.x)
# Para asignarle valor a una variable privada/oculta
p2.__x = 10  # Esto no funciona
p2.x = 10  # Esto si

"""
Deriban de objet
__init__(self,args) Inicializa los valores
__new__(cls,args) Crea el objeto
__del__(self) Livera la memoria de ese objeto
__str__(self) Funciona como un toString
__eq__(self,outo) Para comparar objetos Hay que implementarlo
"""
print(p2.__eq__(p))
# print(p2==p)


#Excepciones
try:
    print(5/0)
except (ZeroDivisionError,SyntaxError):
    print("Erro: Non se pode hacer division por 0")
except ValueError:
    print("Erro: valor incorrecto")
else:
    print("A division realizouse")
finally:
    print("A division fixose ou non")




def unha_funcion(p1,p2):
    print(p1)
    print(p2)

unha_funcion("hola", 2.366)
unha_funcion(p2=2.366,p1="hola")
def unha_funcion2(p1="p1",p2=3.000):
    print(p1)
    print(p2)
unha_funcion2()
unha_funcion2(p1="KISKOS")

def suma(*n):
    suma= 0
    for numeros in n:
        suma =suma +numeros
    return suma
print(suma(1,2,3,4,5,6))
def suma2(n1,n2,**numeros):
    suma=n1+n2
    for n in numeros.items():
        suma=suma+n[1]
    return suma

print(suma2(1,2,numero3=3, numeros4=4))