 
from collections import defaultdict 
class Graph: 

	 
	def __init__(self): 

		
		self.graph = defaultdict(list)
		self.visited1=set()

	
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.visited=[] 

	
	def BFS(self, s): 

		
		queue = [] 

		queue.append(s) 
		self.visited.append(s) 

		while queue: 

			s = queue.pop(0) 
			print (s, end = " ") 
 
			for i in self.graph[s]: 
				if i not in self.visited: 
					queue.append(i) 
					self.visited.append(s) 
					
	def DFS(self, v):
		
		self.visited1.add(v)
		print(v,end=" ")
		for n in self.graph[v]:
			if n not in self.visited1:
				self.DFS(n)
	
		

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
print("BFS")
g.BFS(2) 
print()
print("DFS")
g.DFS(2)

