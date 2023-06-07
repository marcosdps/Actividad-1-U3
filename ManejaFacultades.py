from claseFacultad import Facultad
from claseCarrera import Carrera
import csv

class ManejaFacultades:

    def __init__(self):
        self.__listaFacultades = []


    def leoArchivo(self):
        with open("facultades.csv", "r", encoding="utf8")as archi:
            reader = csv.reader(archi, delimiter=",")
            j=-1
            for fila in reader:
                if fila[1].find("Facultad") != -1:
                    unaFacu = Facultad(*fila)
                    self.__listaFacultades.append(unaFacu)
                    j +=1
                else:
                    self.__listaFacultades[j].agregarCarrera(fila)
            for i in range(len(self.__listaFacultades)):
                print(self.__listaFacultades[i])
                self.__listaFacultades[i].mostrarCarreras()
    
    def muestroDatosFacu(self, cod):
        i=0
        while i < len(self.__listaFacultades) and self.__listaFacultades[i].getCodigo() != cod:
            i +=1
        if i < len(self.__listaFacultades):
            print(self.__listaFacultades[i].getNombre())
            self.__listaFacultades[i].mostrarNomYDuracion()

    def mostrarDatosCarrera(self, nombre):
        codigo = None
        i = -1
        while i < len(self.__listaFacultades) and codigo == None:
            codigo = self.__listaFacultades[i].buscoCarrera(nombre)
            i +=1
        if codigo != None:
            i -=1
            print(f"Codigo: {codigo} {self.__listaFacultades[i].getNombre()} con localidad en {self.__listaFacultades[i].getLocalidad()}")
