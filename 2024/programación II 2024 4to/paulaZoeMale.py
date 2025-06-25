#Clase 03_04
# Inicializa un diccionario vacío llamado 'productos' con cuatro categorías como claves
productos = {
    'lácteos': [],
    'carnes': [],
    'verduras': [],
    'legumbres': []
}




def cargar_producto(categoria): # Define una función llamada 'cargar_producto' que toma una categoría como argumento
    producto = input("Ingrese el nombre del producto: ")  # Solicita al usuario que ingrese el nombre de un producto
    productos[categoria].append(producto)  # Agrega el producto a la categoría especificada en el diccionario 'productos'
    print("Producto cargado exitosamente.") # Muestra un mensaje de éxito


def mostrar_productos(): # Define una función llamada 'mostrar_productos' que itera sobre cada categoría y sus productos
    for categoria, productos_categoria in productos.items(): # Iterar sobre cada categoría y su correspondiente lista de productos
        print(f"Categoría: {categoria}") # Muestra el nombre de la categoría
        if len(productos_categoria) == 0:  # Verifica si hay productos en la categoría actual
            print("No hay productos en stock.") # Si no hay productos, muestra un mensaje indicando que no hay productos en stock
        else:
            for producto in productos_categoria: # Si hay productos, itera sobre cada uno y muéstralo
                print(producto) # Muestra una línea en blanco para separar cada categoría
        print()


def menu(): # Define una función llamada 'menu' que muestra un menú y toma la entrada del usuario
    while True: # Muestra el menú y toma la entrada del usuario hasta que elijan salir
        print("----- MENÚ -----")
        print("1. Cargar producto")
        print("2. Mostrar productos en stock")
        print("0. Salir")
        opcion = input("Ingrese una opción: ") # Toma diferentes acciones dependiendo de la elección del menú del usuario


        if opcion == "1":
            categoria = input("Ingrese la categoría del producto (lácteos, carnes, verduras, legumbres): ")
            if categoria in productos:
                cargar_producto(categoria) # Llama a la función 'cargar_producto' con la categoría elegida por el usuario
            else:
                print("Categoría inválida.")
        elif opcion == "2":
            mostrar_productos() # Llama a la función 'mostrar_productos' para mostrar todos los productos en stock
        elif opcion == "0": # Muestra un mensaje de despedida y sale del programa
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.") # Si el usuario ingresa una opción inválida, muestra un mensaje de error


menu() # Llama a la función 'menu' para iniciar el programa