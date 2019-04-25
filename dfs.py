from collections import defaultdict 
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def DFSUtil(self,v,visited): 
        visited[v]= True
        print v, 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 

    def DFS(self,v): 
        #visited = [False]*(len(self.graph)) 
        visited = [False]*(a+1)
        self.DFSUtil(v,visited) 


g = Graph() 
a = input("Enter number of vertices")
l = input("Enter number of links")
for i in range(l):
    x = input("Enter source")
    y = input("Enter destination")
    g.addEdge(x,y) 
  
print "Following is DFS from (starting from vertex 2)"
g.DFS(1) 
  
