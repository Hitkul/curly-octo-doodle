def floyd(graph):
    dist = graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i==j:
                dist[i][j] = 0
            elif dist[i][j]==0:
                dist[i][j]= float('Inf')
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

graph =[[0,0,-2,0],
        [4,0,3,0],
        [0,0,0,2],
        [0,-1,0,0]]
dist=floyd(graph)
for row in dist:
    print(row)
