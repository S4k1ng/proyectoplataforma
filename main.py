from plataforma import Plataforma
from usuario import Usuario
from contenido import Contenido
from arbol_binario import ABB
from arbol_general import CatalogoGeneral, NodoGeneral
from grafo import GrafoContenido 
from datetime import datetime

# Crear la plataforma
plataforma = Plataforma()

peliculas = [
    ("Avengers: Endgame", 181, "Acción"),
    ("The Lion King", 118, "Animación"),
    ("Joker", 122, "Drama"),
    ("Titanic", 195, "Romance"),
    ("Inception", 148, "Ciencia ficción"),
    ("The Dark Knight", 152, "Acción"),
    ("Forrest Gump", 142, "Drama"),
    ("The Matrix", 136, "Ciencia ficción"),
    ("The Godfather", 175, "Crimen"),
    ("Star Wars: Episode V - The Empire Strikes Back", 124, "Acción"),
    ("Pulp Fiction", 154, "Crimen"),
    ("Fight Club", 139, "Drama"),
    ("Interstellar", 169, "Ciencia ficción"),
    ("The Shawshank Redemption", 142, "Drama"),
    ("Gladiator", 155, "Acción"),
    ("The Dark Knight Rises", 164, "Acción"),
    ("The Avengers", 143, "Acción"),
    ("Black Panther", 134, "Acción"),
    ("Guardians of the Galaxy", 121, "Acción")
]

# Agregar películas al catálogo
for pelicula in peliculas:
    plataforma.agregar_pelicula(pelicula[0], pelicula[1], pelicula[2])


series = [
    ("Breaking Bad", "Crimen"),
    ("Stranger Things", "Ciencia ficción"),
    ("Game of Thrones", "Fantasía"),
    ("The Mandalorian", "Acción"),
    ("The Crown", "Drama"),
    ("The Witcher", "Fantasía"),
    ("Narcos", "Crimen"),
    ("Friends", "Comedia"),
    ("The Office", "Comedia"),
    ("Black Mirror", "Ciencia ficción")
]

# Agregar series al catálogo
for serie_nombre, genero in series:
    serie = NodoGeneral(serie_nombre, "serie", genero=genero)
    for i in range(1, 4):  # 3 temporadas por serie
        temporada = NodoGeneral(f"Temporada{i}", "temporada")
        for j in range(1, 6):  # 5 capítulos por temporada
            episodio = NodoGeneral(f"Episodio{j}", "episodio")
            temporada.agregar_hijo(episodio)
        serie.agregar_hijo(temporada)
    plataforma.agregar_serie(serie_nombre, genero, serie)


usuarios = [
    ("Carlos", "01/01/1990", ["Acción", "Ciencia ficción", "Crimen"]),
    ("Ana", "15/03/1992", ["Comedia", "Drama", "Romance"]),
    ("Juan", "20/07/1985", ["Acción", "Ciencia ficción", "Animación"]),
    ("Maria", "10/09/1987", ["Drama", "Romance", "Comedia"]),
    ("Luis", "25/12/1990", ["Ciencia ficción", "Acción", "Crimen"]),
    ("Sofia", "12/06/1989", ["Ciencia ficción", "Drama", "Fantasía"]),
    ("Pedro", "03/02/1991", ["Comedia", "Acción", "Romance"]),
    ("Lucia", "09/11/1992", ["Acción", "Drama", "Comedia"]),
    ("Jorge", "15/05/1994", ["Fantasía", "Comedia", "Acción"]),
    ("Paula", "22/08/1986", ["Romance", "Drama", "Fantasía"]),
    ("Raul", "05/04/1988", ["Acción", "Fantasía", "Ciencia ficción"]),
    ("Elena", "30/11/1990", ["Comedia", "Ciencia ficción", "Drama"]),
    ("Andres", "13/10/1985", ["Acción", "Romance", "Drama"]),
    ("Victoria", "01/12/1993", ["Acción", "Ciencia ficción", "Fantasía"]),
    ("Samuel", "28/03/1991", ["Comedia", "Crimen", "Romance"])
]

# Agregar usuarios a la plataforma
for nombre, fecha_nacimiento, preferencias in usuarios:
    usuario = Usuario(nombre, fecha_nacimiento, preferencias)
    plataforma.agregar_usuario(usuario)

    # Agregar al historial de cada usuario al menos 7 visualizaciones (películas y series)
    for j in range(7):
        contenido = plataforma.catalogo_general.raiz.hijos[j % len(plataforma.catalogo_general.raiz.hijos)].hijos[j % 3]  # Alternar entre películas y series
        usuario.agregar_visualizacion(contenido)

# Mostrar el catálogo de contenido
#plataforma.mostrar_catalogo()

# Mostrar historial de un usuario específico
print("\nHistorial de Carlos:")
historial = plataforma.mostrar_historial_usuario("Carlos")
print(historial)

# Generar recomendaciones para un usuario (por ejemplo, Usuario1)
usuario = plataforma.buscar_usuario("Carlos")
if usuario:
    recomendaciones = plataforma.recomendar_contenido(usuario)
    print("\nRecomendaciones para Carlos:")
    for contenido in recomendaciones:
        print(contenido)

# Mostrar contenido popular
plataforma.mostrar_contenido_popular()
