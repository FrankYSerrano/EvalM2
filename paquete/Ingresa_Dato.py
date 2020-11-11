def preguntar_numero(param_intento, param_valor):
    while not param_intento:
        valor = input("Ingrese un número entero: ")
        if valor.upper() == "SALIR":
            break 
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
                    # print(str(i))
                    # print(str( i-5 + len(valor)))
                        param_valor[i] = int(valor[i-6 + len(valor)])
                # print(param_valor)            
                        #  for i in range(0, len(valor)):
                    #  print(valor[i])
                    #  param_valor[i]=int(valor[i])
                    #param_intento=True
                # print(str(len(valor)))
            except ValueError:
                print("ATENCIÓN: Debe ingresar un cifra de valor  entero.")
  #  print(param_valor)        
 
if __name__ == "__main__":
    preguntar_numero(False,[0, 0, 0, 0, 0, 0])