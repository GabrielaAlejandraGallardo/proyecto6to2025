productos_lacteos = []
productos_carnes = []
productos_verduras = []
productos_legumbres = []




def cargar_productos(categoria): #define una funcion para cargar producto
    nombre = input("Ingrese el nombre del producto: ") #le pide al usuario que ingrese el nombre del productos que desea agregar
    precio = int(input("Ingrese el precio del producto: ")) #le pide al usuario que ingrese el precio del producto
   
    if categoria == "lacteos":
        productos_lacteos.append((nombre, precio))
    elif categoria == "carnes":
        productos_carnes.append((nombre, precio))
    elif categoria == "verduras":
        productos_verduras.append((nombre, precio))
    elif categoria == "legumbres":
        productos_legumbres.append((nombre, precio))
    else:
        print("Categoría inválida.")
    #eso es para que el usuario pueda elegir en que categoria quiere añadir el producto




# Función para mostrar los productos en stock
def mostrar_productos():
    print("Productos en la categoría lácteos:")
    for producto in productos_lacteos:
        print(producto[0], "-", producto[1])
   
    print("\nProductos en la categoría carnes:")
    for producto in productos_carnes:
        print(producto[0], "-", producto[1])
   
    print("\nProductos en la categoría verduras:")
    for producto in productos_verduras:
        print(producto[0], "-", producto[1])
   
    print("\nProductos en la categoría legumbres:")
    for producto in productos_legumbres:
        print(producto[0], "-", producto[1])




# creamos el menu
while True:
    print("\nMenú:")
    print("1. Cargar productos")
    print("2. Mostrar productos en stock")
    print("3. Salir")
   
    opcion = input("Seleccione una opción: ")
   
    if opcion == "1":
        categoria = input("Ingrese la categoría de productos (lacteos, carnes, verduras, legumbres): ")
        cargar_productos(categoria)
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


