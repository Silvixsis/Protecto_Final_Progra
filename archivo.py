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
        self.eventos = []  # Lista para almacenar eventos
        self.competidores = []  # Lista para almacenar competidores

    # Agregar un evento a la lista de eventos
    def agregar_evento(self, nombre, fecha, hora):
        evento = Evento(nombre, fecha, hora)
        self.eventos.append(evento)
        print("Evento agregado exitosamente.")

    # Eliminar un evento de la lista de eventos
    def eliminar_evento(self, nombre):
        self.eventos = [evento for evento in self.eventos if evento.nombre != nombre]
        print("Evento eliminado exitosamente.")

    # Agregar un competidor a la lista de competidores
    def agregar_competidor(self, nombre, edad, categoria):
        competidor = Competidor(nombre, edad, categoria)
        self.competidores.append(competidor)
        print("Competidor agregado exitosamente.")

    # Eliminar un competidor de la lista de competidores
    def eliminar_competidor(self, nombre):
        self.competidores = [competidor for competidor in self.competidores if competidor.nombre != nombre]
        print("Competidor eliminado exitosamente.")

    # Mostrar todos los eventos
    def mostrar_eventos(self):
        for evento in self.eventos:
            print(f"Nombre: {evento.nombre}, Fecha: {evento.fecha}, Hora: {evento.hora}")

    # Mostrar todos los competidores
    def mostrar_competidores(self):
        for competidor in self.competidores:
            print(f"Nombre: {competidor.nombre}, Edad: {competidor.edad}, Categoría: {competidor.categoria}")
