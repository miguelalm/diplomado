

def gestion_de_productos(data_ex):
    def agregar_producto():
        print("Agregar producto")
        try:
            codigo = int(input("Inserte valor numérico del código del producto "))
            nombre = str(input("Inserte nombre del producto "))
            precio = int(input("Inserte valor numérico del precio del producto "))
            disponible = int(input("Inserte valor numérico de la cantidad disponible del producto "))
            minimo = int(input("Inserte valor numérico del monto mínimo a disponer del producto "))
            valor_add = {"nombre": nombre, "precio": precio, "disponible": disponible, "minimo": minimo}
            data_ex[codigo] = valor_add
            print("Producto agregado")
        except:
            print("Ocurrió un error, intenta de nuevo") #todo: test para probar errores

    def editar_producto():
        print("Editar producto")
        try:
            #numero = int(input("Inserte valor del número del producto "))
            codigo = int(input("Inserte valor numérico del código del producto "))
            nombre = str(input("Inserte nombre del producto "))
            precio = int(input("Inserte valor numérico del precio del producto "))
            disponible = int(input("Inserte valor numérico de la cantidad disponible del producto "))
            minimo = int(input("Inserte valor numérico del monto mínimo a disponer del producto "))
            valor_add = {"nombre": nombre, "precio": precio, "disponible": disponible, "minimo": minimo}
            data_ex[codigo] = valor_add
            print("Producto modificado")
        except:
            print("Ocurrió un error, intenta de nuevo") #todo: test para probar errores

    def eliminar_producto():
        print("Eliminar producto")
        try:
            #numero = int(input("Inserte valor del número del producto "))
            codigo = int(input("Inserte valor numérico del código del producto "))
            del data_ex[codigo]
            print("Producto eliminado")
        except:
            print("Ocurrió un error, intenta de nuevo") #todo: test para probar errores

    print("Gestión de productos, presione tecla para avanzar")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("0. Volver")
    seleccion = input("Escribe una opción: ")

    if seleccion == "1":
        agregar_producto()
    elif seleccion == "2":
        editar_producto()
    elif seleccion == "3":
        eliminar_producto()
    elif seleccion == "0":
        return
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")

    gestion_de_productos(data_ex)
