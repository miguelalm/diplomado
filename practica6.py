# ----------------------------------------------------
#  SISTEMA DE INVENTARIO CON REPORTES AVANZADOS
# ----------------------------------------------------

# Lista global para almacenar los productos
inventario = []

# Lista global para registrar cada venta con su fecha
ventas_registradas = []

# --------------------------
#      MENÚ PRINCIPAL
# --------------------------
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Gestión de Productos")
    print("2. Visualización del Inventario")
    print("3. Búsqueda de Productos")
    print("4. Control de Stock (umbral fijo = 1)")
    print("5. Generación de Reportes (submenú)")
    print("6. Registrar Venta")
    print("7. Salir")
    opcion = input("Selecciona una opción (1-7): ")
    return opcion

# --------------------------
#   GESTIÓN DE PRODUCTOS
# --------------------------
def gestionar_productos(inventario):
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            actualizar_producto(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def agregar_producto(inventario):
    print("\n--- Agregar Producto ---")
    codigo = input("Ingrese el código del producto: ")
    
    # Verificar que no exista otro producto con el mismo código
    for prod in inventario:
        if prod["codigo"].lower() == codigo.lower():
            print(f"Ya existe un producto con el código {codigo}.")
            return
    
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    
    # Crear el diccionario del producto
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "ventas": 0  # Se incrementa en registrar_venta
    }
    inventario.append(producto)
    
    print(f"Producto '{nombre}' agregado con éxito.")

def actualizar_producto(inventario):
    print("\n--- Actualizar Producto ---")
    codigo = input("Ingrese el código del producto que desea actualizar: ")
    
    for producto in inventario:
        if producto["codigo"].lower() == codigo.lower():
            print(f"Producto encontrado: {producto}")
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            
            print(f"Producto '{producto['nombre']}' actualizado correctamente.")
            return
    print("No se encontró ningún producto con ese código.")

def eliminar_producto(inventario):
    print("\n--- Eliminar Producto ---")
    codigo = input("Ingrese el código del producto que desea eliminar: ")
    
    for i, producto in enumerate(inventario):
        if producto["codigo"].lower() == codigo.lower():
            inventario.pop(i)
            print(f"Producto '{producto['nombre']}' eliminado correctamente.")
            return
    print("No se encontró ningún producto con ese código.")

# --------------------------
#   VISUALIZACIÓN INVENTARIO
# --------------------------
def visualizar_inventario(inventario):
    print("\n--- Inventario Actual ---")
    if len(inventario) == 0:
        print("No hay productos en el inventario.")
    else:
        for producto in inventario:
            print(f"Código: {producto['codigo']} | "
                  f"Nombre: {producto['nombre']} | "
                  f"Precio: {producto['precio']} | "
                  f"Cantidad: {producto['cantidad']} | "
                  f"Ventas: {producto['ventas']}")

# --------------------------
#    BÚSQUEDA DE PRODUCTOS
# --------------------------
def buscar_producto(inventario):
    print("\n--- Búsqueda de Productos ---")
    criterio = input("¿Deseas buscar por código (C) o por nombre (N)? ").strip().lower()
    
    if criterio == 'c':
        codigo = input("Ingresa el código del producto: ")
        for producto in inventario:
            if producto["codigo"].lower() == codigo.lower():
                print("Producto encontrado:")
                print(f"Código: {producto['codigo']}, "
                      f"Nombre: {producto['nombre']}, "
                      f"Precio: {producto['precio']}, "
                      f"Cantidad: {producto['cantidad']}, "
                      f"Ventas: {producto['ventas']}")
                return
        print("No se encontró ningún producto con ese código.")
    
    elif criterio == 'n':
        nombre = input("Ingresa el nombre del producto: ")
        for producto in inventario:
            if producto["nombre"].lower() == nombre.lower():
                print("Producto encontrado:")
                print(f"Código: {producto['codigo']}, "
                      f"Nombre: {producto['nombre']}, "
                      f"Precio: {producto['precio']}, "
                      f"Cantidad: {producto['cantidad']}, "
                      f"Ventas: {producto['ventas']}")
                return
        print("No se encontró ningún producto con ese nombre.")
    
    else:
        print("Opción de búsqueda no válida.")

# --------------------------
#     CONTROL DE STOCK
# --------------------------
def control_stock(inventario):
    """
    Muestra alerta de los productos con stock por debajo de 1 (umbral fijo).
    """
    print("\n--- Control de Stock ---")
    umbral = 1  
    alerta = False
    
    for producto in inventario:
        if producto["cantidad"] < umbral:
            print(f"¡ALERTA! El producto '{producto['nombre']}' "
                  f"(Código {producto['codigo']}) tiene stock bajo: {producto['cantidad']}")
            alerta = True
    
    if not alerta:
        print(f"No hay productos con stock menor a {umbral}.")

# --------------------------
#     REGISTRAR VENTA
# --------------------------
def registrar_venta(inventario, ventas_registradas):
    print("\n--- Registrar Venta ---")
    codigo = input("Ingrese el código del producto que desea vender: ")
    
    for producto in inventario:
        if producto["codigo"].lower() == codigo.lower():
            print(f"Producto encontrado: {producto}")
            
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
            
            if producto["cantidad"] < unidades_vendidas:
                print(f"No hay suficiente stock. Stock disponible: {producto['cantidad']}")
            else:
                # Actualizar stock y ventas
                producto["cantidad"] -= unidades_vendidas
                producto["ventas"] += unidades_vendidas
                print(f"Se vendieron {unidades_vendidas} unidades de '{producto['nombre']}'.")
                print(f"Stock restante: {producto['cantidad']}")

                # Registrar esta venta en la lista global
                registro = {
                    "fecha": fecha,
                    "codigo": codigo,
                    "unidades": unidades_vendidas
                }
                ventas_registradas.append(registro)
            return
    print("No se encontró ningún producto con ese código.")

# --------------------------
#  GENERACIÓN DE REPORTES
# --------------------------
def generar_reportes(inventario, ventas_registradas):
    while True:
        print("\n--- Menú de Reportes ---")
        print("1. Top X productos más vendidos (orden por 'ventas')")
        print("2. Productos con stock menor a un umbral (decidido por el usuario)")
        print("3. Venta por día (unidades vendidas en una fecha dada)")
        print("4. Venta promedio (promedio de unidades vendidas por día)")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            reporte_top_vendidos(inventario)
        elif opcion == "2":
            reporte_stock_bajo(inventario)
        elif opcion == "3":
            reporte_venta_diaria(ventas_registradas)
        elif opcion == "4":
            reporte_venta_promedio(ventas_registradas)
        elif opcion == "5":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# (1) TOP X PRODUCTOS MÁS VENDIDOS
def reporte_top_vendidos(inventario):
    """
    Ordena por 'ventas' (descendiente) y muestra los X primeros.
    NO muestra stock para evitar confusiones.
    """
    if len(inventario) == 0:
        print("No hay productos en el inventario. No se pueden generar reportes.")
        return
    
    try:
        x = int(input("¿Cuántos productos más vendidos deseas ver?: "))
        if x <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        # Ordenamos de mayor a menor según 'ventas'
        top_vendidos = sorted(inventario, key=lambda p: p["ventas"], reverse=True)
        
        print(f"\nLos {x} productos más vendidos (ordenados por 'ventas'):")
        for i, producto in enumerate(top_vendidos[:x], start=1):
            print(f"{i}. {producto['nombre']} (Código: {producto['codigo']}) "
                  f"- Ventas: {producto['ventas']}")
    except ValueError:
        print("Debes ingresar un número entero válido.")

# (2) PRODUCTOS CON STOCK BAJO (UMBRAL USUARIO)
def reporte_stock_bajo(inventario):
    if len(inventario) == 0:
        print("No hay productos en el inventario. No se pueden generar reportes.")
        return
    
    try:
        umbral = int(input("Ingresa el umbral de stock: "))
        print(f"\nProductos con stock menor a {umbral}:")
        bajos = [p for p in inventario if p["cantidad"] < umbral]
        if len(bajos) == 0:
            print(f"No hay productos con stock menor a {umbral}.")
        else:
            for producto in bajos:
                print(f"- {producto['nombre']} (Código {producto['codigo']}): "
                      f"{producto['cantidad']} unidades")
    except ValueError:
        print("Debes ingresar un número entero válido.")

# (3) VENTAS POR DÍA
def reporte_venta_diaria(ventas_registradas):
    if len(ventas_registradas) == 0:
        print("No hay registros de ventas.")
        return
    
    fecha_consulta = input("Ingrese la fecha a consultar (YYYY-MM-DD): ")
    total_vendido = 0
    for venta in ventas_registradas:
        if venta["fecha"] == fecha_consulta:
            total_vendido += venta["unidades"]
    
    print(f"En la fecha {fecha_consulta} se vendieron {total_vendido} unidades en total.")

# (4) VENTA PROMEDIO (promedio de unidades vendidas por día)
def reporte_venta_promedio(ventas_registradas):
    if len(ventas_registradas) == 0:
        print("No hay registros de ventas.")
        return
    
    # Obtenemos el set de fechas únicas
    dias_unicos = set(venta["fecha"] for venta in ventas_registradas)
    if len(dias_unicos) == 0:
        print("No se pudieron calcular estadísticas porque no hay fechas registradas.")
        return
    
    total_vendido = sum(venta["unidades"] for venta in ventas_registradas)
    promedio = total_vendido / len(dias_unicos)
    print(f"La venta promedio por día es de {promedio:.2f} unidades.")

# --------------------------
#       BUCLE PRINCIPAL
# --------------------------
if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            gestionar_productos(inventario)
        elif opcion == "2":
            visualizar_inventario(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            control_stock(inventario)
        elif opcion == "5":
            generar_reportes(inventario, ventas_registradas)
        elif opcion == "6":
            registrar_venta(inventario, ventas_registradas)
        elif opcion == "7":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")
