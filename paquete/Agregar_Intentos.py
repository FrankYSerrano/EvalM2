# FUNCION QUE RECIBE LA LISTA DE VALORES ENTREGADOS Y LOS RECONSTRUYE EN UN STRING AGREGANDO
# EL SEPARADOR DE MILES (".") EN CASO DE SER NECESARIO

def agrega_intentos(param_intentos, param_valor):
    #Variable para almacenar la conversion de lista a String
    cadena_caracteres =""

    #ciclo que recorre la lista param_valor la cual siempre tiene 6 elementos
    for i in range(0, 6):
        #Concatenado de los elementos de la lista en un string
        cadena_caracteres = cadena_caracteres + str(param_valor[i])
    #Si los 1eros 3 digitos del string son mayores a cero entonces el numero es mayor a mil y requiere insertarle el .
    if int(cadena_caracteres[0:3]) > 0:
        cadena_caracteres = str(int(cadena_caracteres[0:3])) + "." + cadena_caracteres[3:6]
    else:
        #Si es menor a mil el string debe cambiar eliminandole los ceros de la parte delantera
        cadena_caracteres = str(int(cadena_caracteres[3:6]))
    param_intentos.append(cadena_caracteres)
#    print(param_intentos)
    return param_intentos, param_valor

if __name__ == "__main__":
    agrega_intentos([], [0,0,0,0,0,0])
    agrega_intentos(['4.000'], [0,0,0,0,0,0])
    agrega_intentos(['4.000'], [0,0,0,0,2,0])
    agrega_intentos(['4.000'], [0,0,0,3,0,0])
    agrega_intentos(['4.000'], [0,0,4,0,0,0])
    agrega_intentos(['4.000'], [0,5,0,0,0,0])
    agrega_intentos(['4.000'], [6,0,0,0,0,0])
    agrega_intentos(['4.000'], [1,2,3,4,5,6])
