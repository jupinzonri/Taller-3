"""
Taller_3_IA.py
Implementación de 3 ejercicios usando Algoritmos Genéticos (AGs) y librerías científicas.
"""

import numpy as np
from scipy.optimize import differential_evolution

# =====================================================================
# EJERCICIO 1: Maximización de función matemática continua
# =====================================================================
def ejercicio_1_maximizacion():
    """
    Maximizar f(x) = x * sin(10 * pi * x) + 1 en el intervalo [0, 1].
    Se utiliza Evolución Diferencial (un tipo de AG continuo de SciPy).
    """
    print("--- EJERCICIO 1: MAXIMIZACIÓN ---")
    
    # SciPy minimiza por defecto, por lo que invertimos el signo de la función
    def funcion_aptitud(x):
        return -(x[0] * np.sin(10 * np.pi * x[0]) + 1)
    
    limites = [(0, 1)]
    resultado = differential_evolution(funcion_aptitud, limites, popsize=50, maxiter=100)
    
    x_optimo = resultado.x[0]
    maximo_encontrado = -resultado.fun
    
    print(f"Mejor cromosoma (x): {x_optimo:.4f}")
    print(f"Aptitud máxima f(x): {maximo_encontrado:.4f}\n")


# =====================================================================
# EJERCICIO 2: Verdadera Democracia (Distribución de Poder)
# =====================================================================
def ejercicio_2_democracia():
    """
    Distribuir 50 entidades estatales entre 5 partidos políticos.
    Basado en los operadores estándar de AG: Selección, Cruce y Mutación.
    """
    print("--- EJERCICIO 2: DEMOCRACIA ---")
    np.random.seed(42)
    
    num_partidos = 5
    num_entidades = 50
    
    # Generar curules aleatorias que sumen 50
    curules_brutas = np.random.randint(1, 20, size=num_partidos)
    curules = (curules_brutas / curules_brutas.sum() * 50).astype(int)
    curules[-1] = 50 - curules[:-1].sum() # Ajuste de redondeo
    proporcion_ideal = curules / 50.0
    
    # Pesos de las 50 entidades (1 a 100)
    poder_entidades = np.random.randint(1, 101, size=num_entidades)
    poder_total = poder_entidades.sum()
    poder_ideal_partidos = proporcion_ideal * poder_total
    
    # Parámetros del AG
    tamano_pob = 100
    generaciones = 200
    prob_mutacion = 0.1
    
    # Inicialización aleatoria (cada gen es el ID del partido al que va la entidad)
    poblacion = np.random.randint(0, num_partidos, size=(tamano_pob, num_entidades))
    
    def evaluar_aptitud(cromosoma):
        poder_real = np.zeros(num_partidos)
        for i, partido in enumerate(cromosoma):
            poder_real[partido] += poder_entidades[i]
        # Minimizar el error cuadrático medio (penalidad por alejarse del ideal)
        error = np.sum((poder_real - poder_ideal_partidos)**2)
        return 100000 / (1 + error) # Transformar minimización de error a maximización de aptitud
    
    for gen in range(generaciones):
        aptitudes = np.array([evaluar_aptitud(ind) for ind in poblacion])
        
        # Selección (Elitismo simple + Ruleta)
        probabilidades = aptitudes / aptitudes.sum()
        indices_seleccionados = np.random.choice(tamano_pob, size=tamano_pob, p=probabilidades)
        padres = poblacion[indices_seleccionados]
        
        # Cruce (1 punto)
        hijos = np.empty_like(padres)
        for i in range(0, tamano_pob, 2):
            punto = np.random.randint(1, num_entidades - 1)
            hijos[i] = np.concatenate([padres[i][:punto], padres[i+1][punto:]])
            if i+1 < tamano_pob:
                hijos[i+1] = np.concatenate([padres[i+1][:punto], padres[i][punto:]])
                
        # Mutación
        mascara_mutacion = np.random.rand(tamano_pob, num_entidades) < prob_mutacion
        mutaciones = np.random.randint(0, num_partidos, size=(tamano_pob, num_entidades))
        hijos = np.where(mascara_mutacion, mutaciones, hijos)
        
        poblacion = hijos

    aptitudes_finales = np.array([evaluar_aptitud(ind) for ind in poblacion])
    mejor_ind = poblacion[np.argmax(aptitudes_finales)]
    
    poder_final = np.zeros(num_partidos)
    for i, partido in enumerate(mejor_ind):
        poder_final[partido] += poder_entidades[i]
        
    print(f"Curules asignadas por partido: {curules}")
    print(f"Poder ideal objetivo: {poder_ideal_partidos.astype(int)}")
    print(f"Poder real alcanzado por AG: {poder_final.astype(int)}\n")


# =====================================================================
# EJERCICIO 3: Despacho de Energía
# =====================================================================
def ejercicio_3_energia():
    """
    Minimización de costos (generación + transporte) mediante un AG matricial,
    aplicando 'Alta Penalidad' para el manejo de restricciones operativas.
    """
    print("--- EJERCICIO 3: DESPACHO DE ENERGÍA ---")
    
    capacidades = np.array([3, 6, 5, 4]) # Plantas: C, B, M, Ba
    demandas = np.array([4, 3, 5, 3])    # Ciudades: Cali, Bogota, Medellin, Barranquilla
    costos_gen = np.array([680, 720, 660, 750]).reshape(4, 1)
    costos_trans = np.array([
        [1, 4, 3, 6],
        [4, 1, 4, 5],
        [3, 4, 1, 4],
        [6, 5, 4, 1]
    ])
    costo_total_matriz = costos_gen + costos_trans
    
    # Parámetros del AG
    tamano_pob = 300
    generaciones = 300
    prob_mutacion = 0.15
    
    # Cada genoma es una matriz 4x4 de flujos (valores reales entre 0 y 5 GW)
    poblacion = np.random.rand(tamano_pob, 4, 4) * 5 
    
    def aptitud_energia(matriz_flujo):
        costo_operativo = np.sum(matriz_flujo * costo_total_matriz)
        
        # Penalidad por restricciones (Alta Penalidad)
        exceso_generacion = np.maximum(0, np.sum(matriz_flujo, axis=1) - capacidades)
        falla_demanda = np.abs(np.sum(matriz_flujo, axis=0) - demandas)
        
        penalidad = np.sum(exceso_generacion) * 50000 + np.sum(falla_demanda) * 50000
        
        # Aptitud es inversa al costo total (a menor costo + penalidad, mayor aptitud)
        return 1.0 / (costo_operativo + penalidad + 1e-6)

    for gen in range(generaciones):
        aptitudes = np.array([aptitud_energia(ind) for ind in poblacion])
        probabilidades = aptitudes / aptitudes.sum()
        
        # Selección por Ruleta
        indices = np.random.choice(tamano_pob, size=tamano_pob, p=probabilidades)
        padres = poblacion[indices]
        
        # Cruce Aritmético (ideal para matrices de reales)
        hijos = np.empty_like(padres)
        for i in range(0, tamano_pob, 2):
            alpha = np.random.rand()
            hijos[i] = alpha * padres[i] + (1 - alpha) * padres[i+1]
            if i+1 < tamano_pob:
                hijos[i+1] = (1 - alpha) * padres[i] + alpha * padres[i+1]
                
        # Mutación
        mascara = np.random.rand(tamano_pob, 4, 4) < prob_mutacion
        variacion = np.random.randn(tamano_pob, 4, 4) * 0.5
        hijos = np.clip(hijos + mascara * variacion, 0, None) # Evitar flujos negativos
        
        poblacion = hijos

    aptitudes_finales = np.array([aptitud_energia(ind) for ind in poblacion])
    mejor_matriz = poblacion[np.argmax(aptitudes_finales)]
    costo_final = np.sum(mejor_matriz * costo_total_matriz)
    
    print(f"Matriz de despacho óptimo encontrada (GW):\n{np.round(mejor_matriz, 2)}")
    print(f"Generación por planta (Max {capacidades}): {np.round(np.sum(mejor_matriz, axis=1), 2)}")
    print(f"Demanda cubierta (Meta {demandas}): {np.round(np.sum(mejor_matriz, axis=0), 2)}")
    print(f"Costo Mínimo Estimado: ${costo_final:,.2f}")

# Ejecución de los scripts
if __name__ == "__main__":
    ejercicio_1_maximizacion()
    ejercicio_2_democracia()
    ejercicio_3_energia()
"""
