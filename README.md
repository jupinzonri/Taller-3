# Taller 3: Algoritmos Genéticos
**Nombre:** Juan Felipe Pinzón Rincón

## Análisis de los Ejercicios Seleccionados

### 1. Maximización de la función $f(x)=x \sin(10 \pi x)+1$
* El algoritmo genético opera como una técnica de optimización por búsqueda estocástica basada en los mecanismos de la selección natural, ideal para funciones con múltiples picos donde los métodos analíticos tradicionales pueden fallar[span_0](start_span)[span_0](end_span).
* Cada solución posible (valor de $x$ entre 0 y 1) se codifica en la estructura de un cromosoma, el cual es evaluado por la función de aptitud para determinar su capacidad de supervivencia[span_1](start_span)[span_1](end_span).
* Mediante operadores de cruce y una probabilidad de mutación, el algoritmo explora el espacio de soluciones evitando quedar atrapado en óptimos locales, garantizando la convergencia hacia el máximo global[span_2](start_span)[span_2](end_span).

### 2. Verdadera Democracia (Distribución de Poder)
* Este escenario se modela como un problema de optimización combinatoria tipo NP-Completo, compartiendo características fundamentales con el problema clásico de la mochila[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span).
* El cromosoma se diseña como un arreglo donde cada gen representa una de las 50 entidades, y su valor (alelo) indica el partido político asignado (0 a 4)[span_5](start_span)[span_5](end_span).
* La función de aptitud busca minimizar la diferencia entre el poder político ideal (basado en el porcentaje de curules aleatorias) y el poder real asignado. Se aplica un enfoque de minimización del error cuadrático, actuando como una penalidad moderada para guiar a la población hacia distribuciones equitativas[span_6](start_span)[span_6](end_span).

### 3. Despacho Óptimo de Energía (Problema de Transporte)
* Representa un problema complejo donde se requiere satisfacer las restricciones operativas de la red, minimizando simultáneamente los costos asociados al transporte y a la generación de energía[span_7](start_span)[span_7](end_span).
* La codificación del individuo es una matriz de flujos $4 \times 4$ que dictamina la cantidad de GW enviados desde cada planta a cada ciudad[span_8](start_span)[span_8](end_span).
* Dado que las plantas tienen un límite de generación y las ciudades una demanda estricta, la función de aptitud emplea el método de "Alta Penalidad", reduciendo drásticamente la aptitud de cualquier cromosoma infractor que exceda capacidades o no cubra demandas, asegurando que las generaciones futuras dominen con soluciones viables[span_9](start_span)[span_9](end_span).
