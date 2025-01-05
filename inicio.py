# Online Python - IDE, Editor, Compiler, Interpreter

valor_ex_1 = {"codigo": 1, "nombre": "producto 1", "precio" : 1000, "disponible" : 5, "minimo": 3}
valor_ex_2 = {"codigo": 2, "nombre": "producto 2", "precio" : 1500, "disponible" : 3, "minimo": 2}
data_ex = {
  1 : valor_ex_1,
  2 : valor_ex_2
}

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
    print("Gestión de productos")
    print("Esta sección está en construcción.")
    input("Presiona Enter para regresar al menú principal.")


def lista_de_productos():
    print("Lista de productos")
    print("Aquí se mostraría una lista de productos, pero estamos trabajando en eso.")
    input("Presiona Enter para regresar al menú principal.")

def busqueda_de_productos():
    print("Búsqueda de productos")
    print("Ingrese nombre o código de producto para buscarlo.")
    busqueda = input("Ingresa busqueda: ")
    productos = buscar_producto(data_ex, busqueda)
    print(productos) # TODO : mostrar mejor la lista
    opcion = input("Presiona Enter para regresar al menú principal o 1 para buscar otro producto.")
    if opcion == "1":
        busqueda_de_productos()


def buscar_producto(diccionario, valor):
    resultados = []
    for id_registro, subdiccionario in diccionario.items():
        #print ("Subdiccionario")
        #print(subdiccionario)
        if str(valor) == str(subdiccionario['codigo']) or str(valor) in str(subdiccionario['nombre']):
            resultados.append((id_registro, subdiccionario))
    return resultados

menu()
