import random


# A class to represent a graph object
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]

        for (src, dest) in edges:
            self.adjList[dest-1].append(src)
            self.adjList[src-1].append(dest)

def colorGraph(graph, n):
    # keep track of the color assigned to each vertex
    result = {}

    # assign a color to vertex one by one
    for u in range(n):

        # check colors of adjacent vertices of `u` and store them in a set
        assigned = set([result.get(i) for i in graph.adjList[u] if i in result])

        # check for the first free color
        color = 0
        for c in assigned:
            if color != c:
                break
            color = color + 1

        # assign vrtex `u` the first available color
        result[u] = color

        print(result)
    x = 0

    for v in range(n):
        if  colors[result[v]] > x:
            x = colors[result[v]]

    print(x)


# Greedy coloring of a graph
if __name__ == '__main__':
    # Add more colors for graphs with many more vertices
    colors = range(2520)

    # List of graph edges as per the above diagram
    edges2 = []
    z=1
    with open("sample1.txt") as f:
        for i in f:

            split = i.split()
            if split[0] == "p":
                vertices = int(split[1])
                continue
            x = (int(split[1]), int(split[2]))
            # print(z,x)
            # z+=1

            edges2.append(x)

    # total number of nodes in the graph (labelled from 0 to 5)
    n = vertices

    # build a graph from the given edges
    graph = Graph(edges2, n)

    # color graph using the greedy algorithm
    colorGraph(graph, n)