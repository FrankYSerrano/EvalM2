 #funcion que valida el dato ingresado en el menu principal:validacion de ingreso o sale del programa, 
 # velidacion de numero que no se ingrese palabras y validacion de numero entero.

def preguntar_numero(param_intento, param_valor): 
       while not param_intento: # loop que valida si sigue o sale del programa
        valor = input("Ingrese un número entero: ")  
        if valor.upper() == "SALIR":                 #valida que lo ingresado es numero y no letra
            break                                   
        else:   
            try:
                valorentero=int(valor)                #validador que lo ingresado es un numero entero
                if valorentero > 999999:
                    print(" el numero se pasa de los parametros") # restringido para que se ingresen cifras menores que 
                else:                                             # 999.999
                    if valorentero < 99999:
                        param_valor[0]=0
                    if valorentero < 9999:
                        param_valor[1]=0
                    if valorentero < 999:
                        param_valor[2]=0
                    if valorentero < 99:
                        param_valor[3]=0    
                    if valorentero < 9:
                        param_valor[4]=0    

                    for i in range(5, 5-len(valor), -1):               # funcion que sirve para recorrer la lista y           
                        param_valor[i] = int(valor[i-6 + len(valor)])  # dejarala en orden ademas de colocar cero en el inicio de la cifra 
            except ValueError:                                         # para lograr las cantidades de fichas              
                print("ATENCIÓN: Debe ingresar un cifra de valor  entero.")
  #  print(param_valor)        
if __name__ == "__main__":
    preguntar_numero(False,[0, 0, 0, 0, 0, 0])
    