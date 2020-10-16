import usuarios.usuario as modelo

class Acciones:

    def registro(self):
            print("\nOK!!! Vamos a registrate en el sistema...")
            nombre = input("¿Cual es tu nombre?: ")
            apellidos = input("¿Cuales son tus apellidos?: ")
            email = input("¿Cual es tu email?: ")
            password = input("¿Cual es tu contraseña?: ")
    
            usuario = modelo.Usuario(nombre, apellidos, email, password)
            registro = usuario.registrar()

            if registro[0] >= 1:
                print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            else:
                print("\nNo te has registrado correectamente !!!")


    def login(self):
        print("Vale!!! Identifícate en el sistema...")
        
        try:
            email = input("¿Cual es tu nombre?: ")
            password = input("¿Cual es tu contraseña?: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()

        
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema {login[5]}.")
                self.proximasAcciones(login)
                
        except Exception: # as identifier:
            # print(type(identifier))
            # print(type(identifier).__name__)
            print(f"Login incorrecto!!! Inténtalo más tarde")
        

    def proximasAcciones(self, usuario):
        pass