import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOK {usuario[1]}!!!Vamos a crear una nueva nota...")
        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")
            