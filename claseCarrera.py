

class Carrera:
    __codigo: str
    __nombre: str
    __nombreTitulo: str
    __duracion: str
    __titulo: str

    def __init__(self, codigo=None, nombre=None, nombreTitulo=None, duracion=None, titulo=None):
        self.__codigo= codigo
        self.__nombre = nombre
        self.__nombreTitulo = nombreTitulo
        self.__duracion = duracion
        self.__titulo = titulo

    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo

    def muestroDatos(self):
        print(f"{self.__nombre} - Duracion: {self.__duracion}")

    def __str__(self):
        return f"{self.__codigo} {self.__nombre} {self.__nombreTitulo} {self.__duracion} {self.__titulo}"