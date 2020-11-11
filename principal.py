#script principal
import paquete as p

#INICIALIZACIONE DE VARIABLES

#VARIABLE QUE PERMITIRA CONTROLAR EL LOOP
intento = True
#VARIABLE DE TIPO LISTA QUE ALMACENARA EL VALOR DE CADA POSICION
valorL = [0, 0, 0, 0, 0, 0]

#VARIABLE QUE ALMACENARA LOS INTENTOS INGRESADOS POR EL USUARIO
intentos = []

#VARIABLE QUE SERVIRA PARA ALMACENAR LA CANTIDAD DE CADA UNIDAD DE DESCOMPOSICION
diccionario_unidades = {"centena_mil" : 0, "decena_mil" : 0, "unidad_mil" : 0, "centena" : 0, "decena" : 0, "unidad" : 0}

otro = ''

while intento:
    p.preguntar_numero(not intento, valorL)
#    print(intento)
#    print(valorL)
    p.agrega_intentos(intentos, valorL)
#    print(intentos)
#    print(valorL)
#    if not intento:
#        break
#    else:
    p.agrega_diccionario(valorL, diccionario_unidades)
        #Descomponer_En_Diccionario(valor, diccionario_unidades)    FERNANDO
        #Mostrar_Abaco(diccionario_unidades)    GUIDO
    print("abaco y diccionario")

    otro = input("Desea ingresar otro valor? S/N ")
    if otro.upper() == 'N':
        intento = False

print("Los ingresos fueron: " + str(intentos))
print("FIN")