def preguntar_numero(param_intento, param_valor):
    control = True
    while control:
        valor = input("Ingrese un número entero: ")
        if valor.upper() == "SALIR":
            param_intento=True
            control = False
#            break 
        else:   
            try:
                valorentero=int(valor)
                if valorentero > 999999:
                    print(" el numero se pasa de los parametros")
                else:  
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
                    for i in range(5, 5-len(valor), -1):
                        param_valor[i] = int(valor[i-6 + len(valor)])
                    control=False
            except ValueError:
                print("ATENCIÓN: Debe ingresar un cifra de valor  entero.")
#    print("Lista al  salir de Funcion " + str(param_valor))   
    print("Variable BOOLEANA de control de ciclo principal al salir de Funcion " + str(param_intento))        
 
if __name__ == "__main__":
    preguntar_numero(False,[0, 0, 0, 0, 0, 0])