#En el bloque principal del programa definir un diccionario que almacene
#los nombres de paises como clave y como valor la cantidad de habitantes.
#implementar una funcion para mostrar cada clave y valor.
def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])

#bloque principal

paises={"Argentina ":400000000, "España ":460000000, "Brasil ":190000000, "Uruguay": 3400000}
imprimir(paises)
