def dfs(startNode, graph, visited):
    if visited[startNode]:
        return
    visited[startNode] = True

    for neighbor in graph[startNode]:
        dfs(neighbor, graph, visited)

def traverseGraph(graph):
    visited = {}
    for key in graph.keys():
        visited[key] = False
    for key in graph.keys():
        dfs(key, graph, visited)


def main():
    graph = {
        0: [1, 9],
        1: [8],
        2: [3],
        3: [4,5,7],
        4: [3],
        5: [3,6],
        6: [5,7],
        7: [3,6,8,10,11],
        8: [1,7,9],
        9: [0,8],
        10: [7,11],
        11: [7,10],
        12: []
    }
    traverseGraph(graph)

main()