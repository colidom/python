def show_contacts(phone_book):
    print(" ")
    if phone_book == {}:
        print("==Lista de contactos vacía==")
    else:
        print("==Lista de contactos==")
        for name, number in phone_book.items():
            print(f"{name}: {number}")
        print(" ")
        input("Pulse ENTER para volver al menú.")


def add_contact(phone_book, name, phone):
    phone_book[name] = phone


def remove_contact(phone_book, name):
    del(phone_book[name])


def menu():
    phone_book = {}
    try:
        while True:
            print("******************************")
            print("1. Mostrar lista de contactos.")
            print("2. Insertar un nuevo contacto.")
            print("3. Borrar un contacto.")
            print("4. Salir. ")
            print("******************************")
            option = input("Elija una opción: ")
            option = int(option)
            if option == 1:
                show_contacts(phone_book)
            if option == 2:
                name = input("Introduzca el nombre: ")
                if name in phone_book:
                    print(f"Error, el contacto '{name}' ya existe.")
                else:
                    phone = input("Introduzca el número de teléfono: ")
                    add_contact(phone_book, name, phone)
            if option == 3:
                name = input("Nombre del contacto que decea eliminar: ")
                if name in phone_book:
                    remove_contact(phone_book, name)
                    print(f"Eliminado el contacto '{name}'...")
                else:
                    print(f"Error...el contacto '{name}' no existe.")
            if option == 4:
                print("Adiós.")
                break
    except:
        menu()
menu()
