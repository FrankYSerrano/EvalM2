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

#CICLO PARA INGRESAR VALORES VALIDOS (SOLO NUMEROS!) o SALIR
while intento:
    #LLAMADO A FUNCION QUE SOLICITA IMPUT AL USUARIO
    intento, valorL = p.preguntar_numero(intento, valorL)
    #SI EL USUARIO INTRODUJO SALIR intento SERA FALSE DE LO CONTRARIO PROSIGUE A DIBUJAR EL ABACO Y REPREGUNTAR
    if intento:
        #FUNCION QUE REGISTRA EN LISTA DE POSIBLES VALORES EL VALOR INGRESADO
        intentos, valorL = p.agrega_intentos(intentos, valorL)
        #FUNCION QUE LLENA EL DICCIONARIO CON LOS VALORES INGRESADOS
        valorL, diccionario_unidades = p.agrega_diccionario(valorL, diccionario_unidades)
        #FUNCION QUE DIBUJA EL ABACO
        diccionario_unidades = p.mostrar_abaco(diccionario_unidades)

print("Los ingresos fueron: " + str(intentos))
print("FIN")