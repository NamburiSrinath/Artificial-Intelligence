from queue import PriorityQueue


def search(graph, start, end):
    queue = PriorityQueue()
    queue.put((0, [start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]

        if end in node[1]:
            print("Path found: " + str(node[1][0]), end=" ")
            tcost = 0
            for i in range(0, (len(node[1]) - 1)):
                print("--> " + str(node[1][i + 1]), end=" ")
                tcost = tcost + graph[node[1][i]][node[1][i + 1]]
            print("\nPath Cost:" + str(tcost))
            break

        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((heuristic[neighbor], temp))


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

heuristic = {
    'Chittor' : 402,
    'Hyderabad' : 250,
    'Khammam': 99,
    'Kurnool' : 288,
    'Nellore' : 242,
    'Rajamundry' : 135,
    'Vijayawada' : 0,
    'Vizag' : 303
}
search(graph, 'Hyderabad', 'Vijayawada')
