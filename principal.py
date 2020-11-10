#script principal
import paquete as p

#INICIALIZACIONE DE VARIABLES

#VARIABLE QUE PERMITIRA CONTROLAR EL LOOP
intento = False
#VARIABLE DE TIPO LISTA QUE ALMACENARA EL VALOR DE CADA POSICION
valor = [0, 0, 0, 0, 0, 0]

#VARIABLE QUE ALMACENARA LOS INTENTOS INGRESADOS POR EL USUARIO
intentos = []

#VARIABLE QUE SERVIRA PARA ALMACENAR LA CANTIDAD DE CADA UNIDAD DE DESCOMPOSICION
diccionario_unidades = {"centena_mil" : 0, "decena_mil" : 0, "unidad_mil" : 0, "centena" : 0, "decena" : 0, "unidad" : 0}

while not intento:
    #Ingresa_Dato(intento, valor)
    if not intento:
        break
    else:
        #Descomponer_En_Diccionario(valor, diccionario_unidades)
        #Mostrar_Abaco(diccionario_unidades)
        #Agregar_Intentos(intentos, valor)

print("Los ingresos fueron: " + str(intentos))
print("FIN")