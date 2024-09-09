#desarrollar una funcion que solicite la carga del dia, mes y año y
#almacene dichos datos a una tupla que luego debe retornar.
#la segunda funcion a implementar debe recibir una tupla
#con la fecha y mostrarla por pantalla.
def cargar_fecha():
    dd=int(input("Ingrese número de día:"))
    mm=int(input("Ingrese número de mes:"))
    aa=int(input("Ingrese número de año:"))
    return (dd,mm,aa)


def imprimir_fecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

#bloque principal
fecha=cargar_fecha()
imprimir_fecha(fecha)
