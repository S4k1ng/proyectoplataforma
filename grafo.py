from contenido import Contenido

class NodoContenido:
    def __init__(self, contenido):
        self.contenido = contenido  
        self.vecinos = {}

    def agregar_vecino(self, vecino, peso):
        if vecino not in self.vecinos:
            self.vecinos[vecino] = peso
        else:
            self.vecinos[vecino] += peso 


class GrafoContenido:
    def __init__(self):
        self.nodos = {} 

    def agregar_nodo(self, contenido):
        if contenido.titulo not in self.nodos:
            self.nodos[contenido.titulo] = NodoContenido(contenido)

    def agregar_arista(self, titulo1, titulo2, peso):
        if titulo1 in self.nodos and titulo2 in self.nodos:
            self.nodos[titulo1].agregar_vecino(self.nodos[titulo2], peso)
            self.nodos[titulo2].agregar_vecino(self.nodos[titulo1], peso)

    def mostrar_grafo(self):
        for titulo, nodo in self.nodos.items():
            vecinos = [f"{vecino.contenido.titulo} ({peso})" for vecino, peso in nodo.vecinos.items()]
            print(f"{titulo}: {', '.join(vecinos)}")

    def recomendar_contenido(self, titulo_visto, limite=5):
        if titulo_visto not in self.nodos:
            return f"El contenido '{titulo_visto}' no existe en el grafo."

        nodo_inicial = self.nodos[titulo_visto]
        recomendaciones = {}

        # Explorar vecinos del contenido visto
        for vecino, peso in nodo_inicial.vecinos.items():
            recomendaciones[vecino.contenido.titulo] = peso

        # Ordenar recomendaciones por peso
        recomendaciones_ordenadas = sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)

        # Retornar las recomendaciones más relevantes
        return [titulo for titulo, _ in recomendaciones_ordenadas[:limite]]
