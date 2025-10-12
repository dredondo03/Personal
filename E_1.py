#Logica correcta
#Hay que mejorar la conexion a la API

import requests
import _json
#Listas
List_Entr = []
List_Contr = []
CARRITO = []
#_________________________________________________________________________________________________________________
API_URL = "https://fakestoreapi.com/products"
def Agregar_User ():
   Ag_us = (input(" Agrega un Nombre de usuario "))
   Ag_cnt = (input(" Agrega tu contraseña "))
   List_Entr.append(Ag_us)
   List_Contr.append(Ag_cnt)

def obt_prod (): #API Obtencion
    try:
        response= requests.get(API_URL)
        if response == 200:
            productos = response.json()
        else:
            print("Error al conectar la API{response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexion a la API")
        return None

def agregar_prd(Productos):
    if not Productos:
        print("No hay nada en el carrito")
        return
    try: 
        Producto_id= int(input("Ingrese el ID del producto que quiere agregar"))
    except ValueError:
        print("Ingresaste mal el ID o el producto no existe")
        return
    for x in Productos:
        if x['id'] == Producto_id:
            producto_slct = x
            break

    if producto_slct:
        Prev_carr = {
            "id" : producto_slct['id'],
            "nombre" : producto_slct['title'],
            "precio" : producto_slct['price']
        }
        CARRITO.append(Prev_carr)
        print(f"Se ha agregado al CARRITO {producto_slct['id']},{producto_slct['title']},{producto_slct['price']}")







#_______________________________________________________________________________________


def Main():
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar Usuario")
        print("2. Agregar al carrito")
        print("3. Confirmar Pedido y Pago (Ver Carrito)")
        print("4. Salir del programa") 
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
            
            print("\nContenido del carrito:", CARRITO)
        
        
        elif OP == 4:
            print("Hasta la proximaaaa")
            break 
        
        else:
            
            print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")


    
    
Main() 
