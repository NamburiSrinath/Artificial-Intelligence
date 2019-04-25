from collections import defaultdict 
class Graph: 
  
   
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
    	#print("length = " + str(len(self.graph)))
        #visited = [False] * (len(self.graph)) 
        visited = [False] * (a+1)
        queue = []
        queue.append(s) 
        visited[s] = True
        while queue: 
            s = queue.pop(0) 
            print(s) 
            for i in self.graph[s]: 
            	#print("i = " + str(i))
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
  
g = Graph() 
a = input("Enter number of vertices")
l = input("Enter number of links")
for i in range(l):
	x = input("Enter source")
	y = input("Enter destination")
	g.addEdge(x,y) 

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(1) 
  
