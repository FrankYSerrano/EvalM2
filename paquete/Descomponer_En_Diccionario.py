# FUNCION QUE RECIBE UNA LISTA Y LA TRASPASA A UNA VARIABLE DE TIPO DICCIONARIO

def agrega_diccionario(param_valor,diccionario):
    diccionario ["unidad"] = param_valor[5]
    diccionario ["decena"] = param_valor[4]
    diccionario ["centena"] = param_valor[3]
    diccionario ["unidad_mil"] = param_valor[2]
    diccionario ["decena_mil"] = param_valor[1]
    diccionario ["centena_mil"] = param_valor[0]
#    print(diccionario)
    return param_valor, diccionario

if __name__ == "__main__":
    agrega_diccionario([6, 5, 4, 3, 2, 1], {"centena_mil":0, "decena_mil":0, "unidad_mil":0, "centena":0, "decena":0, "unidad":0})

