print("╔═════════════════════════════════════════════════════════════╗") 
print("║                    VALIDACIÓN DE PRODUCTOS                  ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")


productos = []


while True:

    porcentaje_descuento=0
    #Verificamos el nombre del producto
    while True:
        try:
            nombre_producto = str(input("Ingresa el nombre del producto: "))

            if nombre_producto.isalpha():
                break
            else: 
                print("Ingrese un nombre valido")            
            
        except ValueError:
            print("ingresa un dato valido por favor")


    #Verificamos el precio_unitario
    while True:
        try:
            precio_unitario = float(input("Ingresa el precio del producto: "))

            if precio_unitario > 0:
                break
            else: 
                print("Ingrese un valor positivo")            
            
        except ValueError:
            print("ingresa un dato valido por favor")


    #Verificamos el precio_unitario
    while True:
        try:
            cantidad_productos = int(input("Ingresa la cantidad de productos: "))
            if cantidad_productos >= 0:
                break
            else: 
                print("Ingrese un valor positivo")            
            
        except ValueError:
            print("ingresa un dato valido por favor")
            


    #Verificamos que el porcentaje sea valido
    while True:
        try:
            porcentaje_descuento = int(input("Ingresa el porcentaje de descuento a aplicar(0% - 100%): "))
            if porcentaje_descuento >=1 and porcentaje_descuento <=100 or porcentaje_descuento == 0:
                break 
            else: 
                print("Ingrese un valor en el rango de 0 - 100")            
            
        except ValueError:
            print("ingresa un dato valido por favor")  
    
    #Lo agrega como tupla
    productos.append((nombre_producto,precio_unitario,cantidad_productos))


    seguir = int(input("\nDigite 1 si quiere agregar mas nombres, digite 2 si quiere salir del programa:  "))
    if seguir == 2:
        break

#Verificamos que el porcentaje sea valido
    while True:
        try:
            porcentaje_descuento = int(input("Ingresa el porcentaje de descuento a aplicar(0% - 100%): "))
            if porcentaje_descuento >=1 and porcentaje_descuento <=100 or porcentaje_descuento == 0:
                break 
            else: 
                print("Ingrese un valor en el rango de 0 - 100")            
            
        except ValueError:
            print("ingresa un dato valido por favor")

total = 0
for valor in productos:
    print(valor[0],valor[1],valor[2])


    
