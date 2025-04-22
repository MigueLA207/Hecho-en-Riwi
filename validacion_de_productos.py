print("╔═════════════════════════════════════════════════════════════╗") 
print("║                    VALIDACIÓN DE PRODUCTOS                  ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

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

        if precio_unitario >=0:
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
 



#Calculamos el total

print("\n╔═════════════════════════════════════════════════════════════╗") 
print("║                          FACTURA                            ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")


subtotal = cantidad_productos * precio_unitario

if porcentaje_descuento > 0:
    costo_total = subtotal * (1 - porcentaje_descuento/100)
else: 
    costo_total = subtotal

print(f"Nombre del producto: {nombre_producto}")
print(f"cantidad del producto: {cantidad_productos}")
print(f"total a pagar: {costo_total: .2f}")



    

          
    
