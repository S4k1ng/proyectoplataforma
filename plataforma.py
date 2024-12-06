from arbol_binario import ABB
from contenido import Contenido
from usuario import Usuario
from arbol_general import CatalogoGeneral,NodoGeneral
from grafo import GrafoContenido

class Plataforma:
    def __init__(self):
        self.usuarios = ABB() 
        self.catalogo_popularidad = ABB()
        self.catalogo_general = CatalogoGeneral()
        self.grafo_contenido = GrafoContenido() 


    #Usuario
    def agregar_usuario(self, usuario):
        if self.usuarios.buscar(self.usuarios.raiz, usuario):
            print(f"Usuario {usuario.nombre} ya está registrado.")
        else:
            self.usuarios.insertar(usuario)
            print(f"Usuario {usuario.nombre} agregado al sistema.")

    def buscar_usuario(self, nombre):
        def _buscar_por_nombre(nodo, nombre):
            if nodo is None:
                return None
            if nodo.valor.nombre == nombre:
                return nodo.valor
            elif nombre < nodo.valor.nombre:
                return _buscar_por_nombre(nodo.izq, nombre)
            else:
                return _buscar_por_nombre(nodo.der, nombre)

        return _buscar_por_nombre(self.usuarios.raiz, nombre)

    def mostrar_historial_usuario(self, usuario_nombre):
        usuario = self.buscar_usuario(usuario_nombre)  
        if usuario:
            historial = usuario.historial_de_visualizacion 
            return [str(contenido) for contenido in historial]
        return "Usuario no encontrado."



    #Contenido
    def agregar_pelicula(self, titulo, duracion, genero):
        pelicula = NodoGeneral(titulo, "película", duracion, genero)
        self.catalogo_general.agregar_pelicula(pelicula)
        self.grafo_contenido.agregar_nodo(pelicula) 
        print(f"Película '{titulo}' agregada al catálogo.")

    def agregar_serie(self, titulo, genero, temporada=None, episodio=None):
        serie = NodoGeneral(titulo, "serie", genero=genero)
        temporada_nodo = NodoGeneral(temporada, "temporada") if temporada else None
        episodio_nodo = NodoGeneral(episodio, "episodio") if episodio else None

        self.catalogo_general.agregar_serie(serie, temporada_nodo, episodio_nodo)
        self.grafo_contenido.agregar_nodo(serie)
        print(f"Serie '{titulo}' agregada con temporada '{temporada}' y episodio '{episodio}'.")

    def mostrar_catalogo(self):
        print("Catálogo de contenido:")
        self.catalogo_general.mostrar_catalogo()
       
    #Uso recursivo   
    def recomendar_contenido(self, usuario, nodo=None):
        if nodo is None:
            nodo = self.catalogo_general.raiz 

        recomendaciones = []

        if nodo.tipo in ["película", "serie"] and nodo.genero in usuario.preferencias:
            if nodo not in usuario.historial_de_visualizacion:
                recomendaciones.append(nodo)

        for hijo in nodo.hijos:
            recomendaciones.extend(self.recomendar_contenido(usuario, hijo))

        return recomendaciones


    #Grafo
    def construir_grafo(self):
        contenidos = [nodo for categoria in self.catalogo_general.raiz.hijos for nodo in categoria.hijos]
        for i, contenido1 in enumerate(contenidos):
            for contenido2 in contenidos[i + 1:]:
                if set(contenido1.genero).intersection(contenido2.genero):
                    self.grafo_contenido.agregar_arista(contenido1.titulo, contenido2.titulo, 1)

        def recorrer_y_relacionar(nodo):
            if nodo is None:
                return
            usuario = nodo.valor
            historial = usuario.historial_de_visualizacion
            for i, contenido1 in enumerate(historial):
                for contenido2 in historial[i + 1:]:
                    self.grafo_contenido.agregar_arista(contenido1.titulo, contenido2.titulo, 1)
            recorrer_y_relacionar(nodo.izq)
            recorrer_y_relacionar(nodo.der)

        recorrer_y_relacionar(self.usuarios.raiz)

    def recomendar_contenido_grafo(self, titulo_visto, limite=5):
        return self.grafo_contenido.recomendar_contenido_grafo(titulo_visto, limite)



    #Buscar contendio por popularidad con el ABB
    def buscar_contenido_popular(self, popularidad):
        return self.catalogo_general.buscar(self.catalogo_general.raiz, popularidad)

    def mostrar_contenido_popular (self):
        popularidad = self.catalogo_popularidad.en_orden(self.catalogo_popularidad.raiz)
        if popularidad:
            print("Contenido popular: ")
            print(" | ".join(map(str, popularidad)))
        else:
            print("No hay contenidos populares disponibles.")