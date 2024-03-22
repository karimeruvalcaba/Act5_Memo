# Juego de Memoria de Coches

Este es un juego de memoria simple implementado en Python utilizando la biblioteca turtle y algunas funciones auxiliares. El objetivo del juego es encontrar todos los pares de fichas idénticas ocultas en la cuadrícula.
## Cómo jugar

    1. Haz clic en dos fichas para revelarlas.
    2. Si las fichas coinciden, permanecerán visibles.
    3. Si no coinciden, se volverán a ocultar después de un breve momento.
    4. El juego termina cuando todas las fichas se han revelado.

## Ejecución del código

Para ejecutar el código, asegúrate de tener Python instalado en tu sistema y las bibliotecas necesarias (turtle y freegames). Luego, simplemente ejecuta el script en tu entorno Python preferido.

```
python nombre_del_archivo.py
```

## Acerca del Código

El código está estructurado de la siguiente manera:

    1. Variables globales: Se definen las variables globales necesarias para el estado del juego, como las imágenes de las fichas, la lista de fichas, el estado de visibilidad de las fichas, etc.

    2. Funciones de ayuda: Se definen varias funciones de ayuda para dibujar el tablero, manejar los eventos de clic, convertir coordenadas, etc.

    3. Función principal (draw): Esta función se encarga de dibujar el tablero de juego, las fichas y la imagen del coche. También maneja la lógica del juego, como verificar si se han revelado todas las fichas.

    4. Configuración de la ventana y ejecución del juego: Aquí se configura la ventana de la tortuga, se oculta la tortuga, se configura el bucle principal del juego y se inicia el bucle.

¡Diviértete jugando!
