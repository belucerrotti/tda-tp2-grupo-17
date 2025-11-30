import pulp

def imprimir_resultados(modelo, flujo, rutas):
    print(f"Estado: {pulp.LpStatus[modelo.status]}")
    print(f"Enlaces totales usados: {pulp.value(modelo.objective)}")
    print("-" * 30)
    for (i, j) in rutas:
        cantidad = pulp.value(flujo[(i, j)])
        if cantidad > 0:
            print(f"Nodo {i} -> Nodo {j}: {cantidad} MB")

def encontrar_ruta_optima(capacidades, nodos, origen, destino, total_archivo):
    modelo = pulp.LpProblem("Ruta_Optima", pulp.LpMinimize)

    rutas = capacidades.keys()
    flujo = pulp.LpVariable.dicts("MB", rutas, lowBound=0, cat='Continuous')
    activo = pulp.LpVariable.dicts("Uso", rutas, cat='Binary')

    modelo += pulp.lpSum(activo)

    for (i, j) in rutas:
        modelo += flujo[(i, j)] <= capacidades[(i, j)] * activo[(i, j)]

    for nodo in nodos:
        entra = pulp.lpSum(flujo[(i, j)] for (i, j) in rutas if j == nodo)
        sale = pulp.lpSum(flujo[(i, j)] for (i, j) in rutas if i == nodo)

        if nodo == origen:
            modelo += (sale - entra == total_archivo)
        elif nodo == destino:
            modelo += (entra - sale == total_archivo)
        else:
            modelo += (entra == sale)

    modelo.solve()
    return modelo, flujo, rutas


def main():

    capacidades = {
        (1, 2): 5, (1, 3): 5,
        (2, 6): 4, (2, 5): 2, (2, 9): 2,
        (3, 5): 3, (3, 7): 2, (3, 4): 3,
        (4, 7): 1, (4, 8): 4,
        (5, 7): 2,
        (6, 9): 3,
        (7, 10): 4, 
        (8, 10): 3, 
        (9, 10): 3
    }

    nodos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    origen = 1
    destino = 10
    total_archivo = 10

    modelo, flujo, rutas = encontrar_ruta_optima(capacidades, nodos, origen, destino, total_archivo)
    imprimir_resultados(modelo, flujo, rutas)
    
    return 0

main()