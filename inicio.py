# Online Python - IDE, Editor, Compiler, Interpreter
from gestion import gestion_de_productos

valor_ex_1 = {"nombre": "producto 1", "precio" : 1000, "disponible" : 5, "minimo": 3}
valor_ex_2 = {"nombre": "producto 2", "precio" : 1500, "disponible" : 3, "minimo": 2}
registros = {
  1 : valor_ex_1,
  2 : valor_ex_2
}

detalle_largo = {
    "codigo": 6, "nombre": 30, "precio": 8, "disponible":10, "minimo":12
}

cabecero = {
    "Código": 6, "Nombre": 30, "Precio": 8, "Existencia":10, "Mínimo stock":12
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
            gestion_de_productos(registros)
        elif seleccion == "2":
            lista_de_productos()
        elif seleccion == "3":
            busqueda_de_productos()
        elif seleccion == "0":
            print("\nSaliendo")
            break
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")

def lista_de_productos():
    print("Lista de productos")
    productos = listar_productos(registros)
    mostrar_productos(productos)
    input("Presiona Enter para regresar al menú principal.")

def generar_reporte():
    print("Generar reporte")
    print("Se mostrará el listado de reportes a generar.")
    input("Presiona Enter para regresar al menú principal.")

def busqueda_de_productos():
    print("Búsqueda de productos")
    print("Ingrese nombre o código de producto para buscarlo.")
    busqueda = input("Ingresa busqueda: ")
    productos = buscar_producto(registros, busqueda)
    mostrar_productos(productos)
    opcion = input("Presiona Enter para regresar al menú principal o 1 para buscar otro producto. ")
    if opcion == "1":
        busqueda_de_productos()

def diccionario_a_tabla(lista):
    filas = lista[0:]

    elementos_separados = [
        element.ljust(length) for element, length in cabecero.items()
    ]

    print("| " + " | ".join(elementos_separados) +" |")
    for codigo, fila in filas:
        texto_final = ''

        elementos_separados = [
            str(element).ljust(detalle_largo.get(field, len(str(element))))
            for field, element in fila.items()
        ]
        texto_final = texto_final+' | '.join(elementos_separados)
        texto_final = "| " + str(codigo).ljust(detalle_largo["codigo"]) + ' | ' + texto_final
        print(texto_final + " |")


def buscar_producto(diccionario, valor):
    resultados = []
    for id_registro, subdiccionario in diccionario.items():
        if str(valor) == str(id_registro) or str(valor) in str(subdiccionario['nombre']):
            resultados.append((id_registro, subdiccionario))
    return resultados

def listar_productos(diccionario):
    resultados = []
    for id_registro, subdiccionario in diccionario.items():
        resultados.append((id_registro, subdiccionario))
    return resultados

def mostrar_productos(productos):
    print("A continuación se muestra el listado de productos")
    diccionario_a_tabla(productos)

menu()
