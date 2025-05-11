import bench_marking as bm;
from sort_methods import sortingMethods
import matplotlib.pyplot as plt
import random
from datetime import datetime


#Este es el metodo para crear un arreglo
def build_arreglo(arreglo, nuevo_tamano):
    arreglon = arreglo.copy()
    tam_actual = len(arreglo)
    for _ in range(nuevo_tamano - tam_actual):
        numero = random.randrange(0, 99999)
        arreglon.append(numero)
    return arreglon

if __name__ == "__main__":
    bench = bm.Benchmarking()
    sortingM = sortingMethods
    
    #Tamaños:
    tamanos = [5_000, 10_000, 30_000, 50_000]
    max_tamano = 100_000

    #Se almacenan los resultados
    resultados = []

    #Arreglo vacio
    arreglo_base= []

    for tam in tamanos:
        arreglo_base = build_arreglo(arreglo_base, tam)
        
        algoritmos =  {
            "Burbuja":sortingM.sort_burbble,
            "Burbuja_mejorado":sortingM.sort_bubble_optimized,
            "Metodo_insercion":sortingM.sort_insertion,
            "Seleccion":sortingM.sort_selection,
            "Shell":sortingM.sort_shell,
        }

        for nombre, fun_metodo in algoritmos.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)






