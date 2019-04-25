#If the city is connected which is represented by 1st condition AND if it's color is same as connected color, then 
#we need to put in another color. So, return false so that if condition breaks in mapcoloring function
def is_safe(n, graph, colors, c): 
    for i in range(n): #This for loop checks whether the connected cities has the same color. If not, it returns true
        if graph[n][i] and c == colors[i]: 
            return False
    return True

def mapcoloring(graph,color_nb,colors, n):
    if n==6:
        return True
    #c takes the values 1,2,3 here and colors according to constraints. if it passes 'if' condition, that color will be there
    for c in range(1, color_nb+1):
        if is_safe(n, graph, colors, c):
            colors[n] = c
            if mapcoloring(graph, color_nb, colors, n+1):
              return True
            colors[n] = 0

#Name of the cities
vertex=["western australia","northernterritory","southaustralia","queensland","victoria","newsouth wale"]
vertex_nb=len(vertex)
#takes colors
color=input("enter colors:")
color=color.split()
color_nb =len(color)

colors = [0] * vertex_nb
graph = [[0,1,1,0,0,0],[1,0,1,1,0,0],[1,1,0,1,1,1],[0,1,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,1,0]]
if mapcoloring(graph, color_nb, colors, 0):
    for i in range(0,6):
      print ("Color of " + vertex[i],"is :",color[colors[i]-1])
else:
    print ("No solutions")