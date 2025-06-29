import time
import random

# Algoritmo con bucles anidados: compara cada elemento del formulario con cada ID registrado
def id_duplicado_bucles_anidados(ids_registrados, ids_formulario):
    for id1 in ids_registrados:             
        for id2 in ids_formulario:             
            if id1 == id2:                    # Se ejecuta n x m veces
                return True
    return False
# Complejidad total: O(n*m) -> convirtiendose en el peor de los casos a O(n^2)

# Algoritmo con dict: convierte la lista de registrados en un diccionario para verificar duplicados
def id_duplicado_dict(ids_registrados, ids_formulario):
    registrados_dict = {}                      
    for id in ids_registrados:                # O(n)
        registrados_dict[id] = True           
    for id in ids_formulario:                 # O(m)
        if id in registrados_dict:            # O(1) ejecuta la búsqueda
            return True
    return False                            
# Complejidad total: O(n + m). Se reduce a O(n)

# Función auxiliar para medir el tiempo de ejecución de cada algoritmo
def medir_tiempo(funcion, lista1, lista2):
    inicio = time.time()
    resultado = funcion(lista1, lista2)
    fin = time.time()
    return resultado, fin - inicio

if __name__ == "__main__":
    # Generación de listas de prueba con IDs aleatorios de 6 dígitos
    n = 10000
    ids_registrados = [random.randint(100000, 999999) for _ in range(n)]
    ids_formulario = [random.randint(100000, 999999) for _ in range(n)]

    # Ejecución y medición del algoritmo lento (con posibles duplicados)
    resultado1, tiempo1 = medir_tiempo(id_duplicado_bucles_anidados, ids_registrados, ids_formulario)
    print(f"[Algoritmo bucles anidados] -- Hay duplicados?: {resultado1} -- Tiempo: {tiempo1:.6f} segundos")

    # Ejecución y medición del algoritmo rápido (con posibles duplicados)
    resultado2, tiempo2 = medir_tiempo(id_duplicado_dict, ids_registrados, ids_formulario)
    print(f"[Algoritmo con diccionario] -- Hay duplicados?: {resultado2} -- Tiempo: {tiempo2:.6f} segundos")

    # Generación de listas SIN duplicados para simular el peor caso
    ids_registrados = [random.randint(100000, 200000) for _ in range(n)]
    ids_formulario = [random.randint(300000, 400000) for _ in range(n)]     

    # Ejecución y medición del algoritmo lento (sin duplicados)
    resultado1, tiempo1 = medir_tiempo(id_duplicado_bucles_anidados, ids_registrados, ids_formulario)
    print(f"[Algoritmo bucles anidados] -- Hay duplicados?: {resultado1} -- Tiempo: {tiempo1:.6f} segundos")

    # Ejecución y medición del algoritmo rápido (sin duplicados)
    resultado2, tiempo2 = medir_tiempo(id_duplicado_dict, ids_registrados, ids_formulario)
    print(f"[Algoritmo con diccionario] -- Hay duplicados?: {resultado2} -- Tiempo: {tiempo2:.6f} segundos")