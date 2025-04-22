print("╔═════════════════════════════════════════════════════════════╗") 
print("║                    VALIDACIÓN DE PRODUCTOS                  ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")
'''
nombre_producto = str(input("Ingresa el nombre del producto: "))
precio_unitario = float(input("Ingresa el precio del producto: "))
cantidad_productos = int(input("Ingresa la cantidad de productos: "))
#porcentaje_descuento = int(input("Ingresa el porcentaje de descuento a aplicar(0% - 100%): "))
'''

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
        
          


#Verificamos el descuento
while True:
    try:
        porcentaje_descuento = int(input("Ingresa el porcentaje de descuento a aplicar(0% - 100%): "))
        if porcentaje_descuento >=0 and porcentaje_descuento <=100:
            break
        else: 
            print("Ingrese un valor en el rango de 0 - 100")            
           
    except ValueError:
        print("ingresa un dato valido por favor")  
          
    
