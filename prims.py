def prims(graph,source):
    mst =  [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]
    unvisited = set()
    visited = set()
    visited.add(source)
    unvisited = set([i for i in range(len(graph)) if i != source])
    temp = set()
    while len(unvisited)>0:
        temp.clear()
        for v_node in visited:
            for uv_node in unvisited:
                if graph[v_node][uv_node]!=0:
                    temp.add((graph[v_node][uv_node],(v_node,uv_node)))
        value = min(temp)
        unvisited.remove(value[1][1])
        visited.add(value[1][1])
        mst[value[1][0]][value[1][1]] = value[0]
        mst[value[1][1]][value[1][0]] = value[0]
    return mst

graph =[[0,3,0,2,0,0,0,0,4],
        [3,0,0,0,0,0,0,4,0],
        [0,0,0,6,0,1,0,2,0],
        [2,0,6,0,1,0,0,0,0],
        [0,0,0,1,0,0,0,0,8],
        [0,0,1,0,0,0,8,0,0],
        [0,0,0,0,0,8,0,0,0],
        [0,4,2,0,0,0,0,0,0],
        [4,0,0,0,8,0,0,0,0]]
source = 0
mst = prims(graph,source)
for row in mst:
    print(row)
