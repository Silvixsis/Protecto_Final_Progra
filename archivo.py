import json
import os

# Clase que representa un evento deportivo
class Evento:
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}")

    @staticmethod
    def mostrar_eventos(eventos):
        if eventos:
            for evento in eventos:
                evento.mostrar_detalles()
        else:
            print("No hay eventos para mostrar.")

# Clase que representa un competidor
class Competidor:
    def __init__(self, nombre, apellido, edad, evento, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.evento = evento
        self.categoria = categoria

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}, Evento: {self.evento}, Categoría: {self.categoria}")

    @staticmethod
    def mostrar_competidores(competidores):
        if competidores:
            for competidor in competidores:
                competidor.mostrar_detalles()
        else:
            print("No hay competidores para mostrar.")

# Clase para manejar el almacenamiento de datos
class ManejoDatos:  
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
        self.eventos, self.competidores = ManejoDatos.cargar_datos()

    def agregar_evento(self, nombre, fecha, hora):
        if any(evento.nombre == nombre for evento in self.eventos):
            print("El evento ya existe.")
        else:
            evento = Evento(nombre, fecha, hora)
            self.eventos.append(evento)
            print("Evento agregado exitosamente.")

    def eliminar_evento(self, nombre):
        eventos_antes = len(self.eventos)
        self.eventos = [evento for evento in self.eventos if evento.nombre != nombre]
        if len(self.eventos) < eventos_antes:
            print("Evento eliminado exitosamente.")
        else:
            print("Evento no encontrado.")

    def agregar_competidor(self, nombre, apellido, edad, evento, categoria):
        if any(competidor.nombre == nombre and competidor.apellido == apellido for competidor in self.competidores):
            print("El competidor ya existe.")
        else:
            competidor = Competidor(nombre, apellido, edad, evento, categoria)
            self.competidores.append(competidor)
            print("Competidor agregado exitosamente.")

    def eliminar_competidor(self, nombre, apellido):
        competidores_antes = len(self.competidores)
        self.competidores = [competidor for competidor in self.competidores if not (competidor.nombre == nombre and competidor.apellido == apellido)]
        if len(self.competidores) < competidores_antes:
            print("Competidor eliminado exitosamente.")
        else:
            print("Competidor no encontrado.")
    
    def modificar_evento(self, nombre, nuevo_nombre, nueva_fecha, nueva_hora):
        for evento in self.eventos:
            if evento.nombre == nombre:
                evento.nombre = nuevo_nombre
                evento.fecha = nueva_fecha
                evento.hora = nueva_hora
                print("Evento modificado exitosamente.")
                return
        print("Evento no encontrado.")

    def modificar_competidor(self, nombre, apellido, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_evento, nueva_categoria):
        for competidor in self.competidores:
            if competidor.nombre == nombre and competidor.apellido == apellido:
                competidor.nombre = nuevo_nombre
                competidor.apellido = nuevo_apellido
                competidor.edad = nueva_edad
                competidor.evento = nuevo_evento
                competidor.categoria = nueva_categoria
                print("Competidor modificado exitosamente.")
                return
        print("Competidor no encontrado.")

# Función principal para mostrar el menú y manejar la interacción del usuario
def menu():
    manager = SportPlanningManager()
    
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
            apellido = input("Apellido del competidor: ")
            edad = input("Edad del competidor: ")
            evento = input("Evento del competidor: ")
            categoria = input("Categoría del competidor: ")
            manager.agregar_competidor(nombre, apellido, edad, evento, categoria)
        elif opcion == "4":
            nombre = input("Nombre del competidor a eliminar: ")
            apellido = input("Apellido del competidor a eliminar: ")
            manager.eliminar_competidor(nombre, apellido)
        elif opcion == "5":
            Evento.mostrar_eventos(manager.eventos)
        elif opcion == "6":
            Competidor.mostrar_competidores(manager.competidores)
        elif opcion == "7":
            nombre = input("Nombre del evento a modificar: ")
            nuevo_nombre = input("Nuevo nombre del evento: ")
            nueva_fecha = input("Nueva fecha del evento (dd-mm-aaaa): ")
            nueva_hora = input("Nueva hora del evento (hh:mm): ")
            manager.modificar_evento(nombre, nuevo_nombre, nueva_fecha, nueva_hora)
        elif opcion == "8":
            nombre = input("Nombre del competidor a modificar: ")
            apellido = input("Apellido del competidor a modificar: ")
            nuevo_nombre = input("Nuevo nombre del competidor: ")
            nuevo_apellido = input("Nuevo apellido del competidor: ")
            nueva_edad = input("Nueva edad del competidor: ")
            nuevo_evento = input("Nuevo evento del competidor: ")
            nueva_categoria = input("Nueva categoría del competidor: ")
            manager.modificar_competidor(nombre, apellido, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_evento, nueva_categoria)
        elif opcion == "9":
            ManejoDatos.guardar_datos(manager.eventos, manager.competidores)
        elif opcion == "10":
            ManejoDatos.guardar_datos(manager.eventos, manager.competidores)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()







