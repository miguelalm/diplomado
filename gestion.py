

def gestion_de_productos(data_ex):
    def agregar_producto():
        print("\n--- Agregar producto ---")
        try:
            codigo = int(input("Inserte valor numérico del código del producto "))
            if codigo in data_ex:
                print(f"Código {codigo} existe en inventario, si desea actualizarlo, utilice el módulo de Editar producto")
            else:
                nombre = str(input("Inserte nombre del producto "))
                precio = int(input("Inserte valor numérico del precio del producto "))
                disponible = int(input("Inserte valor numérico de la cantidad disponible del producto "))
                minimo = int(input("Inserte valor numérico del monto mínimo a disponer del producto "))
                valor_add = {"nombre": nombre,
                             "precio": precio,
                             "disponible": disponible,
                             "minimo": minimo
                             }
                data_ex[codigo] = valor_add
                print("\n--- Producto agregado ---")
        except:
            print("Ocurrió un error, intenta de nuevo") #todo: test para probar errores

    def editar_producto():
        print("\n--- Editar producto ---")
        try:
            codigo = int(input("Inserte valor numérico del código del producto "))
            if codigo in data_ex:
                nombre = str(input("Inserte nombre del producto "))
                precio = int(input("Inserte valor numérico del precio del producto "))
                disponible = int(input("Inserte valor numérico de la cantidad disponible del producto "))
                minimo = int(input("Inserte valor numérico del monto mínimo a disponer del producto "))
                valor_add = {"nombre": nombre,
                             "precio": precio,
                             "disponible": disponible,
                             "minimo": minimo
                             }
                data_ex[codigo] = valor_add
                print("\n--- Producto modificado ---")
            else:
                print("Producto no existe")

        except:
            print("\n--- Ocurrió un error, intenta de nuevo ---") #todo: test para probar errores

    def eliminar_producto():
        print("\n--- Eliminar producto ---")
        try:
            #numero = int(input("Inserte valor del número del producto "))
            codigo = int(input("Inserte valor numérico del código del producto "))
            if codigo in data_ex:
                del data_ex[codigo]
                print("Producto eliminado")
            else:
                print("Producto no existe")
        except:
            print("Ocurrió un error, intenta de nuevo") #todo: test para probar errores

    print("\n--- Gestión de Productos ---")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("0. Volver")
    seleccion = input("Selecciona una opción (0-3): ")

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

def registrar_venta(data_ex, ventas_registradas):
    print("\n--- Registrar Venta ---")

    while True:
        try:
            codigo = int(input("Ingrese el código del producto que desea vender: "))
            if codigo in data_ex:
                producto = data_ex[codigo]
                break
            else:
                print("Producto no existe, busque otro")
        except Exception as error:
            print(f"Problema al buscar producto: ", error)

    # Fecha de la venta
    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")

    # Cantidad a vender
    while True:
        try:
            unidades_vendidas = int(input("Ingrese cuántas unidades se venden: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    if unidades_vendidas <= 0:
        print("No se pueden vender 0 o menos unidades.")
        return
    if producto["disponible"] < unidades_vendidas:
        print(f"No hay suficiente stock. Stock disponible: {producto['disponible']}")
        return

    # Actualizar stock y ventas
    producto["disponible"] -= unidades_vendidas
    producto["ventas"] += unidades_vendidas
    print(f"Se vendieron {unidades_vendidas} unidades de '{producto['nombre']}'.")
    print(f"Stock restante: {producto['disponible']}")

    # Registrar esta venta en la lista global
    registro = {
        "fecha": fecha,
        "codigo": codigo,
        "unidades": unidades_vendidas
    }
    ventas_registradas.append(registro)