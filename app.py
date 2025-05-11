import bench_marking as bm
from sort_methods import sortingMethods
import matplotlib.pyplot as plt
import random
from datetime import datetime

def build_arreglo(arreglo, nuevo_tamano):
    arreglon = arreglo.copy()
    tam_actual = len(arreglo)
    for _ in range(nuevo_tamano - tam_actual):
        numero = random.randrange(0, 99999)
        arreglon.append(numero)
    return arreglon

if __name__ == "__main__":
    bench = bm.Benchmarking()
    sortingM = sortingMethods()

    tamanos = [5_000, 10_000, 30_000, 50_000]
    max_tamano = 100_000
    arreglo_base = []

    algoritmos = {
        "Burbuja": sortingM.sort_burbble,
        "Buebja mejorado": sortingM.sort_bubble_optimized,
        "Seleccion": sortingM.sort_selection,
        "Shell": sortingM.sort_shell,
    }

    resultados_tamanos = []
    resultados_max = []

    for tam in tamanos:
        arreglo_base = build_arreglo(arreglo_base, tam)
        for nombre, fun_metodo in algoritmos.items():
            tiempo = bench.medir_tiempo(fun_metodo, arreglo_base)
            resultados_tamanos.append((tam, nombre, tiempo))

    arreglo_base = build_arreglo(arreglo_base, max_tamano)
    for nombre, fun_metodo in algoritmos.items():
        tiempo = bench.medir_tiempo(fun_metodo, arreglo_base)
        resultados_max.append((max_tamano, nombre, tiempo))

    resultados_por_algoritmo = {}
    for tam, nombre, tiempo in resultados_tamanos:
        if nombre not in resultados_por_algoritmo:
            resultados_por_algoritmo[nombre] = {"tamanos": [], "tiempos": []}
        resultados_por_algoritmo[nombre]["tamanos"].append(tam)
        resultados_por_algoritmo[nombre]["tiempos"].append(tiempo)

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.canvas.manager.set_window_title(f"Pablo Escandón - Mateo Namicela - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    for nombre, datos in resultados_por_algoritmo.items():
        axs[0].plot(datos["tamanos"], datos["tiempos"], marker='o', label=nombre)
    axs[0].set_title("Tiempos por Tamaños de Arreglos")
    axs[0].set_xlabel("Tamaño del Arreglo")
    axs[0].set_ylabel("Tiempo de Ejecución (s)")
    axs[0].legend()
    axs[0].grid(True)

    for nombre in algoritmos.keys():
        tiempos = [tiempo for tam, nom, tiempo in resultados_max if nom == nombre]
        axs[1].plot([max_tamano], tiempos, marker='o', label=nombre)
    axs[1].set_title(f"Tiempos con arreglo de tamaño {max_tamano}")
    axs[1].set_xlabel("Tamaño del Arreglo")
    axs[1].set_ylabel("Tiempo de Ejecución (s)")
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()
