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

# Clase para manejar el almacenamiento de datos
class DataManager:
    @staticmethod
    def guardar_datos(eventos, competidores, archivo_eventos="eventos.json", archivo_competidores="competidores.json"):
        eventos_dict = [evento.__dict__ for evento in eventos]
        competidores_dict = [competidor.__dict__ for competidor in competidores]
        
        with open(archivo_eventos, 'w') as f:
            json.dump(eventos_dict, f)
        with open(archivo_competidores, 'w') as f:
            json.dump(competidores_dict, f)
        
        print("Datos guardados exitosamente.")

    @staticmethod
    def cargar_datos(archivo_eventos="eventos.json", archivo_competidores="competidores.json"):
        eventos, competidores = [], []
        
        if os.path.exists(archivo_eventos):
            with open(archivo_eventos, 'r') as f:
                eventos_dict = json.load(f)
                eventos = [Evento(**evento) for evento in eventos_dict]
        
        if os.path.exists(archivo_competidores):
            with open(archivo_competidores, 'r') as f:
                competidores_dict = json.load(f)
                competidores = [Competidor(**competidor) for competidor in competidores_dict]
        
        print("Datos cargados exitosamente.")
        return eventos, competidores

# Clase principal para gestionar los eventos y competidores
class SportPlanningManager:
    def __init__(self):
        self.eventos = [] 
        self.competidores = [] 

    # Función para agregar un evento a la lista de eventos
    def agregar_evento(self, nombre, fecha, hora):
        if any(evento.nombre == nombre for evento in self.eventos):
            print("El evento ya existe.")
        else:
            evento = Evento(nombre, fecha, hora)
            self.eventos.append(evento)
            print("Evento agregado exitosamente.")

    # Función para eliminar un evento de la lista de eventos
    def eliminar_evento(self, nombre):
        if any(evento.nombre == nombre for evento in self.eventos):
            self.eventos = [evento for evento in self.eventos if evento.nombre != nombre]
            print("Evento eliminado exitosamente.")
        else:
            print("Evento no encontrado.")

    # Función para agregar un competidor a la lista de competidores
    def agregar_competidor(self, nombre, edad, categoria):
        if any(competidor.nombre == nombre for competidor in self.competidores):
            print("El competidor ya existe.")
        else:
            competidor = Competidor(nombre, edad, categoria)
            self.competidores.append(competidor)
            print("Competidor agregado exitosamente.")

    # Función para eliminar un competidor de la lista de competidores
    def eliminar_competidor(self, nombre):
        if any(competidor.nombre == nombre for competidor in self.competidores):
            self.competidores = [competidor for competidor in self.competidores if competidor.nombre != nombre]
            print("Competidor eliminado exitosamente.")
        else:
            print("Competidor no encontrado.")

    # Función para mostrar todos los eventos
    def mostrar_eventos(self):
        if self.eventos:
            for evento in self.eventos:
                print(f"Nombre: {evento.nombre}, Fecha: {evento.fecha}, Hora: {evento.hora}")
        else:
            print("No hay eventos para mostrar.")

    # Función para mostrar todos los competidores
    def mostrar_competidores(self):
        if self.competidores:
            for competidor in self.competidores:
                print(f"Nombre: {competidor.nombre}, Edad: {competidor.edad}, Categoría: {competidor.categoria}")
        else:
            print("No hay competidores para mostrar.")
    
    # Función para modificar los detalles de un evento ya existente
    def modificar_evento(self, nombre, nuevo_nombre, nueva_fecha, nueva_hora):
        for evento in self.eventos:
            if evento.nombre == nombre:
                evento.nombre = nuevo_nombre
                evento.fecha = nueva_fecha
                evento.hora = nueva_hora
                print("Evento modificado exitosamente.")
                return
        print("Evento no encontrado.")

    # Función para modificar los detalles de un competidor ya existente
    def modificar_competidor(self, nombre, nuevo_nombre, nueva_edad, nueva_categoria):
        for competidor in self.competidores:
            if competidor.nombre == nombre:
                competidor.nombre = nuevo_nombre
                competidor.edad = nueva_edad
                competidor.categoria = nueva_categoria
                print("Competidor modificado exitosamente.")
                return
        print("Competidor no encontrado.")

# Función principal para mostrar el menú y manejar la interacción del usuario
def menu():
    manager = SportPlanningManager()
    manager.eventos, manager.competidores = DataManager.cargar_datos()
    
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
            DataManager.guardar_datos(manager.eventos, manager.competidores)
        elif opcion == "10":
            DataManager.guardar_datos(manager.eventos, manager.competidores)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()



