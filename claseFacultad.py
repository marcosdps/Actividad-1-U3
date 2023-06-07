from claseCarrera import Carrera


class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __provincia: str
    __telefono: str
    __Carrera: list

    def __init__(self, codigo=None, nombre=None, direccion=None, localidad=None, provincia=None, telefono=None):
        self.__codigo = int(codigo)
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__provincia = provincia
        self.__telefono = telefono
        self.__Carrera = []

    def agregarCarrera(self,fila):
        self.__Carrera.append(Carrera(*fila))

    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def tamaño(self):
        return len(self.__Carrera)
    
    def getLocalidad(self):
        return self.__localidad

    def mostrarCarreras(self):
        for i in range(len(self.__Carrera)):
            print(self.__Carrera[i])

    def mostrarNomYDuracion(self):
        for i in range(len(self.__Carrera)):
            self.__Carrera[i].muestroDatos()
    
    def buscoCarrera(self, nombre):
        i =0
        codigo = None
        while i < len(self.__Carrera) and self.__Carrera[i].getNombre() != nombre:
            i +=1
        if i<len(self.__Carrera):
            codigo = self.__Carrera[i].getCodigo()
        return codigo
        

    def __str__(self):
        return f"{self.__codigo} {self.__nombre} {self.__direccion} {self.__localidad} {self.__provincia} {self.__telefono} "


