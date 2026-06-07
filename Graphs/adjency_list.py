class Graph:
    def __init__(self):
        self.adj_list={}
        
    def add_vertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
        
    def add_edges(self,vertex1,vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)
        
    def display(self):
        for vertex in self.adj_list:
            print(f"{vertex}: {self.adj_list[vertex]}")
            
            
g = Graph()
g.add_edges("A","B")
g.add_edges("A","C")
g.display()
            