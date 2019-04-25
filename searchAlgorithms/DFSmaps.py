def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


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
dfs(small_graph, 'Hyderabad', 'Vijayawada')
