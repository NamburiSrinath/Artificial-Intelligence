from queue import PriorityQueue
def search(graph, start, end):
    queue = PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        print(node)
        if end in node[1]:
            print("\n Path found: " + str(node[1]) + " with total distace = " + str(node[0]))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))


graph = {
    'Chittor': {'Kurnool': 366 , 'Nellore': 207},
    'Hyderabad': {'Khammam': 188, 'Kurnool': 212},
    'Khammam': {'Hyderabad': 188, 'Rajamundry': 244},
    'Kurnool': {'Chittor': 366, 'Hyderabad': 212},
    'Nellore': {'Chittor': 207, 'Vijayawada': 281},
    'Rajamundry': {'Khammam': 244, 'Vijayawada': 162, 'Vizag': 190},
    'Vijayawada': {'Nellore': 281, 'Rajamundry': 162},
    'Vizag': {'Rajamundry': 190}
}
search(graph, 'Hyderabad', 'Vijayawada')
