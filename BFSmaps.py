def bfs(graph, start, goal):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


small_graph = {
    'Chittor': ['Kurnool', 'Nellore'],
    'Hyderabad': ['Khammam', 'Kurnool'],
    'Khammam': ['Hyderabad', 'Rajamundry'],
    'Kurnool': ['Chittor', 'Hyderabad'],
    'Nellore': ['Chittor', 'Vijayawada'],
    'Rajamundry': ['Khammam', 'Vijayawada', 'Vizag'],
    'Vijayawada': ['Nellore', 'Rajamundry'],
    'Vizag': ['Rajamundry']
}
bfs(small_graph, 'Hyderabad', 'Vijayawada')
