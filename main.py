# comment
def agregar_producto(inventario):
    nombre = input(f"Ingrese el nombre del producto:\n").lower().strip()
    categoria = input("Ingrese la categoria del producto:\n").lower().strip()
    cantidad = int(input("Ingrese la cantidad del producto:\n"))
    precio = int(input("Ingrese el precio del producto:\n"))
	
    inventario[nombre] = (categoria, cantidad, precio)
	
def buscar_productos(inventario):
    while True:
        print("Favor seleccionar que opcion desea buscar N° 1 Nombre, N°2 Categoria o N°3 Salir")
        valor = int(input("Ingrese numero que corresponda:\n"))
        if valor==1:
            nombre_producto = input("Indique el nombre del producto que va a buscar: ")
            if nombre_producto in inventario.keys():
                print(f"El producto {nombre_producto} pertenece a la categoria de {inventario[nombre_producto][0]}, su cantidad actual es de {inventario[nombre_producto][1]} y su precio es de {inventario[nombre_producto][2]}")
            else:
                print("El producto no existe en el inventario")
                
        #----> BUSQUEDA POR CATEGORIA <----
        elif valor==2:
            categoria = input ("Ingrese la categoria del Producto").strip().lower()
            auxiliar = 0 #contador para verificar si existen productos con esa categoría
            
            for producto, detalle in inventario.items():
                if detalle[0] == categoria:
                    auxiliar += 1
                    print(f"El producto {producto}, su cantidad actual es de {inventario[producto][1]} y su precio es de {inventario[producto][2]}")
            if auxiliar == 0:
                print (" no hay nada de esa categoria ")
                
        elif valor==3:
            print("3. Salir")
            break
        else:
            print("Seleccione una opcion correcta")

# NUNCA MAS 


inventario={}
while True:
	print("Bienvenidos al aCuenta :V")
	print("1. Agregar Producto")
	print("2. Buscar Producto")
	print("3. Actualizar Inventario")
	print("4. Eliminar Producto")
	print("5. Mostrar Inventario")
	print("6. Salir")
	print("------------")
	opcion=input("Ingrese su opción: ")

	if opcion=="1":
		producto=input("Ingrese el producto: ")
	elif opcion=="2":
		pass
	elif opcion=="3":
		pass
	elif opcion=="4":
		pass
	elif opcion=="5":
		pass
	elif opcion=="6":
		break
	else:
		print("Error capa 8")
