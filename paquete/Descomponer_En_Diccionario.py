
# FUNCION QUE RECIBE UNA LISTA Y LA TRASPASA A UNA VARIABLE DE TIPO DICCIONARIO
def agrega_diccionario(param_valor,diccionario):#Aquí ingresa una lista y un diccionario.
    diccionario ["unidad"] = param_valor[5]     #La lista previamente ingresada se descompone y se guarda en el diccionario 
    diccionario ["decena"] = param_valor[4]
    diccionario ["centena"] = param_valor[3]
    diccionario ["unidad_mil"] = param_valor[2]
    diccionario ["decena_mil"] = param_valor[1]
    diccionario ["centena_mil"] = param_valor[0]
    return param_valor, diccionario # La funcion retorna la lista dentro del diccionario

if __name__ == "__main__":#Para ejecutar pruebas
    agrega_diccionario([6, 5, 4, 3, 2, 1], {"centena_mil":0, "decena_mil":0, "unidad_mil":0, "centena":0, "decena":0, "unidad":0})

