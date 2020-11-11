


def mostrar_abaco(abaco):
    cm = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',]
    dm = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',]
    m = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',]
    c = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',]
    d = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',]
    u = ['|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |','|    |',] 

    for i in range(0,abaco ["centena_mil"]): 
        cm [i] = 'XXXXX'

    for i in range(0,abaco ["decena_mil"]): 
        dm [i] = 'XXXXX'
    
    for i in range(0,abaco ["unidad_mil"]): 
        m [i] = 'XXXXX'

    for i in range(0,abaco ["centena"]): 
        c [i] = 'XXXXX'

    for i in range(0,abaco ["decena"]): 
         [i] = 'XXXXX'

    for i in range(0,abaco ["unidad"]): 
        p [i] = 'XXXXX'



   
    print()
    print()    
    print("                   ABACO")
    print()
    print()
    print()
    print("     +-------+         +-------+       +---------+       +-------+       +-------+         +------+")
    print(f"    | {cm[8]}   |    | {dm[8]}   |    |  {m[8]}    |   |  {c[8]}    |   |  {d[8]}    |    |  {u[8]}  |")
    print(f"    | {cm[7]}   |    | {dm[7]}   |    |  {m[7]}    |   |  {c[7]}    |   |  {d[7]}    |    |  {u[7]}  |")
    print(f"    | {cm[6]}   |    | {dm[6]}   |    |  {m[6]}    |   |  {c[6]}    |   |  {d[6]}    |    |  {u[6]}  |")
    print(f"    | {cm[5]}   |    | {dm[5]}   |    |  {m[5]}    |   |  {c[5]}    |   |  {d[5]}    |    |  {u[5]}  |")
    print(f"    | {cm[4]}   |    | {dm[4]}   |    |  {m[4]}    |   |  {c[4]}    |   |  {d[4]}    |    |  {u[4]}  |")
    print(f"    | {cm[3]}   |    | {dm[3]}   |    |  {m[3]}    |   |  {c[3]}    |   |  {d[3]}    |    |  {u[3]}  |")
    print(f"    | {cm[2]}   |    | {dm[2]}   |    |  {m[2]}    |   |  {c[2]}    |   |  {d[2]}    |    |  {u[2]}  |")
    print(f"    | {cm[1]}   |    | {dm[1]}   |    |  {m[1]}    |   |  {c[1]}    |   |  {d[1]}    |    |  {u[1]}  |")
    print(f"    | {cm[0]}   |    | {dm[0]}   |    |  {m[0]}    |   |  {c[0]}    |   |  {d[0]}    |    |  {u[0]}  |")
    print("      +------+        +------+         +------+         +------+          +------+         +------+")
    print("      100.000          10.000          1.000               100              10                1")




    
#def imprimir_x():
   # for palabra_clave == range(0,8):
     #   palabra_clave({"centena_mil" : ' ', "decena_mil" : ' ', "unidad_mil" : ' ', "centena" : ' ', "decena" : ' ', "unidad" : ' ',})
    #if 'unidad'  == rangue(0,8):
      #  print("XXXXX")

        

        


if __name__ == "__main__":
    mostrar_abaco({"centena_mil" : 7, "decena_mil" : 8, "unidad_mil" : 7, "centena" : 6, "decena" : 5, "unidad" : 4,})