class Contenido:
    def __init__(self, titulo, tipo, duracion, genero):
        self.titulo = titulo
        self.tipo = tipo 
        self.duracion = duracion  # En minutos
        self.genero = genero
        self.popularidad = 0 

    def aumentar_popularidad(self):
        self.popularidad += 1

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - Popularidad: {self.popularidad}"