from controllers.cliente_controller import crear_cliente
from controllers.propiedad_controller import agregar_propiedad
from controllers.renta_controller import rentar_propiedad

def menu():
    print("1. Crear Cliente")
    print("2. Agregar Propiedad")
    print("3. Rentar Propiedad")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_cliente(input("Nombre: "), input("Correo: "), input("Contraseña: "))
    elif opcion == "2":
        id_dueno = input("ID Dueño: ")
        direccion = input("Dirección: ")
        tipo = input("Tipo: ")
        valor = float(input("Valor: "))
        agregar_propiedad(id_dueno, direccion, tipo, valor)
    elif opcion == "3":
        rentar_propiedad(input("ID Cliente: "), input("ID Propiedad: "))
    elif opcion == "0":
        exit()
    else:
        print("Opción inválida")

from interfaz import crear_ventana

crear_ventana()





if __name__ == "__main__":
    while True:
        menu()

