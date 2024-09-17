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
            valor = int(input(f"Ingrese numero que corresponda:\n"))
            if valor==1:
                pass
            elif valor==2:
				pass
            elif valor==3:
                print("3. Salir")
                break
            else:
                print("Seleccione una opcion correcta")
			
            
	
	

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
