#Bibliotecas utilizadas

import json
import os

# Clase que representa un evento deportivo
class Evento:
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora

# Clase que representa un competidor
class Competidor:
    def __init__(self, nombre, edad, categoria):
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

# Clase principal para gestionar los eventos y competidores
class SportPlanningManager:
    def __init__(self):

        #Listass para almacenar eventos y competidores
        self.eventos = [] 
        self.competidores = [] 

    # Funcion para agregar un evento a la lista de eventos
    def agregar_evento(self, nombre, fecha, hora):
        evento = Evento(nombre, fecha, hora)
        self.eventos.append(evento)
        print("Evento agregado exitosamente.")

    # Funcion para eliminar un evento de la lista de eventos
    def eliminar_evento(self, nombre):
        self.eventos = [evento for evento in self.eventos if evento.nombre != nombre]
        print("Evento eliminado exitosamente.")

    # Funcion para agregar un competidor a la lista de competidores
    def agregar_competidor(self, nombre, edad, categoria):
        competidor = Competidor(nombre, edad, categoria)
        self.competidores.append(competidor)
        print("Competidor agregado exitosamente.")

    # Funcion para eliminar un competidor de la lista de competidores
    def eliminar_competidor(self, nombre):
        self.competidores = [competidor for competidor in self.competidores if competidor.nombre != nombre]
        print("Competidor eliminado exitosamente.")

    # Funcion para mostrar todos los eventos
    def mostrar_eventos(self):
        for evento in self.eventos:
            print(f"Nombre: {evento.nombre}, Fecha: {evento.fecha}, Hora: {evento.hora}")

    # Funcion para mostrar todos los competidores
    def mostrar_competidores(self):
        for competidor in self.competidores:
            print(f"Nombre: {competidor.nombre}, Edad: {competidor.edad}, Categoría: {competidor.categoria}")
    
    # Funcion para modificar los detalles de un evento ya existente
    def modificar_evento(self, nombre, nuevo_nombre, nueva_fecha, nueva_hora):
        for evento in self.eventos:
            if (evento.nombre == nombre):
                evento.nombre = nuevo_nombre
                evento.fecha = nueva_fecha
                evento.hora = nueva_hora
                print("Evento modificado exitosamente.")
                return
        print("Evento no encontrado.")

    # Funcion para modificar los detalles de un competidor ya existente
    def modificar_competidor(self, nombre, nuevo_nombre, nueva_edad, nueva_categoria):
        for competidor in self.competidores:
            if competidor.nombre == nombre:
                competidor.nombre = nuevo_nombre
                competidor.edad = nueva_edad
                competidor.categoria = nueva_categoria
                print("Competidor modificado exitosamente.")
                return
        print("Competidor no encontrado.")

    # Funcion para guardar los datos de eventos y competidores en archivos JSON
    def guardar_datos(self, archivo_eventos="eventos.json", archivo_competidores="competidores.json"):
        eventos_dict = [evento.__dict__ for evento in self.eventos]
        competidores_dict = [competidor.__dict__ for competidor in self.competidores]
        
        with open(archivo_eventos, 'w') as f:
            json.dump(eventos_dict, f)
        with open(archivo_competidores, 'w') as f:
            json.dump(competidores_dict, f)
        
        print("Datos guardados exitosamente.")

    # Funcion para cargar los datos de eventos y competidores desde archivos JSON
    def cargar_datos(self, archivo_eventos="eventos.json", archivo_competidores="competidores.json"):
        if os.path.exists(archivo_eventos):
            with open(archivo_eventos, 'r') as f:
                eventos_dict = json.load(f)
                self.eventos = [Evento(**evento) for evento in eventos_dict]
        
        if os.path.exists(archivo_competidores):
            with open(archivo_competidores, 'r') as f:
                competidores_dict = json.load(f)
                self.competidores = [Competidor(**competidor) for competidor in competidores_dict]
        
        print("Datos cargados exitosamente.")

# Función principal para mostrar el menú y manejar la interacción del usuario
def menu():
    manager = SportPlanningManager()
    manager.cargar_datos()
    
    while True:
        print("\n--- Sport Planning Manager ---")
        print("1. Agregar Evento")
        print("2. Eliminar Evento")
        print("3. Agregar Competidor")
        print("4. Eliminar Competidor")
        print("5. Mostrar Eventos")
        print("6. Mostrar Competidores")
        print("7. Modificar Evento")
        print("8. Modificar Competidor")
        print("9. Guardar Datos")
        print("10. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del evento: ")
            fecha = input("Fecha del evento (dd-mm-aaaa): ")
            hora = input("Hora del evento (hh:mm): ")
            manager.agregar_evento(nombre, fecha, hora)
        elif opcion == "2":
            nombre = input("Nombre del evento a eliminar: ")
            manager.eliminar_evento(nombre)
        elif opcion == "3":
            nombre = input("Nombre del competidor: ")
            edad = input("Edad del competidor: ")
            categoria = input("Categoría del competidor: ")
            manager.agregar_competidor(nombre, edad, categoria)
        elif opcion == "4":
            nombre = input("Nombre del competidor a eliminar: ")
            manager.eliminar_competidor(nombre)
        elif opcion == "5":
            manager.mostrar_eventos()
        elif opcion == "6":
            manager.mostrar_competidores()
        elif opcion == "7":
            nombre = input("Nombre del evento a modificar: ")
            nuevo_nombre = input("Nuevo nombre del evento: ")
            nueva_fecha = input("Nueva fecha del evento (dd-mm-aaaa): ")
            nueva_hora = input("Nueva hora del evento (hh:mm): ")
            manager.modificar_evento(nombre, nuevo_nombre, nueva_fecha, nueva_hora)
        elif opcion == "8":
            nombre = input("Nombre del competidor a modificar: ")
            nuevo_nombre = input("Nuevo nombre del competidor: ")
            nueva_edad = input("Nueva edad del competidor: ")
            nueva_categoria = input("Nueva categoría del competidor: ")
            manager.modificar_competidor(nombre, nuevo_nombre, nueva_edad, nueva_categoria)
        elif opcion == "9":
            manager.guardar_datos()
        elif opcion == "10":
            manager.guardar_datos()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    menu()


