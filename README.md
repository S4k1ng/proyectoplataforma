# proyectoplataforma

1) **Creo la clase Usuario**: le paso los parametros (nombre, fecha_nacimiento, preferencias, historial_de_visualizacion)
   - Uso datetime para averiguar la edad con la fecha de nacimiento
   - Uso una lista vacia para el historial
   - definimos una funcion para sumar contenido al historial y que se aumente la popularidad del contenido

     
2) **Creo la clase Contenido**: le paso sus parametros (titulo, tipo, duracion, genero, popularidad)
  - iniciamos la popularidad en 0 y definimos una funcion para aumentar su popularida

    
3) **Creo la clase Plataforma**: le inicio una lista vacia a "usuarios" y "contenidos" para almacenar los datos
  - Defino una funcion para agregar un usuario a la lista
  - Defino una funcion para agregar contenido a la lista
  - Defino una funcion para mostrar el contenido
    - Recorro la lista con un for para que me muestre los contenidos
  - Defino una funcion para buscar contenido por genero
    - Recorro la lista con un for y filtro solo aquellos objetos cuyo atributo genero coincide con el argumento genero.
  - Defino una funcion para mostrar el historial del usuario
    - Usando la funcion next() nos busca el usuario (en caso de no encontrar, nos devuelve el valor none), luego retornamos su lista de historial

   
4) Creo un algoritmo recursivo para recomendar el contenido segun las preferencias del usuario
   - Defino una funcion que recorre recursivamente la lista de contenidos tomando de argumento al usuario
     - Si el indice supera el limite de contenidos retornara una lista vacia (indicando que ya recorrio toda la lista del contenido)
     - Si el contenido no esta en la lista del historial y coincide con las preferencias, lo agregará a recomendaciones
     - despues de evaluar un contenido hacemos que la funcion se llame nuevamente, asi permite que el algoritmo siga evaluando todos los contenido
    
5) Instalo desde pypi "arbolbinariobusqueda" y lo agrego en un archivo "arboles.py" para tenerlo a la vista
   - importo el ABB en la plataforma y creo funciones para poder buscar y ordenar el contenido por popularidad
  

  
  
