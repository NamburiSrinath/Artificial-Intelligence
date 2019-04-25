from queue import PriorityQueue


def search(graph, start, end):
    queue = PriorityQueue()
    queue.put((heuristic[start], [start]))
    print("Heuristic start is " + str(heuristic[start]) + " " + str([start]))

    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        print("node is " + str(node[1]))
        print("current is " + str(current))

        if end in node[1]:
            print("Path found: " + str(node[1]) + " with total distance = " + str(node[0]))
            break

        cost = node[0] - heuristic[current]
        print("cost = " +str(cost), "node[0] is = " + str(node[0]), "current heuristics " +str(heuristic[current]), "current node " + str(current))
        for neighbor in graph[current]:
            print("neighbour is " + str(neighbor))
            temp = node[1][:]
            print("temp is " + str(temp))
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor] + heuristic[neighbor], temp))


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
