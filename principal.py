#script principal
import paquete as p

# ************************************ INICIALIZACIONE DE VARIABLES ***********************************

#VARIABLE QUE PERMITIRA CONTROLAR EL LOOP
intento = False
#VARIABLE DE TIPO LISTA QUE ALMACENARA EL VALOR DE CADA POSICION
valorL = [0, 0, 0, 0, 0, 0]

#VARIABLE QUE ALMACENARA LOS INTENTOS INGRESADOS POR EL USUARIO
intentos = []

#VARIABLE QUE SERVIRA PARA ALMACENAR LA CANTIDAD DE CADA UNIDAD DE DESCOMPOSICION
diccionario_unidades = {"centena_mil" : 0, "decena_mil" : 0, "unidad_mil" : 0, "centena" : 0, "decena" : 0, "unidad" : 0}

otro = ''

while not intento:
    p.preguntar_numero(intento, valorL)
    print("Variable BOOLEANA de control de ciclo principal al salir de Funcion " + str(intento))        
    if intento:
#        print("CHAO PESCAO!!!!")
        break
    print(valorL)
    p.agrega_intentos(intentos, valorL)
#    print(intentos)
#    print(valorL)
    p.agrega_diccionario(valorL, diccionario_unidades)
#    Mostrar_Abaco(diccionario_unidades)    GUIDO
    print("abaco")

print("Los ingresos fueron: " + str(intentos))
print("FIN")