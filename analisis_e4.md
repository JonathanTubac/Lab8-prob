# Ejercicio 4 — Preguntas de Análisis
### MM3014 Teoría de Probabilidades — Lab 8 (Etapa 4)


## Pregunta 1
¿Cómo afecta la disminución de K al número esperado de sobres y a la probabilidad de éxito? ¿Es lineal la relación?

Disminuir K reduce significativamente el número esperado de sobres necesarios para completar el álbum y aumenta la probabilidad de éxito para cualquier M fijo. La dirección del efecto es clara: a menor K, menos sobres y mayor probabilidad. Sin embargo, la relación no es lineal. El salto más grande ocurre al pasar de no tener intercambio a tener cualquier forma de canje, donde incluso K = 10 ya reduce el promedio en más de la mitad. A partir de ahí, las mejoras son decrecientes y no siguen una escala proporcional al cambio en K. Esto refleja que la mayor ganancia proviene de la mera existencia del mecanismo, no necesariamente de su generosidad.


## Pregunta 2
Para K = 2, ¿cuántos sobres se ahorran en promedio respecto al caso sin intercambio? Exprese el ahorro en quetzales (Q 9.50 por sobre).

Con K = 2, el número promedio de sobres necesarios para completar el álbum pasa de 72.241 a 19.851, lo que representa un ahorro de aproximadamente 52.39 sobres. Al precio de Q 9.50 por sobre, este ahorro equivale a Q 497.71 por coleccionista que complete el álbum. Se trata de un ahorro sustancial que demuestra que incluso un mecanismo de intercambio moderado tiene un impacto económico relevante.


## Pregunta 3
Para M = 45, ¿cuánto aumenta la probabilidad al pasar de K = 10 a K = 5, y de K = 5 a K = 1?

Con M = 45 sobres, todos los valores de K evaluados alcanzan ya una probabilidad de éxito prácticamente igual a 1. El incremento al pasar de K = 10 a K = 5 es de apenas 0.0001, y al pasar de K = 5 a K = 1 el incremento es de 0.0000. Esto no significa que K no importe, sino que M = 45 es un punto donde todas las curvas ya convergieron al máximo. Las diferencias significativas entre valores de K se observan en valores de M más bajos, entre 20 y 35 sobres, donde las curvas aún no han saturado.


## Pregunta 4
¿Existe un K a partir del cual mejorar el intercambio produce muy poco beneficio adicional? Proponga una posible razón.

Sí. A partir de K = 2 la reducción marginal respecto a K = 1 es de apenas 6.72 puntos porcentuales en la reducción del número esperado de sobres. Con K = 1, el álbum exige el mínimo teórico posible, que es el valor de ceil(100 / 7) = 15 sobres, por lo que ningún mecanismo puede ir más allá de ese límite. La razón subyacente es que, una vez que K es suficientemente pequeño para eliminar casi todo el desperdicio de repetidas, el cuello de botella pasa a ser la variabilidad aleatoria del muestreo y no la acumulación de duplicados. El único límite restante es puramente combinatorio y no depende de K.


## Pregunta 5
¿Cuál es el costo efectivo por estampa nueva obtenida mediante canje? ¿Qué tasa K sería la más rentable?

Cada sobre cuesta Q 9.50 y entrega 7 estampas, por lo que cada estampa tiene un costo implícito de Q 1.357. Las estampas repetidas provienen de sobres ya comprados, así que su valor de oportunidad es ese mismo costo unitario. Para obtener una estampa nueva mediante canje se necesitan K repetidas, lo que equivale a un costo efectivo de K × Q 1.357. Para K = 1 el costo es Q 1.357, para K = 2 es Q 2.714, para K = 5 es Q 6.786 y para K = 10 es Q 13.571.

La tasa más rentable es K = 1, ya que el costo de obtener una estampa nueva por canje es igual al costo directo de obtenerla dentro de un sobre, aprovechando al máximo cada repetida. Con K mayor, el canje es siempre más caro por estampa nueva que simplemente comprar más sobres. En términos prácticos, K = 2 ofrece el mejor equilibrio entre rentabilidad y viabilidad, con un costo efectivo razonable y una reducción en sobres necesarios del 72.52%.
