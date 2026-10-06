# Taller 3: Algoritmos Genéticos
**Nombre:** Juan Felipe Pinzón Rincón

## Análisis de los Ejercicios Seleccionados

### 1. Maximización de la función continua
* El algoritmo genético se implementó como una técnica de optimización por búsqueda estocástica, la cual es ideal para funciones trigonométricas con múltiples picos donde los métodos analíticos tradicionales pueden fallar.
* Cada solución posible (el valor de $x$ entre 0 y 1) se codifica en la estructura de un cromosoma y es evaluada por la función objetivo para determinar su aptitud.
* Mediante operadores de cruce y mutación, el algoritmo explora el espacio de soluciones evitando quedar atrapado en óptimos locales, garantizando así la convergencia hacia el máximo global.

### 2. Verdadera Democracia (Distribución de Poder)
* Este escenario se modeló como un problema de optimización combinatoria, compartiendo características algorítmicas con el clásico problema de la mochila.
* El cromosoma se diseñó como un arreglo de 50 posiciones donde cada gen representa una entidad estatal, y su valor indica el partido político asignado.
* La función de aptitud busca minimizar la diferencia (error cuadrático) entre el poder político ideal basado en curules y el poder real asignado. Esto actúa como una penalidad moderada que guía a la población hacia una distribución equitativa.

### 3. Despacho Óptimo de Energía (Problema de Transporte)
* Se resolvió un problema complejo para satisfacer las restricciones operativas de una red eléctrica, minimizando simultáneamente los costos de transporte y generación.
* La codificación del individuo es una matriz de flujos bidimensional que dictamina la cantidad de energía enviada desde cada planta a cada ciudad.
* Dado que las plantas tienen un límite estricto de generación y las ciudades una demanda fija, la función de aptitud emplea un método de "Alta Penalidad", reduciendo drásticamente la calificación de cualquier solución infractora. Esto asegura que las generaciones finales estén dominadas únicamente por respuestas operativamente viables y económicas.
