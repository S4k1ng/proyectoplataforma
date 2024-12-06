from datetime import datetime 

class Usuario:
    def __init__ (self, nombre, fecha_nacimiento, preferencias,):
        try:
            self.nombre = nombre
            self.preferencias = preferencias
            self.historial_de_visualizacion = []        
            self.fecha_nacimiento = (datetime.now() - datetime.strptime(fecha_nacimiento, "%d/%m/%Y")).days // 365
        except ValueError:
            raise ValueError("Formato de fecha incorrecto, use DD/MM/AAAA.")

    def agregar_visualizacion(self, contenido):
        self.historial_de_visualizacion.append(contenido)
        contenido.aumentar_popularidad()

    def __lt__(self, other):
        return self.nombre < other.nombre

    def __eq__(self, other):
        return self.nombre == other.nombre

    def __str__(self):
        return f"Usuario: {self.nombre}, Edad: {self.fecha_nacimiento}, Preferencias: {self.preferencias}"