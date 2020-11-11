#script principal
import paquete as p

# ************************************ INICIALIZACIONE DE VARIABLES ***********************************

#VARIABLE QUE PERMITIRA CONTROLAR EL LOOP
#intento = False
intento = True

#VARIABLE DE TIPO LISTA QUE ALMACENARA EL VALOR DE CADA POSICION
valorL = [0, 0, 0, 0, 0, 0]

#VARIABLE QUE ALMACENARA LOS INTENTOS INGRESADOS POR EL USUARIO
intentos = []

#VARIABLE QUE SERVIRA PARA ALMACENAR LA CANTIDAD DE CADA UNIDAD DE DESCOMPOSICION
diccionario_unidades = {"centena_mil" : 0, "decena_mil" : 0, "unidad_mil" : 0, "centena" : 0, "decena" : 0, "unidad" : 0}

while intento:
#    print(valorL)
#    print("ID: " + str(id(intento)))
#    print("ID: " + str(id(valorL)))
#    intento = p.preguntar_numero(intento, valorL)
    intento, valorL = p.preguntar_numero(intento, valorL)
#    print("Variable BOOLEANA de control de ciclo principal al salir de Funcion " + str(intento))        
#    if not intento:
#        print("CHAO PESCAO!!!!")
#        break
    if intento:
        print(valorL)
        intentos, valorL = p.agrega_intentos(intentos, valorL)
    #    print(intentos)
    #    print(valorL)
        valorL, diccionario_unidades = p.agrega_diccionario(valorL, diccionario_unidades)
        diccionario_unidades = p.mostrar_abaco(diccionario_unidades)
    #    print("abaco")
    #    if p.salir() == False:
    #        break

print("Los ingresos fueron: " + str(intentos))
print("FIN")