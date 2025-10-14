#Empezar interfaz
import requests
import json

# Listas
List_Entr = []
List_Contr = []
CARRITO = []

#_________________________________________________________________________________________________________________
API_URL = "https://fakestoreapi.com/products"

def Agregar_User():
    Ag_us = input("Agrega un Nombre de usuario: ")
    Ag_cnt = input("Agrega tu contraseña: ")
    List_Entr.append(Ag_us)
    List_Contr.append(Ag_cnt)
    print(f"Usuario '{Ag_us}' agregado correctamente.")

def obt_prod():  # API 
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:  # CORREGIDO: response.status_code
            productos = response.json()
            return productos  # CORREGIDO: retornar los productos
        else:
            print(f"Error al conectar la API: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión a la API: {e}")
        return None

def agregar_prd():  
    # Obtener productos primero
    productos = obt_prod()
    
    if not productos:
        print("No se pudieron obtener los productos de la API")
        return
    
    if len(productos) == 0:
        print("No hay productos disponibles")
        return
    
    # Mostrar productos disponibles
    print("\n--- PRODUCTOS DISPONIBLES ---")
    for producto in productos:
        print(f"ID: {producto['id']} - {producto['title']} - ${producto['price']}")
    
    try: 
        Producto_id = int(input("\nIngrese el ID del producto que quiere agregar: "))
    except ValueError:
        print("Error: Ingresaste un ID inválido")
        return
    
    producto_slct = None
    for x in productos:
        if x['id'] == Producto_id:
            producto_slct = x
            break

    if producto_slct:
        Prev_carr = {
            "id": producto_slct['id'],
            "nombre": producto_slct['title'],
            "precio": producto_slct['price']
        }
        CARRITO.append(Prev_carr)
        print(f"Se ha agregado al CARRITO: {producto_slct['title']} - ${producto_slct['price']}")
    else:
        print("Producto no encontrado")

def ver_carrito():
    if not CARRITO:
        print("El carrito está vacío")
        return
    
    print("\n--- CARRITO DE COMPRAS ---")
    total = 0
    for item in CARRITO:
        print(f"{item['nombre']} - ${item['precio']}")
        total += item['precio']
    print(f"TOTAL: ${total:.2f}")

def remove():
    try:
        rer = int(input("Pon el id del producto que quieres eliminar: "))
        for producto in CARRITO:
            if producto['id'] == rer:  # CORREGIDO: producto['id']
                CARRITO.remove(producto)
                print("Producto Eliminado")
                return
        print("Producto no encontrado en el carrito")  # Mensaje si no encuentra el ID
    except ValueError:
        print("ID debe ser un numero / Ingresaste un valor erroneo")
    


#_______________________________________________________________________________________

def Main():
    print("Bienvenido al sistema de compras")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar Usuario")
        print("2. Agregar al carrito")
        print("3. Ver Carrito")
        print("4. Salir del programa") 
        print("5. Borrar algo del carrito")
        print("----------------------")
        
        try:
            OP = int(input("Elige una opción: "))
        except ValueError:
            print("¡Error! Por favor, ingresa un número válido.")
            continue 
            
        if OP == 1:
            Agregar_User()
        
        elif OP == 2:
            agregar_prd() 
        
        elif OP == 3:
            ver_carrito()
        
        elif OP == 4:
            print("Hasta la próxima!")
            break
             

        elif OP == 5:
            remove()

        

        else:
            print("Opción no válida. Por favor, elige 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
    Main()
