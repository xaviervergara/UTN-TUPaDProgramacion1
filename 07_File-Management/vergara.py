# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 

with open("productos.txt", "w") as file:
    file.write("Teclado,$50,27\n")
    file.write("Mouse,$60,39\n")
    file.write("Camara,$70,44\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: 
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as file:
    contenido = file.readlines() # contenido es una lista cuyos elementos se corresponden con cada una de las filas del archivo original
    for filas in contenido: 
        columnas = filas.strip().split(",")
        print(f"Producto: {columnas[0]} | Precio: {columnas[1]} | Cantidad: {columnas[2]}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

producto_usuario = input("Ingrese un producto en el sgte formato: (nombre, precio, cantidad): ")        

with open("productos.txt", "a") as file:
    file.write(producto_usuario)


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad. 

with open("productos.txt", "r") as file:
    contenido = file.readlines()
    productos = [] # contenido es una lista cuyos elementos se corresponden con cada una de las filas del archivo original
    for filas in contenido:
        columnas = filas.strip().split(",")
        productos.append({"nombre": columnas[0], "precio": columnas[1], "cantidad": columnas[2]})
    print(productos)        
             

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error. 

dato_usuario = input("Ingrese el nombre del producto que desea buscar: ")

for producto in productos:
    if dato_usuario == producto["nombre"].lower():
        existe = True
        print(producto)
        break
    else:
        existe = False
if existe == False:
    print("Error: no se encontro el producto")

# Tambien se puede usar esto:
# se deja de usar flag para usar el "for-else" --> estructura de control exclusiva de python 

# for producto in productos:
#     if dato_usuario == producto["nombre"].lower():
#         print(producto)
#         break
# else:
#     print("Error: no se encontro el producto")


# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista.

with open("productos.txt", "w") as file:
    for producto in productos:
        fila = ",".join(producto.values()) # notese como permite trabajar con un type dict list y no tener que usar list(producto.values()) -investigar
        file.write(fila + "\n")