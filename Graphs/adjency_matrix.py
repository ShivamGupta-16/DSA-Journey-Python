def create_adj_matrix(num_vertices,edges):
    adj_matrix = [[0] * num_vertices for _num in range(num_vertices)]
    
    for (u,v) in edges:
        adj_matrix[u][v] = 1
    return adj_matrix
    
    
        
edges= [(0,1),(2,3),(1,2),(3,3)]
print(create_adj_matrix(4,edges))