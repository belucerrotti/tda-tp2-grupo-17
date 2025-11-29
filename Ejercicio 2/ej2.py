import networkx as nx


def enviar_archivo_por_la_red(grafo_original, tam_archivo):
    G = nx.DiGraph()
    nodos = set()

    # orientamos las aristas del grafo original
    for u, v, cap in grafo_original:
        a, b = sorted((u, v))
        G.add_edge(a, b, capacity=cap)
        nodos.add(a)
        nodos.add(b)

    # agregamos fuente y sumidero 
    
    nodo_min = min(nodos)
    nodo_max = max(nodos)
    S = "S"
    T = "T"
    G.add_node(S)
    G.add_node(T)
    G.add_edge(S, nodo_min, capacity=tam_archivo)
    G.add_edge(nodo_max, T, capacity=tam_archivo)

    # calculamos el flujo máximo y grafo residual
    flujo_maximo, flow_dict = nx.maximum_flow(
        G,
        S,
        T,
        flow_func=nx.algorithms.flow.edmonds_karp
    )

    fragmentacion = []

    for (u, v, _) in grafo_original:
        a, b = sorted((u, v))
        flujo_usado = flow_dict.get(a, {}).get(b, 0)
        if flujo_usado > 0:
            fragmentacion.append((a, b, flujo_usado))


    return flujo_maximo, fragmentacion


if __name__ == "__main__":
    # grafo de ejemplo del punto 1
    grafo = [
        (1, 2, 5),
        (1, 3, 5),
        (2, 6, 4),
        (2, 5, 2),
        (2, 9, 2),
        (3, 4, 3),
        (3, 5, 3),
        (3, 7, 2),
        (4, 7, 1),
        (4, 8, 4),
        (5, 7, 2),
        (6, 9, 3),
        (7, 10, 4),
        (8, 10, 3),
        (9, 10, 3),
    ]

    tam_archivo = 10  

    flujo_max, fragmentos = enviar_archivo_por_la_red(grafo, tam_archivo)

    for u, v, mb in fragmentos:
        print(f"Nodo {u} --> Nodo {v} [{mb} MB]")
    print(f"Flujo máximo: {flujo_max} MB")
    
