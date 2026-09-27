#Ingresar datos de producto: nombre, categoria, precio
#Cada producto debe ser una lista
#Debe haber una lista superior madre de todos los productos
#Debo poder visualizar todos los productos (Que queden numerados)
#Debo poder buscar productos por su nombre
#Si no encontro, informar que no hay nada
#Eliminar un producto por posistema desicion en la lista

stock = [["atun","almacen","2700"],["fideos","almacen","3500"],["yogurt","lacteos","2500"] ]

print("Bienvenido a mi sistema de stock: ")
opcion = ""


while opcion != "5":

    print("_________________________________")
    print("1. Añadir producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Seleccione una opción: ").strip()

    match opcion:
        case "1":
            print("_________________________________")
            print("Agregar Nuevo producto")
            print("_________________________________")

            nombre = input("Nombre del producto: ")
            categoria = input("Categoria del producto: ")
            precio = input("Precio del producto: $")

            print(stock.append([nombre, categoria, precio]))
            print("")
            print("Producto agregado exitosamente")
            
            
        case "2":
            print("_________________________________")
            print("Visualizar productos")
            print("_________________________________")
            contador = 1

            for producto in stock:
                print("_________________________________")
                print(f"Numero: {contador}")
                print("Producto:", producto[0])
                print("Categoria:", producto[1])
                print("Precio: $", producto[2])
                print("")
                contador = contador + 1
        case "3":
            print("_________________________________")
            print("buscar un producto")
            print("_________________________________")

            busqueda = input("Que producto buscas?: ").strip()#.title()
            encontrado = False
            print(busqueda)
            for producto in stock:
                
                if busqueda == producto[0]:
                    encontrado = True
                    print("_________________________________")
                    print("Producto encontrado")
                    print("_________________________________")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("")
        case "4":
            print("_________________________________")
            print("Eliminar producto")
            print("_________________________________")

            productoParaEliminar = input("Que producto queres eliminar?: ").strip()#.title()
            encontrado = False

            for producto in stock:
                if productoParaEliminar == producto[0]:
                    encontrado = True
                    print("_________________________________")
                    print("Producto encontrado")
                    print("_________________________________")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("")


                    desicion = input(f"deseas eliminar el {producto[0]}? (si/no): ").strip().lower()
                    if desicion =="si":
                        stock.remove(producto)
                        print("El producto fue eliminado exitosamente")

            if encontrado == False:   
                print("El producto no se encuentra o ya fue eliminado.")         
        case "5":
            print("_________________________________")
            print("Gracias por usar el sistema de stock")
            print("_________________________________")
        case _:
            print("_________________________________")
            print("Opción no válida")
            print("_________________________________")