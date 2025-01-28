# Clase que representa una tarea
class Tarea:
    def __init__(self, nombre, descripción):
        self.nombre = nombre
        self.descripción = descripción
        self.estado = "Pendiente"

# Clase que gestiona las tareas
class GestorTareas:
    def __init__(self):
        self.tareas = []  # Lista de tareas

    def agregar_tarea(self, nombre, descripción):  
        nueva_tarea = Tarea(nombre, descripción)
        self.tareas.append(nueva_tarea)

    def mostrar_tareas(self):  
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea.nombre} - {tarea.descripción} [{tarea.estado}]")

# Función principal que interactúa con el usuario
def main():
    gestor = GestorTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripción = input("Descripción de la tarea: ")
            gestor.agregar_tarea(nombre, descripción)

        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
