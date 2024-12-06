# proyectoplataforma

1) **Creo la clase Usuario**: le paso los parametros (nombre, fecha_nacimiento, preferencias, historial_de_visualizacion)
   - Uso datetime para averiguar la edad con la fecha de nacimiento (Agrego una validación de datos, para que cuando agreguen mal la fecha salte un msj y no un error)
   - Uso una lista vacia para el historial
   - definimos una funcion para sumar contenido al historial y que se aumente la popularidad del contenido
---
     
2) **Creo la clase Contenido**: le paso sus parametros (titulo, tipo, duracion, genero, popularidad)
  - iniciamos la popularidad en 0 y definimos una funcion para aumentar su popularida
---
    
3) **Creo la clase Plataforma**: le inicio una lista vacia a "usuarios" y "contenidos" para almacenar los datos
  - Defino una funcion para agregar un usuario a la lista
  - Defino una funcion para agregar contenido a la lista
  - Defino una funcion para mostrar el contenido
    - Recorro la lista con un for para que me muestre los contenidos
  - Defino una funcion para buscar contenido por genero
    - Recorro la lista con un for y filtro solo aquellos objetos cuyo atributo genero coincide con el argumento genero.
  - Defino una funcion para mostrar el historial del usuario
    - Usando la funcion next() nos busca el usuario (en caso de no encontrar, nos devuelve el valor none), luego retornamos su lista de historial
---
   
4) Creo un algoritmo recursivo para recomendar el contenido segun las preferencias del usuario
   - Defino una funcion que recorre recursivamente la lista de contenidos tomando de argumento al usuario
     - Si el indice supera el limite de contenidos retornara una lista vacia (indicando que ya recorrio toda la lista del contenido)
     - Si el contenido no esta en la lista del historial y coincide con las preferencias, lo agregará a recomendaciones
     - despues de evaluar un contenido hacemos que la funcion se llame nuevamente, asi permite que el algoritmo siga evaluando todos los contenido
---

5) Instalo desde pypi "arbolbinariobusqueda" y lo agrego en un archivo `arboles.py` para tenerlo a la vista
   - importo el ABB en la plataforma y creo funciones para poder buscar y ordenar el contenido por popularidad
   - Uso metodos de comparacion para los usuarios, de esta manera los puedo agregar al ABB
     - `__lt__` Compara usuarios basándose en el nombre.
     - `__eq__` Comprueba si dos usuarios tienen el mismo nombre.
   - Uso el método insertar para agregar un usuario.
   - Implemento un método para buscar usuarios por nombre.
      - Modifico la busqueda del historial, para que en vez de recorrer una lista con `next` utilice el ABB 
---

6) **Creo un `arbol_general`** para guardar peliculas y series (temporadas y capitulos) y le heredo los parametros de la clase `Contenido`
   - Aplico cambios a la busqueda de contenidos de manera tal que trabajen con el arbol y dejen de trabajar con la lista
   - Cambio la forma recursiva para que busque las recomendaciones desde la raiz del arbol general
---

7) **Creo `grafo.py`** donde cada nodo representa una pelicula o serie
   - Baso las similitudes de generos y visualizaciones de los usuarios para darle peso a los contenidos y asi generar recomendaciones
   - importo el `grafo.py` a la `Plataforma` y inicializo el grafo en el constructor
     - Añado una implementacion en `agregar_pelicula` y `agregar_serie` para añadir el contenido al grafo
   - Añado un método para construir las relaciones del grafo:
     - `construir_grafo` Relaciona nodos por género
     - `recorrer_y_relacionar` Relaciona nodos por historial de usuarios
   - Añado un metodo para recomendar contenido pero con el grafo 
  ---
8) **Creo `main.py`** en el cual creamos la plataforma y le pasamos datos reales de pelicualas, series y usuarios para poder trabajar y testear el codigo

  ---
  ___ 
  # Conclusión del proyecto:

En este proyecto, se diseñó y desarrolló una plataforma de streaming optimizada utilizando diversas estructuras de datos. A través de un Árboles (ABB y AG) y un Grafo, conseguimos organizar tanto los usuarios como el catálogo de contenidos y mejorar la generación de recomendaciones personalizadas.

## 1. El código está dividido en los siguientes archivos:

- **`plataforma.py`**: Controlador principal de la plataforma.
- **`usuario.py`**: Implementación de la clase Usuario.
- **`contenido.py`**: Definición de la clase base Contenido.
- **`arbol_binario.py`**: Implementación del ABB para gestión de usuarios y popularidad.
- **`arbol_general.py`**: Implementación del Árbol General para el catálogo.
- **`grafo.py`**: Implementación del Grafo para modelar relaciones entre contenidos.
- **`main.py`**: Archivo de prueba donde se ejecuta el flujo completo del sistema.

## 2. Estructura del arbol general:
El catálogo está estructurado jerárquicamente, con diferentes categorías como películas y series, cada una con sus respectivos contenidos. La organización se ve de la siguiente manera:
              
      Catálogo
     ├── Películas
     │   ├── Película1
     │   └── Película2
     └── Series
         └── Serie1
             └── Temporada1
                 └── Capítulo1

## 3. Estructura del arbol binario:
   - **Gestión de Usuarios**:
      Los usuarios están organizados mediante un Árbol Binario de Búsqueda (ABB), donde cada nodo representa un usuario y las relaciones se manejan de forma eficiente para permitir búsquedas rápidas y agregados de usuarios por su nombre.

                      [Luis]
                     /      \
                [Ana]      [Pedro]
                 /             \
           [Beatriz]          [Carlos]

     
   - **Popularidad de Películas**:
      Cada nodo representa una película, y el valor dentro del nodo es su popularidad. Las películas se organizan según la popularidad para hacer búsquedas y recomendaciones eficientes.

                            [Película (80)]
                          /                \
                 [Película (50)]        [Película (90)]
                  /          \                 \
           [Película (30)] [Película (60)]   [Película (100)]


## 4. Estructura del grafo:      
   La generación de recomendaciones se realiza utilizando un Grafo donde los nodos son los contenidos (películas y series) y las aristas representan similitudes entre ellos (basadas en género o preferencias de los usuarios). Los contenidos relacionados se exploran para hacer recomendaciones basadas en lo que otros usuarios con gustos similares han visto. La estructura del grafo es la siguiente:

                                 [Pelicula1]
                              /       |       \
                    [Pelicula2]   [Serie1] [Pelicula3]
                     /       \              /       \
              [Serie2]    [Pelicula4] [Serie3]   [Pelicula5]
                  |                                   |
              [Serie4]                           [Pelicula6]






