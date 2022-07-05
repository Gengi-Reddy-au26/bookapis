# # Create the dictionary with graph elements
# graph = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["e"],
#    "e" : ["d"]
# }
# # Print the graph 		 
# print(graph)

# class graph:
#        def __init__(self,gdict=None):
#         if gdict is None:
#          gdict = []
#          self.gdict = gdict
# # Get the keys of the dictionary
#        def getVertices(self):
#         return list(self.gdict.keys())
# # Create the dictionary with graph elements
# graph_elements = { 
#    "a" : ["b","c"],
#    "b" : ["a", "d"],
#    "c" : ["a", "d"],
#    "d" : ["e"],
#    "e" : ["d"]
# }
# g = graph(graph_elements)
# print(g.getVertices())


# # Program to count islands in boolean 2D matrix
# class Graph:

# 	def __init__(self, row, col, g):
# 		self.ROW = row
# 		self.COL = col
# 		self.graph = g

# 	# A function to check if a given cell
# 	# (row, col) can be included in DFS
# 	def isSafe(self, i, j, visited):
# 		# row number is in range, column number
# 		# is in range and value is 1
# 		# and not yet visited
# 		return (i >= 0 and i < self.ROW and
# 				j >= 0 and j < self.COL and
# 				not visited[i][j] and self.graph[i][j])
			

# 	# A utility function to do DFS for a 2D
# 	# boolean matrix. It only considers
# 	# the 8 neighbours as adjacent vertices
# 	def DFS(self, i, j, visited):

# 		# These arrays are used to get row and
# 		# column numbers of 8 neighbours
# 		# of a given cell
# 		rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
# 		colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
		
# 		# Mark this cell as visited
# 		visited[i][j] = True

# 		# Recur for all connected neighbours
# 		for k in range(8):
# 			if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
# 				self.DFS(i + rowNbr[k], j + colNbr[k], visited)


# 	# The main function that returns
# 	# count of islands in a given boolean
# 	# 2D matrix
# 	def countIslands(self):
# 		# Make a bool array to mark visited cells.
# 		# Initially all cells are unvisited
# 		visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

# 		# Initialize count as 0 and traverse
# 		# through the all cells of
# 		# given matrix
# 		count = 0
# 		for i in range(self.ROW):
# 			for j in range(self.COL):
# 				# If a cell with value 1 is not visited yet,
# 				# then new island found
# 				if visited[i][j] == False and self.graph[i][j] == 1:
# 					# Visit all cells in this island
# 					# and increment island count
# 					self.DFS(i, j, visited)
# 					count += 1

# 		return count


# graph = [[1, 1, 0, 0, 0],
# 		[0, 1, 0, 0, 1],
# 		[1, 0, 0, 1, 1],
# 		[0, 0, 0, 0, 0],
# 		[1, 0, 1, 0, 1]]


# row = len(graph)
# col = len(graph[0])

# g = Graph(row, col, graph)

# print ("Number of islands is:")
# print (g.countIslands())

# """
# A Python program to demonstrate the adjacency
# list representation of the graph
# """

# # A class to represent the adjacency list of the node


# class AdjNode:
# 	def __init__(self, data):
# 		self.vertex = data
# 		self.next = None


# # A class to represent a graph. A graph
# # is the list of the adjacency lists.
# # Size of the array will be the no. of the
# # vertices "V"
# class Graph:
# 	def __init__(self, vertices):
# 		self.V = vertices
# 		self.graph = [None] * self.V

# 	# Function to add an edge in an undirected graph
# 	def add_edge(self, src, dest):
# 		# Adding the node to the source node
# 		node = AdjNode(dest)
# 		node.next = self.graph[src]
# 		self.graph[src] = node

# 		# Adding the source node to the destination as
# 		# it is the undirected graph
# 		node = AdjNode(src)
# 		node.next = self.graph[dest]
# 		self.graph[dest] = node

# 	# Function to print the graph
# 	def print_graph(self):
# 		for i in range(self.V):
# 			print("Adjacency list of vertex {}\n head".format(i), end="")
# 			temp = self.graph[i]
# 			while temp:
# 				print(" -> {}".format(temp.vertex), end="")
# 				temp = temp.next
# 			print(" \n")


# # Driver program to the above graph class
# if __name__ == "__main__":
# 	V = 5
# 	graph = Graph(V)
# 	graph.add_edge(0, 1)
# 	graph.add_edge(0, 4)
# 	graph.add_edge(1, 2)
# 	graph.add_edge(1, 3)
# 	graph.add_edge(1, 4)
# 	graph.add_edge(2, 3)
# 	graph.add_edge(3, 4)

# 	graph.print_graph()


#  #DFS IN graph
 
# class graph:

#     def __init__(self,gdict=None):
#       if gdict is None:
#          gdict = {}
#       self.gdict = gdict
# # Check for the visisted and unvisited nodes
# def dfs(graph, start, visited = None):
#    if visited is None:
#       visited = set()
#    visited.add(start)
#    print(start)
#    for next in graph[start] - visited:
#       dfs(graph, next, visited)
#    return visited

# gdict = { 
#    "a" : set(["b","c"]),
#    "b" : set(["a", "d"]),
#    "c" : set(["a", "d"]),
#    "d" : set(["e"]),
#    "e" : set(["a"])
# }
# dfs(gdict, 'a')

# #BFS 
# import collections
# class graph:
#    def __init__(self,gdict=None):
#       if gdict is None:
#          gdict = {}
#       self.gdict = gdict
# def bfs(graph, startnode):
# # Track the visited and unvisited nodes using queue
#    seen, queue = set([startnode]), collections.deque([startnode])
#    while queue:
#       vertex = queue.popleft()
#       marked(vertex)
#       for node in graph[vertex]:
#          if node not in seen:
#             seen.add(node)
#             queue.append(node)

# def marked(n):
#    print(n)

# # The graph dictionary
# gdict = { 
#    "a" : set(["b","c"]),
#    "b" : set(["a", "d"]),
#    "c" : set(["a", "d"]),
#    "d" : set(["e"]),
#    "e" : set(["a"])
# }
# bfs(gdict, "a")



# arr = [5,2,8,7,1,3]
# arr.sort()
# print(arr)

# import calendar
# year =2022
# month = 2
# print(calendar.month(year,month))

# ladder 


# for i in range(3):
#     print("*   *")
#     print("*   *")
#     if i<2:
#         print("*********")

# remoceing duplicate items 
# l = [1,2,2,3,3,4,5,6,7,7]
# res =list(set(l))
# print(res)

# x,y = "12"
# y,z = "34"
# print(x+y+z)

# x = 5
# def add():
#     x = 3
#     x = x+5
#     print(x)
# add()
# print(x)

# PYRAMID
# rows = 6
# for i in range(1,rows+1):
#     print("*" *i)
 
 # CREATING BEEP SOUND   
# import winsound
# f = 3799
# d = 5000
# winsound.Beep(f,d) 




                                            
    
    
