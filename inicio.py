# Online Python - IDE, Editor, Compiler, Interpreter

valor_ex_1 = {"nombre": "producto 1", "precio" : 1000, "disponible" : 5, "minimo": 3}
valor_ex_2 = {"nombre": "producto 2", "precio" : 1500, "disponible" : 3, "minimo": 2}
data_ex = {
  1 : valor_ex_1,
  2 : valor_ex_2
}

cabecero = [
    "Cod.", "Nombre", "Precio", "Q", "Min"
]

def menu():
    while True:
        print("Menú, presione tecla para avanzar")
        print("1. Gestión de productos")
        print("2. Lista de productos")
        print("3. Búsqueda de productos")
        print("4. Generar reporte")
        print("0. Salir")
        seleccion = input("Escribe una opción: ")

        if seleccion == "1":
            gestion_de_productos()
        elif seleccion == "2":
            lista_de_productos()
        elif seleccion == "3":
            busqueda_de_productos()
        elif seleccion == "0":
            print("\nSaliendo")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")


def gestion_de_productos():
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

    gestion_de_productos()


def lista_de_productos():
    print("Lista de productos")
    print("Aquí se mostraría una lista de productos, pero estamos trabajando en eso.")
    input("Presiona Enter para regresar al menú principal.")

def generar_reporte():
    print("Generar reporte")
    print("Se mostrará el listado de reportes a generar.")
    input("Presiona Enter para regresar al menú principal.")

def busqueda_de_productos():
    print("Búsqueda de productos")
    print("Ingrese nombre o código de producto para buscarlo.")
    busqueda = input("Ingresa busqueda: ")
    productos = buscar_producto(data_ex, busqueda)
    print ("A continuación se muestra el listado de productos")
    diccionario_a_tabla(productos)
    opcion = input("Presiona Enter para regresar al menú principal o 1 para buscar otro producto.")
    if opcion == "1":
        busqueda_de_productos()

def diccionario_a_tabla(lista):
    filas = lista[0:]

    def procesar_valor(valor):
        if isinstance(valor, dict):
            return " | ".join(map(str, valor.values()))
        return str(valor)

    print("| " + " | ".join(map(str, cabecero)) +" |")
    for fila in filas:
        print("| " + " | ".join(map(procesar_valor, fila)) + " |")

def buscar_producto(diccionario, valor):
    resultados = []
    for id_registro, subdiccionario in diccionario.items():
        if str(valor) == str(id_registro) or str(valor) in str(subdiccionario['nombre']):
            resultados.append((id_registro, subdiccionario))
    return resultados

menu()
