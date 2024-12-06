from contenido import Contenido

class NodoGeneral(Contenido):
    def __init__(self, titulo, tipo, duracion=0, genero="", popularidad=0):
        super().__init__(titulo, tipo, duracion, genero)
        self.hijos = []  # Lista de nodos hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self, nivel=0):
        representacion = "  " * nivel + f"- {self.titulo} ({self.tipo})\n"
        for hijo in self.hijos:
            representacion += hijo.__str__(nivel + 1)
        return representacion


class CatalogoGeneral:
    def __init__(self):
        self.raiz = NodoGeneral("Catálogo", "raíz")

    def agregar_pelicula(self, contenido):
        peliculas = self._buscar_o_crear_categoria("Películas")
        peliculas.agregar_hijo(contenido)

    def agregar_serie(self, serie, temporada=None, episodio=None):
        series = self._buscar_o_crear_categoria("Series")
        serie_nodo = self._buscar_o_crear_hijo(series, serie.titulo, serie)

        if temporada:
            temporada_nodo = self._buscar_o_crear_hijo(serie_nodo, temporada.titulo, temporada)
            if episodio:
                temporada_nodo.agregar_hijo(episodio)

    def _buscar_o_crear_categoria(self, categoria_nombre):
        for hijo in self.raiz.hijos:
            if hijo.titulo == categoria_nombre:
                return hijo
        nueva_categoria = NodoGeneral(categoria_nombre, "categoría")
        self.raiz.agregar_hijo(nueva_categoria)
        return nueva_categoria

    def _buscar_o_crear_hijo(self, nodo_padre, nombre_hijo, nodo_contenido):
        for hijo in nodo_padre.hijos:
            if hijo.titulo == nombre_hijo:
                return hijo
        nodo_padre.agregar_hijo(nodo_contenido)
        return nodo_contenido

    def mostrar_catalogo(self):
        print(self.raiz)