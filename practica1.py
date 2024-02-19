import heapq

def dijkstra(graph, start):
    # Inicializar las distancias a infinito para todos los nodos excepto el nodo de inicio
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # La distancia al nodo de inicio es 0

    # Usar una cola de prioridad (heap) para almacenar nodos y sus distancias
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Verificar si hay una distancia más corta a través del nodo actual
        if current_distance > distances[current_node]:
            continue

        # Explorar nodos vecinos
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Actualizar la distancia si se encuentra un camino más corto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print(f"Distancias más cortas desde el nodo {start_node}:")
for node, distance in shortest_distances.items():
    print(f"A {node}: {distance}")
