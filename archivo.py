import json
import os

# Clases
class Evento:
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora

class Competidor:
    def __init__(self, nombre, edad, categoria):
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria

class SportPlanningManager:
    def __init__(self):
        self.eventos = []
        self.competidores = []

    def agregar_evento(self, nombre, fecha, hora):
        evento = Evento(nombre, fecha, hora)
        self.eventos.append(evento)
        print("Evento agregado exitosamente.")