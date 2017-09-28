def dijkstra(graph,source_index):
    dist = [float('Inf')]*len(graph)
    prev = [float('Inf')]*len(graph)
    dist[source_index] = 0
    no_of_vertex = len(graph)
    set_of_vertex = set()
    set_of_vertex = set([(dist[i],i) for i in range(no_of_vertex)])

    while len(set_of_vertex)>0:
        current_node = min(set_of_vertex)[1]
        set_of_vertex.remove(min(set_of_vertex))
        neighbor = [graph[current_node].index(node) for node in graph[current_node] if node!=0]
        for node in neighbor:
            alt = dist[current_node] + graph[current_node][node]
            if alt<dist[node]:
                temp = dist[node]
                dist[node] = alt
                prev[node] = current_node
                set_of_vertex.remove((temp,node))
                set_of_vertex.add((dist[node],node))
    return dist , prev



graph = [[0,2,7,0,0],
         [0,0,3,8,5],
         [0,2,0,1,0],
         [0,0,0,0,4],
         [0,0,0,5,0]]
source = 0
dist,prev = dijkstra(graph,source)
print(dist)
