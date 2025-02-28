import sys
sys.stdin = open('D:\\Coding Env\\4. PYTHON\\input.txt', 'r')
sys.stdout = open('D:\\Coding Env\\4. PYTHON\\output.txt', 'w')

"""
Undirected graphs - have edges that do not have a direction. The edges indicate a two-way relationship, in that each edge can be traversed in both directions.

Directed graphs - have edges with direction. The edges indicate a one-way relationship, in that each edge can only be traversed in a single direction.

%%%%%%%% Creating Graphs %%%%%%%%

1. Adjacency Matrix :
One way to represent the information in a graph is with a square adjacency matrix. The nonzero entries in an adjacency matrix indicate an edge between two nodes, and the value of the entry indicates the weight of the edge. The diagonal elements of an adjacency matrix are typically zero, but a nonzero diagonal element indicates a self-loop, or a node that is connected to itself by an edge.
"""


class Graph:
    def __init__(self, edges):
        self.shortestPath = []  # shortest path as per min no. of stops
        self.graph_dict = {}
        self.edges = edges
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_all_routes(self, start, end, path=[]):
        path = path+[start]
        # print("Path", path) # debug
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        allPath = []
        for node in self.graph_dict[start]:
            if node not in path:
                newPath = self.get_all_routes(node, end, path)
                # print("new Path", newPath) # debug
                for i in newPath:
                    allPath.append(i)
                # print("all path",allPath) # debug
        s = 10000
        if len(allPath)==1:
            self.shortestPath = allPath[0]
        else:
            for route in allPath:
                if len(route) < s:
                    s = len(route)
                    self.shortestPath = route
        return allPath


if __name__ == "__main__":
    edges = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Brazil"),
    ]

    graphRoute = Graph(edges)
    # print(graphRoute.graph_dict)
    print("All routes",graphRoute.get_all_routes("Mumbai", "Paris"))
    print("shortest route",graphRoute.shortestPath)
