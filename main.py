from ManejaFacultades import ManejaFacultades
import os

if __name__ == "__main__":
    mFacultades = ManejaFacultades()
    mFacultades.leoArchivo()

    print("""\n---------MENU DE OPCIONES---------
    -1- Punto 1
    -2- Punto 2
    -3- 
    -0- SALIR""")
    opcion = int(input("Ingrese una opcion: "))
    while opcion != 0:
        match opcion:
            case 1:
                cod = int(input("Ingrese un codigo de facultad: "))
                os.system("cls")
                mFacultades.muestroDatosFacu(cod)
            case 2:
                nombre = input("Ingrese el nombre de una carrera: ")
                mFacultades.mostrarDatosCarrera(nombre)
        print("""\n---------MENU DE OPCIONES---------
    -1- Punto 1
    -2- Punto 2
    -3- 
    -0- SALIR""")
        opcion = int(input("Ingrese una opcion: "))
