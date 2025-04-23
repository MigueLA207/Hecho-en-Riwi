#Verificar si un número está en una lista
'''
lista = [1,2,3,4,5]

num= int(input("Escriba el valor de un numero: "))

if num in lista:
    print("El numero esta en la lista")
else:
    print("El numero no se encuentra ne la lista")
    '''
productos = [["Arroz",2000,3,10],["huevo",700,5,5]]
total = 0

for valor in productos:
    subtotal = 0
    descuento = 0
    print(valor[0],valor[1],valor[2])
    
    subtotal = (subtotal + (valor[1]*valor[2]))
    descuento = subtotal * (valor[3]/100)
    total = subtotal-descuento
    

print(total)


