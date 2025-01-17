def reporte_top_vendidos(inventario):
   if len(inventario) == 0:
        print("No hay productos en el inventario. No se pueden generar reportes.")
        return

   try:
        x = int(input("¿Cuántos productos más vendidos deseas ver?: "))
        if x <= 0:
            print("La cantidad debe ser un número positivo.")
            return

        # Ordenamos de mayor a menor según 'ventas'
        top_vendidos = dict(sorted(inventario.items(), key=lambda item: item[1]["ventas"], reverse=True))

        print(f"\nLos {x} productos más vendidos (ordenados por 'ventas'):")
        for codigo, producto in top_vendidos.items():
            print(f"{producto['nombre']} (Código: {codigo}) "
                  f"- Ventas: {producto['ventas']}")
   except ValueError:
        print("Debes ingresar un número entero válido.")


def reporte_stock_bajo(inventario):
    if len(inventario) == 0:
        print("No hay productos en el inventario. No se pueden generar reportes.")
        return

    try:
        bajos = {k: v for k, v in inventario.items() if v["disponible"] < v["minimo"]}
        if len(bajos) == 0:
            print(f"No hay productos con stock menor al umbral.")
        else:
            for codigo, producto in bajos.items():
                print(f"- El producto {producto['nombre']} (Código {codigo}): "
                      f"tiene {producto['disponible']} unidades y su umbral mínimo es {producto['minimo']}")
    except ValueError:
        print("Debes ingresar un número entero válido.")

def ventas_realizadas(ventas_registradas):
    if len(ventas_registradas) == 0:
        print("No hay ventas realizadas.")
        return

    try:
        print(ventas_registradas)
        print("Fecha      | Codigo | Unidades |")
        for venta in ventas_registradas:
            print(f"{venta['fecha']} | {str(venta['codigo']).rjust(6)} | {str(venta['unidades']).rjust(8)} |")
    except ValueError:
        print("Debes ingresar un número entero válido.")

def generar_reportes(inventario, ventas_registradas):
    while True:
        print("\n--- Menú de Reportes ---")
        print("1. Top X productos más vendidos (orden por 'ventas')")
        print("2. Productos con stock menor al umbral")
        print("3. Ventas realizadas")
        print("4. Volver al menú principal")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            reporte_top_vendidos(inventario)
        elif opcion == "2":
            reporte_stock_bajo(inventario)
        elif opcion == "3":
            ventas_realizadas(ventas_registradas)
        elif opcion == "4":
            print("Regresando al menú principal...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
