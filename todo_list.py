import tkinter as tk
from tkinter import messagebox

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

    def obtener_tareas(self):
        if not self.tareas:
            return ["No hay tareas pendientes."]
        else:
            return [f"{tarea.nombre} - {tarea.descripción} [{tarea.estado}]" for tarea in self.tareas]

# Clase para la interfaz gráfica
class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        
        self.gestor = GestorTareas()

        # Etiquetas y campos de entrada
        self.nombre_label = tk.Label(root, text="Nombre de la tarea:")
        self.nombre_label.pack()
        
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.descripcion_label = tk.Label(root, text="Descripción de la tarea:")
        self.descripcion_label.pack()

        self.descripcion_entry = tk.Entry(root)
        self.descripcion_entry.pack()

        # Botón para agregar tarea
        self.agregar_button = tk.Button(root, text="Agregar tarea", command=self.agregar_tarea)
        self.agregar_button.pack()

        # Lista para mostrar tareas
        self.lista_tareas_label = tk.Label(root, text="Tareas pendientes:")
        self.lista_tareas_label.pack()

        self.lista_tareas = tk.Listbox(root)
        self.lista_tareas.pack()

        # Botón para actualizar la lista de tareas
        self.actualizar_button = tk.Button(root, text="Actualizar lista de tareas", command=self.actualizar_lista_tareas)
        self.actualizar_button.pack()

    def agregar_tarea(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()

        if nombre and descripcion:
            self.gestor.agregar_tarea(nombre, descripcion)
            self.nombre_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Entrada incorrecta", "Por favor, ingresa un nombre y una descripción para la tarea.")

    def actualizar_lista_tareas(self):
        # Limpiar la lista actual
        self.lista_tareas.delete(0, tk.END)
        
        # Obtener las tareas actuales y mostrarlas en la lista
        tareas = self.gestor.obtener_tareas()
        for tarea in tareas:
            self.lista_tareas.insert(tk.END, tarea)

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazGrafica(root)
    root.mainloop()
