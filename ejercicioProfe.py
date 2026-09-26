#Ingresar datos de producto: nombre, categoria, precio
#Cada producto debe ser una lista
#Debe haber una lista superior madre de todos los productos
#Debo poder visualizar todos los productos (Que queden numerados)
#Debo poder buscar productos por su nombre
#Si no encontro, informar que no hay nada
#Eliminar un producto por posicion en la lista

stock = [["Arroz","Almacen","1652"],["Cacao","Almacen","8956"],["Alfajor","Golosinas","100"]]

print("Bienvenido a mi sistema de gestion")
opcion = ""

while opcion != "5":
    print("-------------------")
    print("1. Añadir producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Que queres hacer? 1/2/3/4/5: ").strip()
    
    match opcion:
        case "1":
            print("-------------------")
            print("Agregar")
            print("-------------------")
            
            nombre = input("Nombre del producto: ")
            categoria = input("Categoria del producto: ")
            precio = input("Precio del producto: $")
            
            stock.append([nombre, categoria, precio])

            print("Producto agregado!")
            
        case "2":
            print("-------------------")
            print("Visualizar")
            print("-------------------")
            contador = 1
            for producto in stock:
                print("---------")
                print(f"Numero: {contador}")
                print("Producto:", producto[0])
                print("Categoria:", producto[1])
                print(f"${producto[2]}")
                print("---------")
                print("")
                contador = contador + 1
            
        case "3":
            print("-------------------")
            print("Buscar")
            print("-------------------")
            
            busqueda = input("Que producto buscas?: ").strip().title()
            encontrado = False
            
            for producto in stock:
                if busqueda == producto[0]:
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("---------")
                    print("")

            if encontrado == False:
                print("Producto no encontrado")  
            
        case "4":
            print("-------------------")
            print("Eliminar")
            print("-------------------")
            
            #Pedir que quiere Eliminar
            productoAEliminar= input("Que producto queres eliminar?: ")
            encontrado = False
            
            for producto in stock:
                if productoAEliminar == producto[0]:
                    encontrado = True
                    print("---------")
                    print("Producto encontrado!")
                    print("Producto:", producto[0])
                    print("Categoria:", producto[1])
                    print("Precio: $", producto[2])
                    print("---------")
                    print("")
                    
                    decision = input(f"Estas seguro de querer eliminar {producto[0]} Si/No: ")
                    if decision == "Si":
                        stock.remove(producto)
                        print("Listo! Producto eliminado")

                
            if encontrado == False:
                print("El producto que buscas eliminar, ya no existe")  
            
            
        case "5":
            print("-------------------")
            print("Gracias por usar mi sistema")
            print("-------------------")
        case _:
            print("-------------------")
            print("Opcion no valida")
            print("-------------------")
