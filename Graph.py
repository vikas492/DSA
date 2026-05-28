# #                                                     undirected  Graph  adjacency matrix


# def createGraph(V,edges):
#     mat = [ [0 for _ in range (V)] for _ in range(V) ]
#     for it in edges :
#         u = it[0]
#         v = it[1]
#         mat[u][v]=1
#         mat[v][u]=1
#     return mat



# V = 3
# edges = [[0,1],[0,2],[1,2]]
# mat = createGraph(V,edges)

# print("Adjacency matrix representation")
# for i in range (V):
#     for j in range (V):
#         print(mat[i][j], end=" ")
#     print()


# #                                                     directed  Graph  adjacency matrix




# def createGraph(V,edges):
#     mat = [ [0 for _ in range (V)] for _ in range(V) ]
#     for it in edges :
#         u = it[0]
#         v = it[1]
#         mat[u][v]=1
        
#     return mat



# V = 3
# edges = [[0,1],[0,2],[1,2]]
# mat = createGraph(V,edges)

# print("Adjacency matrix representation")
# for i in range (V):
#     for j in range (V):
#         print(mat[i][j], end=" ")
#     print()



#                                           adjacency list for undirected graph


# def createGraph(V,edges):
#     adj = [[] for _ in range(V)]
#     for it in edges:
#         u = it[0]
#         v = it[1]
#         adj[u].append(v)
#         adj[v].append(u)
#     return adj




# V = 3
# edges = [[0,1],[0,2],[1,2]]
# adj = createGraph(V,edges)
# print("Adjacency list representation")
# for i in range (V):
#     print(f"{i}:",end=" ")
#     for j in adj[i]:
#         print(j,end=" ")
#     print()




# #                                           adjacency list for Directed graph



# def createGraph(V,edges):
#     adj = [[] for _ in range(V)]
#     for it in edges:
#         u = it[0]
#         v = it[1]
#         adj[u].append(v)
        
#     return adj




# V = 3
# edges = [[0,1],[0,2],[1,2]]
# adj = createGraph(V,edges)
# print("Adjacency list representation")
# for i in range (V):
#     print(f"{i}:",end=" ")
#     for j in adj[i]:
#         print(j,end=" ")
#     print()


